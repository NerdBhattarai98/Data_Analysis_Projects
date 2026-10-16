import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\Anbit Bhattarai\Desktop\Data_Analysis_Projects\01-spotify-tracks\spotify_dataset.csv")

# print(df)

# # ### Level 1: Foundations
# # 1. Load the CSV and display the first 10 rows
# print(df.head(10))
# # 2. Display the last 5 rows and 5 random rows
# print(df.tail(5))
# print(df.sample(5).to_string()) #Gives Random 5 rows

# # 3. Find the number of rows and columns using `shape`

# print(df.shape)
# # (114000, 21)
# # 114000 rows and 21 column

# # 4. Inspect column names, data types and non-null counts using `info()`

# print(df.columns)
# print(df.dtypes)
# print(df.count())
# # 5. Select five relevant columns (track name, artist, popularity, energy, danceability)
# print(df[["track_name", "artists", "popularity", "energy", "danceability"]])
# # 6. Count unique artists, genres and track IDs

# print(df["artists"].nunique())
# print(df["track_genre"].nunique())
# print(df["track_id"].nunique())

# # ### Level 2: Cleaning and selection

# #7. Count missing values per column and rank the columns

# print(df.isna().sum().sort_values(ascending=False))
# #8. Find duplicate rows and investigate duplicate track IDs separately
# print("Exact duplicate rows:", df.duplicated().sum())

# duplicated_tracks = df[df.duplicated(subset=["track_id"],keep= False)]
# print(duplicated_tracks[["track_id", "track_name", "artists", "album_name"]])

# #Using Numpy
# # #9. Calculate the percentage of missing values per column using NumPy

# missing_values = missing_percentages_np = np.mean(df.isna().to_numpy(), axis=0) * 100
# missing_series = pd.Series(missing_values,index = df.columns)
# print(missing_series)



# print(df.isna().sum())
# print(df.count())
# print((df.isna().sum()/df.count())*100)

# # Unnamed: 0          0.000000
# # track_id            0.000000
# # artists             0.000877
# # album_name          0.000877
# # track_name          0.000877
# # popularity          0.000000
# # duration_ms         0.000000
# # explicit            0.000000
# # danceability        0.000000
# # energy              0.000000
# # key                 0.000000
# # loudness            0.000000
# # mode                0.000000
# # speechiness         0.000000
# # acousticness        0.000000
# # instrumentalness    0.000000
# # liveness            0.000000
# # valence             0.000000
# # tempo               0.000000
# # time_signature      0.000000
# # track_genre         0.000000
# # dtype: float64

# #10. Filter tracks with popularity greater than 70

# print(df[df["popularity"] > 70])
# #11. Filter tracks with energy above 0.7 and danceability above 0.6

# print(df[(df["energy"] > 0.7) & (df["danceability"] > 0.6)])
# #12. Sort tracks by popularity, duration and energy in different orders

# print(df.sort_values(by="popularity" , ascending= False).head(5))
# print(df.sort_values(by="duration_ms" , ascending= True))
# print(df.sort_values(by="energy" , ascending= False))

# # ### Level 3: Grouping and feature engineering
# # -13. Find the 20 most popular tracks
# print(df.sort_values(by="popularity",ascending=False).head(20))
# # -14. Count tracks by genre and identify the most common genres

# tracks = df.groupby("track_genre")
# print(tracks["track_genre"].count().sort_values(ascending=False))
# # -15. Calculate mean, median and standard deviation of popularity
# # popularity = df.groupby("popularity")
# print("Mean: ",df["popularity"].mean())
# print("Median: ",df["popularity"].median())
# print("Standard Deviation: ",df["popularity"].std())

# # -16. Find the 10 artists with the most tracks
# singer = df.groupby("artists")
# print(singer["artists"].count().sort_values(ascending=False).head(10))
# # -17. Create a duration-in-minutes column from milliseconds

# df["duration in minutes"] = df["duration_ms"]/60000
# print(df)

# # df.to_csv(r"C:\Users\Anbit Bhattarai\Desktop\Data_Analysis_Projects\01-spotify-tracks\spotify_dataset.csv")
# # -18. Create a popularity category (low, medium, high) with documented thresholds


# # df["category"] = np.where(
# #     df["popularity"] >= 70,                                    
# #     "High",                                                     
# #     np.where(
# #         (df["popularity"] >= 40) & (df["popularity"] <= 69),     
# #         "Mid",                                                 
# #         "Low"                                                    
# #     )
# # )
# # print(df)

# #USING LOC

# df["category"] = "Low"

# df.loc[(df["popularity"] >=39) | (df["popularity"] <=69),"category"] = "Mid"
# df.loc[df["popularity"] > 70,"category"] = "High"

# print(df)

# df = df.T.drop_duplicates().T
# # df.to_csv(r"C:\Users\Anbit Bhattarai\Desktop\Data_Analysis_Projects\01-spotify-tracks\spotify_dataset.csv")

### Level 4: Statistical analysis
#19. Calculate the 25th, 50th and 75th percentiles of popularity with NumPy

q1,q2,q3 = np.percentile(df["popularity"],[25,50,75])
print(q1)
print(q2)
print(q3)
#20. Classify tracks as high-energy or low-energy using `np.where()`

q1,q2,q3 = np.percentile(df["energy"],[25,50,75])

print(q1)
print(q2)
print(q3)

df["energy_level"] = np.where(df["energy"]>=0.685,"high-energy","low_energy")
print(df)


#21. Calculate the correlation of popularity with energy and with danceability

corr = np.corrcoef(df[["energy","danceability"]], rowvar=False)
print(corr)

#Not so correlated after all

#22. Compare average popularity for explicit and non-explicit tracks

avg_popularity = df.groupby('explicit')['popularity'].mean()
print(avg_popularity)
#23. Use the IQR method to identify unusually long tracks

q1,q2,q3 = np.percentile(df["duration_ms"],[25,50,75])

print(q1)
print(q2)
print(q3)

InQuRa= q3 - q1

LowerLimit = q1 - InQuRa * 1.5
UpperLimit = q3 + InQuRa * 1.5

print(LowerLimit,UpperLimit)

print(df[df["duration_ms"] > UpperLimit])


#24. Find genres with above-overall-median popularity (minimum tracks per genre)

import pandas as pd


overall_median = df['popularity'].median()


min_tracks = 100
genre_counts = df['track_genre'].value_counts()
valid_genres = genre_counts[genre_counts >= min_tracks].index


filtered_df = df[df['track_genre'].isin(valid_genres)]


genre_pop = filtered_df.groupby('track_genre')['popularity'].mean()


top_genres = genre_pop[genre_pop > overall_median]

print(f"Overall Median Popularity: {overall_median}")
print("\nGenres exceeding overall median popularity:")
print(top_genres.sort_values(ascending=False))

# ### Level 5: Analytical challenges
#25. Compare the top 10% and bottom 10% of tracks across audio features

sorted = df.sort_values(by="popularity",ascending=False)
print(sorted)



q1,q2,q3 = np.percentile(df["popularity"],[25,50,75])

InQuRa= q3 - q1

LowerLimit = q1 - InQuRa * 1.5
UpperLimit = q3 + InQuRa * 1.5

print(q1)
print(q2)
print(q3)

print(LowerLimit,UpperLimit)

# print(sorted.head(11400))
# print(sorted.tail(11400))

top10 = sorted.head(11400)
bottom10 = sorted.tail(11400)

print(top10[["danceability","energy","acousticness","valence"]].mean())
print(bottom10[["danceability","energy","acousticness","valence"]].mean())

# danceability    0.601261  
# energy          0.654614
# acousticness    0.255201
# valence         0.491983

# danceability    0.577675
# energy          0.626090
# acousticness    0.329594
# valence         0.510169
# dtype: float64
#26. Rank artists with at least 10 tracks by median popularity
# 1. Group by artist and calculate track count and median popularity
artist_stats = df.groupby('artists')['popularity'].agg(['count', 'median'])

# 2. Filter for artists with at least 10 tracks
artists_at_least_10 = artist_stats[artist_stats['count'] >= 10]

# 3. Sort by median popularity (highest to lowest)
ranked_artists = artists_at_least_10.sort_values(by='median', ascending=False)

print(ranked_artists.head(10))

#27. Identify tracks that are highly popular, energetic and danceable

high_pop = df['popularity'] > 80
high_energy = df['energy'] > 0.7
high_dance = df['danceability'] > 0.7

hit_tracks = df[high_pop & high_energy & high_dance]
print(hit_tracks)
#28. Check whether mean and median popularity give different genre rankings

group = df.groupby("track_genre")
print(group["popularity"].mean())
print(group["popularity"].median())

#yes but not that much

#29. Build a genre summary DataFrame (count, median popularity, average energy and danceability)

print(group.describe())

genre_summary = df.groupby('track_genre').agg(
    count=('popularity', 'count'),                  # Counts how many tracks per genre
    median_popularity=('popularity', 'median'),     # Median popularity
    avg_energy=('energy', 'mean'),                  # Average energy
    avg_danceability=('danceability', 'mean')       # Average danceability
)

print(genre_summary.head(10))
#30. Write five findings, two limitations and three future questions

# Five findings:
#Energy and Danceability not being correlated to each other
#The Popular SOngs tend to have more energy and danceability and less populat songs focus on temp and acoustics
# Explicit tracks tend to achieve higher average popularity scores than non-explicit tracks
#Genre Summarization says that the top genres like pops and hip hops are more popular than acoustics
#

#Limitations:
# While we found that hit songs have higher energy and danceability, this doesn't mean making a song more energetic will automatically make it popular
#This data is based on spotify so like aucostic fans must still listen to the songs from other means and radios

#Future qns:

# Since Spotify data shows lower popularity for acoustic music, do acoustic fans mainly listen to music on other platforms or formats (like vinyl or radio)?
# If high energy and danceability don't automatically make a song popular, what other non-audio factors (like artist fame or marketing) actually drive a hit?
# Why do explicit tracks tend to have higher average popularity than clean tracks among mainstream listeners?