# Data Analysis Projects

A collection of exploratory data analysis (EDA) projects built with Python, Pandas and NumPy. Each project follows 30 structured tasks across five levels, from basic inspection to written analytical findings.

## Objectives

- Build practical skills in data cleaning, filtering, aggregation and statistics.
- Turn raw data into clear, evidence-based conclusions.
- Document every step so the work can be reproduced and reviewed.

## Progress Overview

| # | Project | Level 1 | Level 2 | Level 3 | Level 4 | Level 5 | Tasks Done | Status |
|:-:|---------|:-------:|:-------:|:-------:|:-------:|:-------:|:----------:|:------:|
| 1 | [Spotify Tracks](01-spotify-tracks/) | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0 / 30 | In progress |
| 2 | [Netflix Titles](02-netflix-titles/) | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0 / 30 | Not started |
| 3 | [Formula 1](03-formula-1/) | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0 / 30 | Not started |
| 4 | [International Football](04-international-football/) | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0 / 30 | Not started |
| 5 | [World Happiness 2019](05-world-happiness/) | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0 / 30 | Not started |

**Levels:** 1 Foundations · 2 Cleaning and selection · 3 Grouping and feature engineering · 4 Statistical analysis · 5 Analytical challenges

---

## Task Checklists

<details>
<summary><b>1. Spotify Tracks</b></summary>

### Level 1: Foundations
- [ ] 1. Load the CSV and display the first 10 rows
- [ ] 2. Display the last 5 rows and 5 random rows
- [ ] 3. Find the number of rows and columns using `shape`
- [ ] 4. Inspect column names, data types and non-null counts using `info()`
- [ ] 5. Select five relevant columns (track name, artist, popularity, energy, danceability)
- [ ] 6. Count unique artists, genres and track IDs

### Level 2: Cleaning and selection
- [ ] 7. Count missing values per column and rank the columns
- [ ] 8. Find duplicate rows and investigate duplicate track IDs separately
- [ ] 9. Calculate the percentage of missing values per column using NumPy
- [ ] 10. Filter tracks with popularity greater than 70
- [ ] 11. Filter tracks with energy above 0.7 and danceability above 0.6
- [ ] 12. Sort tracks by popularity, duration and energy in different orders

### Level 3: Grouping and feature engineering
- [ ] 13. Find the 20 most popular tracks
- [ ] 14. Count tracks by genre and identify the most common genres
- [ ] 15. Calculate mean, median and standard deviation of popularity
- [ ] 16. Find the 10 artists with the most tracks
- [ ] 17. Create a duration-in-minutes column from milliseconds
- [ ] 18. Create a popularity category (low, medium, high) with documented thresholds

### Level 4: Statistical analysis
- [ ] 19. Calculate the 25th, 50th and 75th percentiles of popularity with NumPy
- [ ] 20. Classify tracks as high-energy or low-energy using `np.where()`
- [ ] 21. Calculate the correlation of popularity with energy and with danceability
- [ ] 22. Compare average popularity for explicit and non-explicit tracks
- [ ] 23. Use the IQR method to identify unusually long tracks
- [ ] 24. Find genres with above-overall-median popularity (minimum tracks per genre)

### Level 5: Analytical challenges
- [ ] 25. Compare the top 10% and bottom 10% of tracks across audio features
- [ ] 26. Rank artists with at least 10 tracks by median popularity
- [ ] 27. Identify tracks that are highly popular, energetic and danceable
- [ ] 28. Check whether mean and median popularity give different genre rankings
- [ ] 29. Build a genre summary DataFrame (count, median popularity, average energy and danceability)
- [ ] 30. Write five findings, two limitations and three future questions

</details>

<details>
<summary><b>2. Netflix Titles</b></summary>

### Level 1: Foundations
- [ ] 1. Load the CSV and display the first 10 records
- [ ] 2. Inspect the number of rows, columns and column names
- [ ] 3. Identify numerical, categorical and date-related columns
- [ ] 4. Count unique titles, directors, countries and content types
- [ ] 5. Find the earliest and latest release years
- [ ] 6. Count missing values in each column

### Level 2: Cleaning and text processing
- [ ] 7. Find duplicated rows and duplicate show IDs
- [ ] 8. Investigate missing values in director, cast, country and rating
- [ ] 9. Convert `date_added` to datetime, checking invalid dates first
- [ ] 10. Extract the year and month from `date_added`
- [ ] 11. Find titles containing a chosen keyword using string operations
- [ ] 12. Extract numeric duration into a new column, keeping minutes and seasons distinct

### Level 3: Filtering and grouping
- [ ] 13. Count movies and TV shows separately
- [ ] 14. Find the 20 most recent release years in the catalogue
- [ ] 15. Count titles by release year
- [ ] 16. Count titles by content rating
- [ ] 17. Find the 10 most frequently listed directors
- [ ] 18. Find the countries with the most titles, handling multi-country entries

### Level 4: Analytical comparisons
- [ ] 19. Calculate mean, median and standard deviation of movie duration
- [ ] 20. Compare movie durations across release decades
- [ ] 21. Compare content added per year for movies and TV shows
- [ ] 22. Calculate the gap between release year and year added
- [ ] 23. Classify titles by release period using `np.select()`
- [ ] 24. Find ratings disproportionately common in movies versus TV shows

### Level 5: Analytical challenges
- [ ] 25. Identify the release decades with the largest catalogue share
- [ ] 26. Compare the release-year distribution with the addition-year distribution
- [ ] 27. Examine the content-type variety of frequently appearing directors
- [ ] 28. Investigate whether typical movie duration changes across decades
- [ ] 29. Build a summary DataFrame by content type and rating
- [ ] 30. Write five findings, explain the effect of missing data and list three future questions

</details>

<details>
<summary><b>3. Formula 1</b></summary>

### Level 1: Foundations
- [ ] 1. Load the race-results CSV and inspect the first 10 rows
- [ ] 2. Check rows, columns and unique seasons
- [ ] 3. Inspect data types and missing values
- [ ] 4. Count unique drivers and constructors
- [ ] 5. Find the number of recorded results per season
- [ ] 6. Select driver, constructor, season, grid, position and points

### Level 2: Filtering and cleaning
- [ ] 7. Filter race results for a selected season
- [ ] 8. Filter all results for one driver
- [ ] 9. Filter results for one constructor across multiple seasons
- [ ] 10. Investigate missing and non-numeric finishing positions
- [ ] 11. Find podium finishes using valid numeric positions
- [ ] 12. Sort results by points, finishing position and grid position

### Level 3: Aggregation
- [ ] 13. Count recorded appearances per driver
- [ ] 14. Count wins and podiums for every driver
- [ ] 15. Calculate total and average points per driver
- [ ] 16. Calculate total points by constructor and season
- [ ] 17. Find the top constructor in each season
- [ ] 18. Calculate average finishing position (minimum number of valid results)

### Level 4: Derived metrics
- [ ] 19. Create `positions_gained` (grid minus finishing position)
- [ ] 20. Classify results (win, podium, points finish, other, unclassified) with NumPy
- [ ] 21. Calculate each driver's win percentage
- [ ] 22. Calculate each driver's podium percentage
- [ ] 23. Compare mean and median finishing positions for selected drivers
- [ ] 24. Calculate the spread of points per race for drivers with enough results

### Level 5: Analytical challenges
- [ ] 25. Compare two drivers in a selected season (wins, podiums, average finish, points per appearance)
- [ ] 26. Find constructors that scored consistently across several seasons
- [ ] 27. Correlate grid and finishing position, explaining what it can and cannot show
- [ ] 28. Identify drivers who often finish better than they start
- [ ] 29. Build a driver-season summary DataFrame
- [ ] 30. Write five findings and explain the limits of comparing eras

</details>

<details>
<summary><b>4. International Football</b></summary>

### Level 1: Foundations
- [ ] 1. Load the CSV and inspect the first 10 rows
- [ ] 2. Find dimensions and data types
- [ ] 3. Convert the match date to datetime and find the date range
- [ ] 4. Count unique home teams, away teams and tournaments
- [ ] 5. Check missing values and duplicate records
- [ ] 6. Calculate basic statistics for home and away goals

### Level 2: Cleaning and calculated columns
- [ ] 7. Filter matches by year
- [ ] 8. Filter matches involving a chosen national team
- [ ] 9. Filter World Cup matches
- [ ] 10. Create `total_goals`
- [ ] 11. Create `goal_difference` from the home team's perspective
- [ ] 12. Create a match-outcome column with `np.select()` (home win, away win, draw)

### Level 3: Aggregation
- [ ] 13. Count matches played by each home team and away team separately
- [ ] 14. Calculate average total goals per match
- [ ] 15. Calculate home-win, away-win and draw percentages
- [ ] 16. Calculate goals scored and conceded by a chosen team (home and away)
- [ ] 17. Group by tournament: match count, average goals and draw percentage
- [ ] 18. Calculate annual match counts and average goals per match

### Level 4: Comparisons
- [ ] 19. Identify the highest-scoring matches
- [ ] 20. Find the 10 largest winning margins
- [ ] 21. Compare home advantage in neutral and non-neutral matches
- [ ] 22. Compare three teams by win rate, goals scored and conceded per match
- [ ] 23. Calculate median and standard deviation of total goals
- [ ] 24. Use percentiles to identify unusually high-scoring matches

### Level 5: Analytical challenges
- [ ] 25. Rank tournaments by average goals (minimum number of matches)
- [ ] 26. Compare the proportion of draws across tournament categories
- [ ] 27. Investigate changes in average goals per match over time
- [ ] 28. Compare a team's earlier and later recorded periods
- [ ] 29. Build a team summary DataFrame (matches, W/D/L, goals for and against, win rate)
- [ ] 30. Write five findings, explain the effect of data coverage and list three future questions

</details>

<details>
<summary><b>5. World Happiness 2019</b></summary>

### Level 1: Foundations
- [ ] 1. Load the CSV and inspect the first 10 rows
- [ ] 2. Find the dimensions and column names
- [ ] 3. Check data types and missing values
- [ ] 4. Check whether country names are unique
- [ ] 5. Generate descriptive statistics for all numeric columns
- [ ] 6. Sort countries by happiness score

### Level 2: Filtering and statistics
- [ ] 7. Find the 10 happiest countries
- [ ] 8. Find the 10 least happy countries
- [ ] 9. Calculate mean, median and standard deviation of happiness
- [ ] 10. Calculate the range and interquartile range of happiness
- [ ] 11. Calculate the 10th, 25th, 50th, 75th and 90th percentiles with NumPy
- [ ] 12. Find countries with above-average GDP but below-average happiness

### Level 3: Relationships and comparisons
- [ ] 13. Calculate correlations between happiness and each indicator
- [ ] 14. Rank indicators by correlation strength
- [ ] 15. Compare mean and median of GDP, social support and life expectancy
- [ ] 16. Compare average indicators of the top 10 and bottom 10 countries
- [ ] 17. Find countries with high happiness but below-average GDP
- [ ] 18. Calculate the difference between happiness rank and GDP rank

### Level 4: Outliers and bands
- [ ] 19. Identify potential outliers in happiness scores using IQR
- [ ] 20. Group countries as above or below average using `np.where()`
- [ ] 21. Create four happiness bands with `np.percentile()`
- [ ] 22. Calculate average indicator values within each band
- [ ] 23. Compare mean and median summaries where outliers may distort results
- [ ] 24. Investigate high social support with low happiness, and the reverse

### Level 5: Analytical challenges
- [ ] 25. Compare happiness rankings with GDP rankings and note major differences
- [ ] 26. Find countries that are happy despite low GDP
- [ ] 27. Identify the strongest positive and negative relationships
- [ ] 28. Build a country summary DataFrame (happiness, GDP, social support, life expectancy, freedom)
- [ ] 29. Write three evidence-based explanations, separating data from speculation
- [ ] 30. Produce a report with five findings, three limitations, three follow-up questions and a note on why correlation does not prove causation

</details>

---

## Tools

- Python 3
- Pandas
- NumPy

## Repository Structure

```
Data_Analysis_Projects/
├── README.md
├── requirements.txt
├── 01-spotify-tracks/
│   ├── spotify_analysis.py
│   ├── README.md
│   └── data/
├── 02-netflix-titles/
├── 03-formula-1/
├── 04-international-football/
└── 05-world-happiness/
```

## Standards

- Each task is a separate section in the script, with the task written as a comment above the code.
- Every finding is supported by a number.
- Cleaning decisions are documented with reasons.
- Each project ends with findings, limitations and follow-up questions in its own README.

## How to Run

```bash
git clone https://github.com/NerdBhattarai98/Data_Analysis_Projects.git
cd Data_Analysis_Projects
pip install -r requirements.txt
cd 01-spotify-tracks
python spotify_analysis.py
```

Datasets are not always included because of file size. Each project's README links to its Kaggle source. Download the CSV and place it in that project's `data/` folder.

## Author

**NerdBhattarai98**
GitHub: [NerdBhattarai98](https://github.com/NerdBhattarai98)
