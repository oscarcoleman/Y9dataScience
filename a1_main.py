import pandas as pd
# Load the dataset
df = pd.read_csv("athlete_events.csv")
df_2 = pd.read_csv("athlete_events_cleaned.csv")

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

# Filter for male athletes only
male_athletes = df[df['Sex'] == 'M']
print(male_athletes.head())

# Filter for athletes older than 35
older_athletes = df[df['Age'] > 35]
print(older_athletes[['Name', 'Age', 'Sport']].head())

# Filter for athletes from Australian Swimming
australian_swimmers = df[(df['Team'] == 'Australia') & (df['Sport'] == 'Swimming')]
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

sport_counts_male = male_athletes['Sport'].value_counts()
print(sport_counts_male.head())

# Average weight by sex and sport
avg_weight_females = female_athletes.groupby('Sport')['Weight'].mean().sort_values(ascending=False)
print(avg_weight_females.head())

avg_weight_males = male_athletes.groupby('Sport')['Weight'].mean().sort_values(ascending=False)
print(avg_weight_males.head())

# Filter Under 18s and save to new CSV
gymnasts = df[df['Age'] < 18]
gymnasts.to_csv('athletes_under_18.csv', index=False)

# Filter Gold Medalists and save to new CSV
gymnasts = df[df['Medal'] == 'Gold']
gymnasts.to_csv('gold_medalists.csv', index=False)

# Count missing values in each column
print(df.isnull().sum())

# Drop rows missing both height and weight
df_cleaned = df.dropna(subset=['Height', 'Weight'])
print(df_cleaned.shape)

# Unique values 
print(df_cleaned['Sex'].unique())
print(df_cleaned['Medal'].unique()) 
print(df_cleaned['Age'].unique())
print(df_cleaned['Name'].unique())
print(df_cleaned['Games'].unique())
print(df_cleaned['Team'].unique())
print(df_cleaned['Season'].unique())
print(df_cleaned['City'].unique())
print(df_cleaned['Event'].unique())
print(df_cleaned['Sport'].unique())

# Strip whitespace from strings
df_cleaned['Medal'] = df_cleaned['Medal'].str.strip()

# Check again for missing values
#print(df_cleaned.isnull().sum())

# Get stats after cleaning
print(df_cleaned.describe())

# Save your cleaned version
df_cleaned.to_csv("athlete_events_cleaned.csv", index=False)

# ensure cleaned file is cleaned 

print(df_2.isnull().sum())

print(df.isnull().sum())