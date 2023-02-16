import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


filepath = 'csv_file\data12.csv'
df = pd.read_csv(filepath)
print(df)


X = df[['1th','2th','3th','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th'
        ,'14th','15th','16th','17th','18th','19th','20th','21th','22th','23th']]

Y = df['Ans']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=77    
)

print(len(X_train))
print(len(Y_test))


clf = RandomForestClassifier(random_state=77)
clf.fit(X_train, Y_train)
pred = clf.predict(X_test)
print(pred)

#正解率をaccuracyに代入している。
accuracy = accuracy_score(Y_test, pred)
print(accuracy)