import pandas as pd

# Load the dataset
df = pd.read_csv("premier_league_2009_2010.csv")

# Basic Overview
print("Shape:", df.shape)
print("Columns:\n", df.columns)
print("Missing values:\n", df.isnull().sum())
print("Summary stats:\n", df.describe())

# Sample EDA
import matplotlib.pyplot as plt
import seaborn as sns

# Plot: Goals by Home vs Away Team
sns.histplot(df['FTHG'], color='blue', label='Home Goals', kde=True)
sns.histplot(df['FTAG'], color='red', label='Away Goals', kde=True)
plt.legend()
plt.title("Distribution of Home and Away Goals")
plt.xlabel("Goals Scored")
plt.show()

# Match outcomes count
sns.countplot(x='FTR', data=df)
plt.title("Match Results Distribution (H: Home Win, D: Draw, A: Away Win)")
plt.show()


