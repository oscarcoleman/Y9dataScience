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
### Tuesday 10/6
Today I created the folders "directory_practice" and "wk4_dictionary_data_work", and worked on creating, accessing and using files and directories, e.g
```
parent_folder = "directory_practice"
parent_file = "athlete_events.csv"

parent_file_path = parent_folder + "/" + parent_file

file = open(parent_file_path, "r", encoding="utf-8")

contents = file.read()

print(contents)

file.close()
```
I also wrote the ran the following code to practice moving data:
```
import pandas as pd

def main():
    # Create a DataFrame with some sample data
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }
    
    df = pd.DataFrame(data)
    
    # Display the DataFrame
    print("DataFrame:")
    print(df)

    # Save the DataFrame to a CSV file
    df.to_csv('sample_data.csv', index=False)
    print("\nDataFrame saved to 'sample_data.csv'.")

    # Read the DataFrame from the CSV file
    df_loaded = pd.read_csv('sample_data.csv')

    print("\nDataFrame loaded from 'sample_data.csv':")

    # Display the loaded DataFrame
    print(df_loaded)
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

#### Why do you think these three operations [dictionaries] are key to working with data and information?

Dictionaries are important for categorising and labelling data and information, which is desirable when dealing with large piles of data, some distinct and others conforming to a pattern.

## Week 4
### Friday 6/6
#### Which 3 columns have the most missing values?

1. Medals
2. Weight
3. Height

#### Why might this happen in real-world Olympic data?

In the case of medals, not every athlete will actually win a medal. In regards to height and weight, there may be errors in records (when dealing with such large amounts of data, it is understandable), especially if height and weight are not greatly important to the sport.

#### How many rows did you remove?

208653

#### What are the pros and cons of dropping data?

The advantages would be cleaning out incomplete data, which may well otherwise be getting in the way. However, there may still be important data, even if incomplete, such as an error in recording a gold medalist who would now be wiped from the record.

### Friday 13/6

#### Did cleaning improve the dataset?

Using the following code to compare the cleaned vs orginal filesw, with df being the original and df_2 being the cleaned file:
```
print(df.isnull().sum())

print(df_2.isnull().sum())
```
I found that the cleaned file had cleaned all missing values for height and weight, and had substantially reduced missing values of medals and age, although these were not entirely eliminated.

#### What questions could now be answered more confidently?

Inquiries into height and weight would be more accurate and complete.

### Week 4 Reflection Questions

#### What was the dirtiest column in the dataset?

The medals column

#### How did you decide when to drop vs fix missing data?

If other data in the row may still be relevant (not false), then fixing would be wiser.

#### Why is data cleaning so important in real-world projects?

Data cleaning is vital to ensure improved efficiency in datasets, and in eliminating incomplete data which would not be useful.
