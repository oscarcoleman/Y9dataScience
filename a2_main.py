import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("athlete_events_cleaned.csv")

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