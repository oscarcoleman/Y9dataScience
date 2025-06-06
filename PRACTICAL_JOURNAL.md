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
# Filter for female athletes only
female_athletes = df[df['Sex'] == 'F']
print(female_athletes.head())

# Filter for male athletes only
male_athletes = df[df['Sex'] == 'M']
print(male_athletes.head())
```

### Week 3 Reflection Questions
#### What was the easiest filtering task and why?

The filters that were measuring a true or false of one quality of one column (due to simplicity), such as the following
```
# Filter Under 18s and save to new CSV
gymnasts = df[df['Age'] < 18]
gymnasts.to_csv('athletes_under_18.csv', index=False)
```
#### What was the most difficult grouping or sorting task?

ALbeit not greatly difficult, the following required me to change "df" to a specifically made variable, as is shown below

These
```
avg_weight_females = female_athletes.groupby('Sport')['Weight'].mean().sort_values(ascending=False)
print(avg_weight_females.head())

avg_weight_males = male_athletes.groupby('Sport')['Weight'].mean().sort_values(ascending=False)
print(avg_weight_males.head())
```
Required these
```
# Filter for female athletes only
female_athletes = df[df['Sex'] == 'F']
print(female_athletes.head())

# Filter for male athletes only
male_athletes = df[df['Sex'] == 'M']
print(male_athletes.head())
```
#### What trends surprised you in the Olympic data?

Skiing was more popular among females than males

#### What kinds of real-world questions could this kind of analysis help answer?

Gender equality in sports

#### Why do you think these three operations [dictionaires] are key to working with data and information?

Disctionaries are important for categorising and labelling data and information, which is desirable when dealing with large piles of data, some distinct and others conforming to a pattern.
