import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("athlete_events_cleaned.csv")
df2 = pd.read_csv("gold_medalists.csv")

sport_counts = df['Sport'].value_counts().head(10)

print(sport_counts)

sport_counts.plot(kind='bar', title='Top 10 Sports by Athlete Count')
plt.xlabel('Sport')
plt.ylabel('Number of Athletes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_10_sports.png")
plt.show()

median_age = df.groupby('Year')['Age'].median()

median_age.plot(kind='line', title='Median Athlete Age Over Time')
plt.xlabel('Olympic Year')
plt.ylabel('Median Age')
plt.grid(True)
plt.tight_layout()
plt.savefig("median_age_line.png")
plt.show()

df['Weight'].plot(kind='hist', bins=10, title='Distribution of Athlete Weights')
plt.xlabel('Weight (kg)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig("weight_distribution.png")
plt.show()

medal_counts = df[df['Medal'] != 'None']['Medal'].value_counts()

medal_counts.plot(kind='pie', autopct='%1.1f%%', title='Distribution of Medal Types')
plt.ylabel('')  # Removes default y-axis label
plt.tight_layout()
plt.savefig("medal_pie_chart.png")
plt.show()

country_medal_counts = df2['Team'].value_counts().head(10)

country_medal_counts.plot(kind='bar', title='Gold Medals by Country')
plt.xlabel('Country')
plt.ylabel('Number')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("country_medal_counts_bar_graph.png")
plt.show()

country_counts = df['Team'].value_counts().head(10)

country_counts.plot(kind='bar', title='Countries by Participation')
plt.xlabel('Country')
plt.ylabel('Number')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("country_counts_bar_graph.png")
plt.show()