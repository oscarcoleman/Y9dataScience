import pandas as pd
# Load the dataset
df = pd.read_csv("athlete_events.csv")

# Show the first 5 rows
print(df.head())

# Show the column names
print(df.columns)

# Shows top sports
print(df['Sport'].value_counts().head())

# Shows number of male vs female athletes
print(df['Sex'].value_counts())

# Shows stats such as mean and min
print(df.describe())

# Shows country codes (of athletes participating)
print(df['NOC'].nunique())
print(df['NOC'].unique())