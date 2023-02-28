import pandas as pd
import pickle

# ファイル読み込み
df = pd.read_csv('namelist.csv',sep=",")


df = df[['name', 'label']].drop_duplicates()
df = df.sample(frac=1).reset_index(drop=True)

# bi-gramを取る
def bigram(text):
    return [text[i:i+2] for i in range(len(text) - 1)] + ['end_'+text[-2:], 'end_'+text[-1]]

df['bi_yomi'] = df.name.apply(bigram)

from sklearn.preprocessing import MultiLabelBinarizer
mlb = MultiLabelBinarizer()
mlb.fit(df.bi_yomi)
with open('mld.pickle', mode = 'wb') as f:
    pickle.dump(mlb,f)

mlb.classes_

from sklearn.model_selection import KFold

# 渡されたscikit-learnのclassifierに対して学習して評価する
# probabilityが0.6以上だったら判定できたことにする
def train_and_test(classifier, df, mlb, threshold=0.6):
    kf = KFold(n_splits=5)
    for train, test in kf.split(df):
        # 訓練データとテストデータにsplit
        train_df = df.loc[train]
        test_df = df.loc[test]

        # MultiLabelBinarizerを使ってベクトルに
        train_features = mlb.transform(train_df.bi_yomi)
        test_features = mlb.transform(test_df.bi_yomi)

        # 学習
        classifier.fit( train_features, train_df.label )


        # 評価
        test_proba = classifier.predict_proba(test_features)
        test_df['proba_male'] = [p[0] for p in test_proba]
        test_df['proba_female'] = [p[1] for p in test_proba]
        test_df['predict'] = -1
        # probabilityがthreshold以上の場合だけ判定結果を採用（ここでは0.6）
        test_df.loc[test_df.proba_male >= threshold, 'predict'] = 0
        test_df.loc[test_df.proba_female >= threshold, 'predict'] = 1
        all_len = len(test_df)
        predictable = len(test_df[test_df.predict != -1])
        tp = sum(test_df['predict'] == test_df['label'])
        fp = sum((test_df.predict != -1) & (test_df['predict'] != test_df['label']))
        class_name = str(classifier.__class__).split('.')[-1][:-2]
        print('{}: all={}, predictable={}, precision={:.03f}, recall={:.03f}'.format(
                class_name, all_len, predictable, tp / predictable, tp / all_len))
    print(test_df)
    import pickle

    with open('model.pickle', mode='wb') as f:
        pickle.dump(classifier,f)
        
# # logistic regression
# from sklearn.linear_model import LogisticRegression
# classifier = LogisticRegression(C=1.0, penalty='l2')
# train_and_test(classifier, df, mlb)

# svm
from sklearn import svm
classifier = svm.SVC(probability=True, C=0.1)
train_and_test(classifier, df, mlb)



# # xgboost（デフォルトパラメータだとrecallが0.3とかになったのでちょっと調整）
# from xgboost import XGBClassifier
# classifier = XGBClassifier(objective='binary:logistic', n_estimators=300, learning_rate=0.2)
# train_and_test(classifier, df, mlb)