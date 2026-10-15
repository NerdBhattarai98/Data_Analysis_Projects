import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\Anbit Bhattarai\Desktop\Data_Analysis_Projects\01-spotify-tracks\spotify_dataset.csv")

print(df)

# ### Level 1: Foundations
# 1. Load the CSV and display the first 10 rows
print(df.head(10))
# 2. Display the last 5 rows and 5 random rows
print(df.tail(5))
print(df.sample(5).to_string()) #Gives Random 5 rows

# 3. Find the number of rows and columns using `shape`

print(df.shape)
# (114000, 21)
# 114000 rows and 21 column

# 4. Inspect column names, data types and non-null counts using `info()`

print(df.columns)
print(df.dtypes)
print(df.count())
# 5. Select five relevant columns (track name, artist, popularity, energy, danceability)
print(df[["track_name", "artists", "popularity", "energy", "danceability"]])
# 6. Count unique artists, genres and track IDs

print(df["artists"].nunique())
print(df["track_genre"].nunique())
print(df["track_id"].nunique())