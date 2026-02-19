import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("movies.csv")
current_year = 2026
df_last_decade = df[df["year"] >= current_year - 10]
df_last_decade["genre"] = df_last_decade["genre"].str.split(",")
df_exploded = df_last_decade.explode("genre")
df_exploded["genre"] = df_exploded["genre"].str.strip()
genre_ratings = (
    df_exploded.groupby("genre")["rating"]
    .mean()
    .sort_values(ascending=False)
)
top_genres = genre_ratings.head(10)
print("\nTop 10 Rated Genres:\n")
print(top_genres)
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")
sns.barplot(
    x=top_genres.values,
    y=top_genres.index
)
plt.title("Top 10 Movie Genres by Average Rating")
plt.xlabel("Average Rating")
plt.ylabel("Genre")
plt.tight_layout()
plt.show()