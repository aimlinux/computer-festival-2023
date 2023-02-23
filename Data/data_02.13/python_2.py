import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


#filepath = 'csv\csv_file\list.csv'
filepath = 'csv\csv_file\list_2".csv'
df = pd.read_csv(filepath)
print(df)


print("/////////////////////////////////")


X = df[['one', 'two']]

Y = df['ans']

#X_train, X_test, Y_train, Y_test = train_test_split(
#    X, Y, test_size=0.2, random_state=77
#)
#
#clf = RandomForestClassifier(random_state=77)
#clf.fit(X_train, Y_train)

#pred = clf.predict(X_test)
#accuracy = accuracy_score(Y_test, pred)

