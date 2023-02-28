import pickle
import pandas as pd


# モデルのオープン
with open('model.pickle', mode='rb') as f:
    clf = pickle.load(f)

text = "かずま"

# bi-gramを取る
def bigram(text):
    return [text[i:i+2] for i in range(len(text) - 1)] + ['end_'+text[-2:], 'end_'+text[-1]]

name = bigram(text)


df = pd.read_csv('namelist.csv',sep=",")



df['bi_yomi'] = df.name.apply(bigram)


from sklearn.preprocessing import MultiLabelBinarizer
mlb = MultiLabelBinarizer()
mlb.fit(df.bi_yomi)
mlb.classes_

train_name = mlb.transform(name)




#　モデルを用いた予測
ans = clf.predict(train_name)

print(ans)
#if ans == 0:
#    print("男です")
#if ans == 1:
#    print("女です")
