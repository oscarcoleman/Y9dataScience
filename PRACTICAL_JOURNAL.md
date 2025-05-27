# Y9dataScience
## Week 1
Worked on Activities A, in Google Classroom, learned about data science basics.

## Week 2
### Monday
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
### Tuesday
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
