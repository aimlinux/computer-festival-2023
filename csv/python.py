import pandas as pd
from pathlib import Path

filepath = 'csv\list.csv'
print(Path(filepath).read_text())

print("///////////////////////")

df = pd.read_csv(filepath, na_values=['--'])
print(df)


