import pandas as pd
import pickle
import warnings

warnings.simplefilter('ignore')

# ファイル読み込み
df = pd.read_csv('namelist.csv',sep=",")


# df = df[['name', 'label']].drop_duplicates()
# df = df.sample(frac=1, ignore_index=True)

text = input()

list1 = [text,0]
index1 = ['name','label']

target = pd.Series(data = list1,index = index1)





# bi-gramを取る
def bigram(text):
    return [text[i:i+2] for i in range(len(text) - 1)] + ['end_'+text[-2:], 'end_'+text[-1]]

target['bi_yomi'] = bigram(text) 
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
def train_and_test(classifier, df, mlb,target,fcount=0,mcount=0 ,threshold=0.6):
    kf = KFold(n_splits=5)
    for train, test in kf.split(df):
        # 訓練データとテストデータにsplit
        train_df = df.loc[train]
        test_df = df.loc[test]
        
        test_df.loc[4998] = (target)

        
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
        
        s = test_df["predict"][4998]
        
#         print(test_df)
        if s==1:fcount= fcount+1
        if s==0: mcount = mcount +1
    if fcount >= 3:
        return 1
    if mcount >= 3:
        return 0
        
    if fcount+mcount<5:train_and_test(classifier, df, mlb,target)
        
    import pickle

    with open('model.pickle', mode='wb') as f:
        pickle.dump(classifier,f)
        

# svm
from sklearn import svm
classifier = svm.SVC(probability=True, C=0.1)
s = train_and_test(classifier, df, mlb,target)

if s == 1:print("女性です")
if s == 0:print("男性です")








# # xgboost（デフォルトパラメータだとrecallが0.3とかになったのでちょっと調整）
# from xgboost import XGBClassifier
# classifier = XGBClassifier(objective='binary:logistic', n_estimators=300, learning_rate=0.2)
# train_and_test(classifier, df, mlb)