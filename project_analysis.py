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

#total number of athletes per country
athlete_counts = df2['NOC'].value_counts()

#total number of medals won per country
medal_counts = df['NOC'].value_counts()

# combines two above in dataframe
result = pd.DataFrame({
    "Total Athletes": athlete_counts,
    "Total Medals": medal_counts
}).fillna(0)

# calculate medals per athlete 
result["Medals per Athlete"] = result["Total Medals"] / result["Total Athletes"] 

#convert to percentage
result["Medal-Athlete Percentage Ratio"] = result["Medals per Athlete"] * 100

athlete_medal_ratio = result["Medal-Athlete Percentage Ratio"]

# sort medal winner percentage ratio in descending order
athlete_medal_ratio_sorted = athlete_medal_ratio.sort_values(ascending=False)

country_medal_efficiency_counts = athlete_medal_ratio_sorted.head(10)

print(result.head(10))

#Plot top ten in bar chart
country_medal_efficiency_counts.plot(kind='bar', title='Countries by Medal-Athlete ratio')
plt.xlabel('Country')
plt.ylabel('Percentage')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("country_medal_athlete_ratios_top10.png")
plt.show()