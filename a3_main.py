# clean gold_medalists.csv

import pandas as pd

df = pd.read_csv("gold_medalists.csv")
df2 = pd.read_csv("gold_medalists_cleaned.csv")

# missing value count
print(df.isnull().sum())

df.dropna(inplace=True)

df.to_csv("gold_medalists_cleaned.csv", index=False)

print(df2.isnull().sum())