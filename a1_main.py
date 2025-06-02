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

# Filter for female athletes only
female_athletes = df[df['Sex'] == 'F']
print(female_athletes.head())

# Filter for athletes older than 35
older_athletes = df[df['Age'] > 35]
print(older_athletes[['Name', 'Age', 'Sport']].head())

# Filter for athletes from Australia in Swimming
australian_swimmers = df[(df['Country'] == 'Australia') & (df['Sport'] == 'Swimming')]
print(australian_swimmers.head())

# Sort by height
sorted_by_height = df.sort_values(by='Height', ascending=False)
print(sorted_by_height[['Name', 'Height', 'Sport']].head(10))

# Sort by weight
sorted_by_weight = df.sort_values(by='Weight', ascending=False)
print(sorted_by_weight[['Name', 'Weight', 'Sport']].head(10))

# Count participants in each sport
sport_counts = female_athletes['Sport'].value_counts()
print(sport_counts.head())