# clean gold_medalists.csv

import pandas as pd

df = pd.read_csv("gold_medalists.csv")

# missing value count
print(df.isnull().sum())

df_cleaned = df.dropna(inplace=True)

df_cleaned.to_csv("gold_medalists_cleaned.csv", index=False)

