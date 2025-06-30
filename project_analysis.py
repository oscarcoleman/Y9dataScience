import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("gold_medalists_cleaned.csv")
df2 = pd.read_csv("athlete_events_cleaned.csv")

# filter for data in period 1952-1972
filtered_df = df[(df['Year'] >= 1952) & (df['Year'] <= 1972)]
print(filtered_df.head())

# filter for data in period 2000-2020
filtered_df2 = df[(df['Year'] >= 2000) & (df['Year'] <= 2020)]
print(filtered_df2.head())

print(len(df))
print(len(filtered_df))
print(len(filtered_df2))

a = df[(df['NOC'] == 'USA')]
b = df2[(df2['NOC'] == 'USA')]
c = len(a) / len(b)
print(c)

a2 = df[(df['NOC'] == 'GDR')]
b2 = df2[(df2['NOC'] == 'GDR')]
c2 = len(a2) / len(b2)
print(c2)


