import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\medir\\Downloads\\archive\\netflix_titles.csv")

df.head(10)
df.shape
df.info()
df.describe(include="all")

df = df.drop_duplicates(subset="show_id")

df = df.drop(columns=["description"])

df.isnull().sum()

df["country"] = df["country"].fillna("Unknown")
df["director"] = df["director"].fillna("No Director Listed")
df["duration_num"] = df["duration"].str.extract(r"(\d+)").astype(float)









df["duration_minutes"] = np.where(
    df["type"] == "Movie",
    df["duration_num"],
    np.nan
)

df["seasons"] = np.where(
    df["type"] == "TV Show",
    df["duration_num"],
    np.nan
)




df["Is_Recent"] = np.where(df["release_year"] >= 2015, 1, 0)




plt.figure()
sns.countplot(x="type", data=df)

plt.show()


plt.figure()
plt.hist(df["release_year"].dropna(), bins=20)
plt.show()

plt.figure()
df["country"].value_counts().head(10).plot(kind="bar")
plt.show()

plt.figure()
sns.boxplot(
    x="Is_Recent",
    y="duration_minutes",
    data=df[df["type"] == "Movie"]
)
plt.show()

numeric_df = df[["release_year", "duration_minutes", "seasons", "Is_Recent"]]

plt.figure()
sns.heatmap(numeric_df.corr(), annot=True)
plt.show()
