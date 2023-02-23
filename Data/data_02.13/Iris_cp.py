import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


filepath = 'csv\csv_file\iris_cp.csv'
df = pd.read_csv(filepath)
print(df)


X = df[['First', 'Second', 
        'Third', 'Fourth']]

Y = df['Looking']

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