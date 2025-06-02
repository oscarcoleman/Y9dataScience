# Y9dataScience

All work, including questions, in this markdown file is sourced from the following: https://vormamim-web-programming.gitbook.io/hsc-software-engineering/pandas-for-data-science/week-3/filtering-sorting-and-grouping 

## Week 1
### 23/5
Worked on Activities A, in Google Classroom, learned about data science basics.

## Week 2
### Monday 26/5
I installed pandas on VS code, and ran the following code:
```
import pandas as pd

# Load the dataset
df = pd.read_csv("athlete_events.csv")

# Show the first 5 rows
print(df.head())

# Show the column names
print(df.columns)
```
### Tuesday 27/5
#### Questions

##### How many columns are in the dataset?

15

##### Name 3 of them and explain what they represent.

- Name: Name of athlete

- City: Home city of athlete

- Medal: Medal, if any, won by athlete

##### What do the first 5 rows show?

The stats of the first 5 athletes.

##### What are the top 5 sports?

- Athletics

- Gymnastics

- Swimming

- Shooting

- Cycling

##### Male vs female athletes?

- 196594 Males

- 74522 Females

##### What is the average age?

25.6

##### List oldest and youngest athlete age.

- Oldest is 97

- Youngest is 10

##### Any columns with missing or strange values?

Year and Index have means and whatnot that are irrelevant.

#### Reflection Questions

##### What’s one thing you learned about the Olympics dataset?

It has an extremely large collection of records about athletes, and all of their stats.

##### What did you find challenging in setting up or running Pandas?

Nothing, it all went smoothly.

##### What’s something you'd like to analyse next?

Population stats.

## Week 3
### Tuesday 27/5
#### What do these filters do?

They filter out the data (athletes) that is in accordance with, in one instance, being female and, in another, being older than 35.

#### How many rows were returned?

5

### Monday 2/6
I have worked on writing the following code:
```
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
```
and
```
```
