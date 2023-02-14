import pandas as pd
from sklearn.model_selection import train_test_split


filepath = 'csv\csv_file\list_2.csv'
df = pd.read_csv(filepath)
print(df)

X = df[['1', '2']]

Y = df['ans']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=77
)


