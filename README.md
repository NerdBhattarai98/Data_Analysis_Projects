# Data Analysis Projects

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0)
![Progress](https://img.shields.io/badge/Progress-0%2F300%20tasks-orange)

A practical data analysis portfolio built with Python. Five real-world datasets are analyzed through 60 structured tasks each (300 in total), progressing from data inspection and cleaning to statistical analysis, visualization and evidence-based reporting.

## Portfolio Objectives

- Build job-ready skills for junior and associate Data Analyst roles.
- Clean and validate real datasets with documented, justified decisions.
- Use Pandas, NumPy, Matplotlib and Seaborn where each fits the question best.
- Produce findings supported by numbers, with clear limitations and no causal overstatement.

## Projects

| # | Project | Dataset focus | Main questions |
|---|---------|---------------|----------------|
| 1 | [Spotify Tracks](#project-1-spotify-tracks) | Popularity, genres, artists, audio features | What audio profile do popular tracks and genres share? How do explicit tracks compare? |
| 2 | [Netflix Titles](#project-2-netflix-titles) | Movies vs TV shows, release and addition dates, ratings, countries, genres | How has the catalogue changed? Does Netflix add recent or older titles? |
| 3 | [Formula 1](#project-3-formula-1) | Race results, grid and finishing positions, points, fastest laps | How much does grid position relate to the result? Who gains places consistently? |
| 4 | [International Football](#project-4-international-football) | Match results, home and away teams, tournaments, venues | How large is home advantage? How has scoring changed over time? |
| 5 | [World Happiness 2019](#project-5-world-happiness-2019) | Happiness scores and country-level indicators | Which indicators are most associated with happiness? Which countries differ from what GDP suggests? |

## Progress Overview

| Project | Total Tasks | Completed | Remaining | Status |
|---------|:-----------:|:---------:|:---------:|--------|
| Spotify Tracks | 60 | 0 | 60 | In progress |
| Netflix Titles | 60 | 0 | 60 | Not started |
| Formula 1 | 60 | 0 | 60 | Not started |
| International Football | 60 | 0 | 60 | Not started |
| World Happiness 2019 | 60 | 0 | 60 | Not started |
| **Total** | **300** | **0** | **300** | |

Each project uses the same six levels of ten tasks:

| Level | Focus | Tasks |
|-------|-------|:-----:|
| 1 | Data Fundamentals | 1–10 |
| 2 | Data Cleaning and Manipulation | 11–20 |
| 3 | Aggregation and Feature Engineering | 21–30 |
| 4 | Statistical and Analytical Methods | 31–40 |
| 5 | Data Visualization | 41–50 |
| 6 | Advanced Analysis and Portfolio Delivery | 51–60 |

The full task checklist for each project is below.

## Technologies and Tools

| Tool | Used for |
|------|----------|
| Python 3 | Analysis scripts |
| Pandas | Loading, cleaning, filtering, grouping, reshaping and summarizing data |
| NumPy | Vectorized logic, percentiles, outlier detection and numerical transformations |
| Matplotlib | Custom charts, multi-panel figures, annotations and layout control |
| Seaborn | Statistical charts such as distributions, box plots, heatmaps and pair plots |

## Repository Structure

```
Data_Analysis_Projects/
├── README.md
├── requirements.txt
├── 01-spotify-tracks/
├── 02-netflix-titles/
├── 03-formula-1/
├── 04-international-football/
└── 05-world-happiness/
```

Each project folder follows the same layout as it is built out:

```
NN-project-name/
├── README.md               # Project overview, task checklist, findings and limitations
├── <project>_analysis.py   # Analysis script
├── data/                   # Source CSV
├── figures/                # Generated charts
└── outputs/                # Exported summary tables
```

## Installation and Execution

```bash
git clone https://github.com/NerdBhattarai98/Data_Analysis_Projects.git
cd Data_Analysis_Projects
pip install -r requirements.txt

cd 01-spotify-tracks
python spotify_analysis.py
```

Datasets may not be included because of file size. Download the CSV listed in each project's README and place it in that project's `data/` folder. Replacing a CSV with an updated version of the same dataset and rerunning the script recalculates all results.

## Project Standards

- Results are calculated from the current dataset; nothing is hardcoded.
- Cleaning decisions (missing values, duplicates, invalid values) are documented with reasons.
- Rates use appropriate denominators, and division by zero is handled.
- Rankings apply minimum sample sizes so small groups do not dominate.
- Correlation is never presented as causation.
- Charts and summary tables are saved to each project's `figures/` and `outputs/` folders with meaningful filenames.
- Missing files or required columns produce clear validation messages.

## Skills Demonstrated

- Data inspection, validation and cleaning
- Filtering, grouping, aggregation, reshaping and ranking with Pandas
- Statistical summaries, percentiles, outlier detection and correlation with NumPy and Pandas
- Purposeful visualization with Matplotlib and Seaborn
- Feature engineering and multi-step analytical investigations
- Clear, evidence-based reporting with stated limitations

---

## Project 1: Spotify Tracks

### Overview
This project explores a dataset of Spotify tracks to understand what is associated with track popularity, how audio features differ across genres, and how explicit content, duration, tempo and musical mode relate to listener engagement. The work progresses from basic inspection to multi-step investigations and a final evidence-based report.

**Status:** 30 / 60 tasks completed

### Tasks
> Tasks 1–30 were completed under the earlier five-level checklist and are kept here in their original order.

#### Level 1 — Data Fundamentals (Tasks 1–10)

- [] **Task 01 — Preview the Dataset**
  - **Objective:** Get a first look at the structure and content of the data.
  - **Requirements:** Load the CSV into a DataFrame; display the first 10 rows.
  - **Skills:** `pd.read_csv()`, `head()`
  - **Expected output:** A 10-row preview.

- [] **Task 02 — Inspect the End and a Random Sample**
  - **Objective:** Check whether the data looks consistent beyond the first rows.
  - **Requirements:** Display the last 5 rows; display 5 random rows using a fixed random seed.
  - **Skills:** `tail()`, `sample()`
  - **Expected output:** Two small previews.

- [] **Task 03 — Measure Dataset Size**
  - **Objective:** Know how many records and variables you are working with.
  - **Requirements:** Report the number of rows and columns.
  - **Skills:** `shape`
  - **Expected output:** Row and column counts.

- [] **Task 04 — Check Data Types and Completeness**
  - **Objective:** Confirm each column has a sensible type and see where values are missing.
  - **Requirements:** Review column names, data types and non-null counts.
  - **Skills:** `info()`, `dtypes`
  - **Expected output:** A short note on any unexpected types.

- [] **Task 05 — Select Core Columns**
  - **Objective:** Create a focused view of the most relevant fields.
  - **Requirements:** Select `track_name`, `artists`, `popularity`, `energy` and `danceability`.
  - **Skills:** Column selection
  - **Expected output:** A five-column DataFrame.

- [] **Task 06 — Count Unique Entities**
  - **Objective:** Understand how many distinct artists, genres and tracks exist.
  - **Requirements:** Count unique values in `artists`, `track_genre` and `track_id`; compare unique `track_id` with total rows.
  - **Skills:** `nunique()`
  - **Expected output:** Three counts and a note on repeated IDs.

- [] **Task 07 — Rank Columns by Missing Values**
  - **Objective:** Find where data is incomplete.
  - **Requirements:** Count missing values per column; sort from most to least missing.
  - **Skills:** `isna()`, `sum()`, `sort_values()`
  - **Expected output:** A ranked missing-value table.

- [] **Task 08 — Investigate Duplicates**
  - **Objective:** Distinguish fully duplicated rows from repeated track IDs.
  - **Requirements:** Count fully duplicated rows; separately count `track_id` values that appear more than once; inspect examples of each.
  - **Skills:** `duplicated()`, `value_counts()`
  - **Expected output:** Two counts and an explanation of the difference.

- [] **Task 09 — Calculate Missing-Value Percentages**
  - **Objective:** Express missing data relative to dataset size.
  - **Requirements:** Calculate the percentage of missing values per column using NumPy; round sensibly.
  - **Skills:** NumPy arithmetic, `round()`
  - **Expected output:** A percentage table.

- [] **Task 10 — Filter Popular Tracks**
  - **Objective:** Isolate highly popular tracks.
  - **Requirements:** Filter tracks with `popularity` greater than 70; report how many qualify and their share of all tracks.
  - **Skills:** Boolean filtering
  - **Expected output:** A filtered DataFrame and its share.

#### Level 2 — Data Cleaning and Manipulation (Tasks 11–20)

- [] **Task 11 — Filter Energetic, Danceable Tracks**
  - **Objective:** Combine conditions to find a specific track profile.
  - **Requirements:** Filter tracks with `energy` above 0.7 and `danceability` above 0.6.
  - **Skills:** Multiple Boolean conditions
  - **Expected output:** A filtered DataFrame and its count.

- [] **Task 12 — Sort by Several Columns**
  - **Objective:** Practise ordering data in different ways.
  - **Requirements:** Sort by `popularity`, `duration_ms` and `energy` using different ascending/descending combinations.
  - **Skills:** `sort_values()` with multiple keys
  - **Expected output:** Sorted previews.

- [] **Task 13 — Find the 20 Most Popular Tracks**
  - **Objective:** Identify the top tracks.
  - **Requirements:** Return the 20 highest-popularity tracks with name, artist and genre.
  - **Skills:** `nlargest()` or sorting
  - **Expected output:** A 20-row table.

- [] **Task 14 — Count Tracks by Genre**
  - **Objective:** See how tracks are distributed across genres.
  - **Requirements:** Count tracks per genre; identify the most common genres.
  - **Skills:** `value_counts()`
  - **Expected output:** A genre count table.

- [] **Task 15 — Summarize Popularity**
  - **Objective:** Describe the centre and spread of popularity.
  - **Requirements:** Calculate the mean, median and standard deviation of `popularity`.
  - **Skills:** Pandas and NumPy statistics
  - **Expected output:** Three statistics.

- [] **Task 16 — Find the Most Prolific Artists**
  - **Objective:** Identify artists with the most tracks.
  - **Requirements:** List the 10 artists with the most tracks.
  - **Skills:** `value_counts()`
  - **Expected output:** A top-10 table.

- [] **Task 17 — Convert Duration to Minutes**
  - **Objective:** Make track length easier to interpret.
  - **Requirements:** Create a duration-in-minutes column from `duration_ms`.
  - **Skills:** Vectorized arithmetic
  - **Expected output:** A new column.

- [] **Task 18 — Create Popularity Categories**
  - **Objective:** Group tracks into low, medium and high popularity.
  - **Requirements:** Define and document the thresholds; create the category column.
  - **Skills:** `pd.cut()`
  - **Expected output:** A category column and its counts.

- [] **Task 19 — Calculate Popularity Percentiles**
  - **Objective:** Describe the popularity distribution with percentiles.
  - **Requirements:** Calculate the 25th, 50th and 75th percentiles with NumPy.
  - **Skills:** `np.percentile()`
  - **Expected output:** Three percentile values.

- [] **Task 20 — Classify Energy Levels**
  - **Objective:** Label tracks as high- or low-energy.
  - **Requirements:** Create the label with `np.where()` using a documented threshold.
  - **Skills:** `np.where()`
  - **Expected output:** A new column and its counts.

#### Level 3 — Aggregation and Feature Engineering (Tasks 21–30)

- [] **Task 21 — Correlate Popularity with Energy and Danceability**
  - **Objective:** Measure how these features move with popularity.
  - **Requirements:** Calculate both correlations.
  - **Skills:** `corr()`
  - **Expected output:** Two correlation values with a short interpretation.

- [] **Task 22 — Compare Explicit and Non-Explicit Tracks**
  - **Objective:** See whether explicit tracks differ in popularity.
  - **Requirements:** Compare average popularity by `explicit`; include group sizes.
  - **Skills:** `groupby()`
  - **Expected output:** A two-row comparison.

- [] **Task 23 — Detect Unusually Long Tracks**
  - **Objective:** Identify duration outliers.
  - **Requirements:** Apply the IQR rule to duration; count and inspect flagged tracks.
  - **Skills:** `np.percentile()`, IQR method
  - **Expected output:** Thresholds and a list of long tracks.

- [] **Task 24 — Find Above-Median Genres**
  - **Objective:** Identify genres with higher typical popularity.
  - **Requirements:** Compare each genre's median popularity with the overall median; apply a minimum track count.
  - **Skills:** `groupby()`, filtering
  - **Expected output:** A filtered genre list.

- [] **Task 25 — Compare Top and Bottom 10%**
  - **Objective:** See how the most and least popular tracks differ.
  - **Requirements:** Split by popularity percentiles; compare average audio features.
  - **Skills:** Percentiles, `groupby()`
  - **Expected output:** A comparison table.

- [] **Task 26 — Rank Artists by Median Popularity**
  - **Objective:** Rank artists fairly.
  - **Requirements:** Keep artists with at least 10 tracks; rank by median popularity.
  - **Skills:** `groupby()`, `agg()`, filtering
  - **Expected output:** A ranked artist table.

- [] **Task 27 — Find Popular, Energetic, Danceable Tracks**
  - **Objective:** Combine three conditions into one profile.
  - **Requirements:** Define and document the thresholds; filter the matching tracks.
  - **Skills:** Combined Boolean filtering
  - **Expected output:** A filtered table and its share.

- [] **Task 28 — Compare Mean and Median Genre Rankings**
  - **Objective:** Check whether the choice of statistic changes the ranking.
  - **Requirements:** Rank genres by mean and by median popularity; compare the two rankings.
  - **Skills:** `agg()`, `rank()`
  - **Expected output:** A side-by-side ranking.

- [] **Task 29 — Build a Genre Summary**
  - **Objective:** Create one reusable genre-level table.
  - **Requirements:** Include track count, median popularity, average energy and average danceability.
  - **Skills:** `groupby().agg()`
  - **Expected output:** A genre summary DataFrame.

- [] **Task 30 — Write First Findings**
  - **Objective:** Summarize what the analysis shows so far.
  - **Requirements:** Write five findings, two limitations and three future questions.
  - **Skills:** Analytical writing
  - **Expected output:** A short written summary.

#### Level 4 — Statistical and Analytical Methods (Tasks 31–40)

- [ ] **Task 31 — Build a Full Audio-Feature Correlation Table**
  - **Objective:** Find the strongest relationships among all audio features, not just with popularity.
  - **Requirements:** Calculate the correlation matrix for `popularity` and the numeric audio features; remove the diagonal and duplicate pairs; list the three strongest positive and three strongest negative pairs.
  - **Skills:** `corr()`, NumPy masking, `stack()`
  - **Expected output:** A ranked table of feature pairs with correlation values.

- [ ] **Task 32 — Compare Pearson and Spearman Correlations**
  - **Objective:** Check whether relationships with popularity are linear or only rank-based.
  - **Requirements:** Calculate Pearson and Spearman correlations between `popularity` and each audio feature; place them side by side; note features where the two methods disagree in strength or direction.
  - **Skills:** `corr(method=...)`, DataFrame construction
  - **Expected output:** A comparison table and two to three sentences of interpretation.

- [ ] **Task 33 — Measure Distribution Shape**
  - **Objective:** Identify which features are heavily skewed.
  - **Requirements:** Calculate skewness for each numeric audio feature; compare mean and median for the three most skewed features.
  - **Skills:** `skew()`, `np.mean()`, `np.median()`
  - **Expected output:** A skewness table and a note on which summary statistic suits each skewed feature.

- [ ] **Task 34 — Apply a Justified Log Transformation**
  - **Objective:** Reduce skew in a strongly right-skewed feature.
  - **Requirements:** Choose one non-negative skewed feature; apply `np.log1p()`; compare skewness before and after; explain why `log1p` is used instead of `log`.
  - **Skills:** `np.log1p()`, `skew()`
  - **Expected output:** Before-and-after skewness values and a short justification.

- [ ] **Task 35 — Detect Outliers with Z-Scores**
  - **Objective:** Compare z-score and IQR outlier detection.
  - **Requirements:** Calculate z-scores for `tempo` and `loudness` (state whether you use sample or population standard deviation); flag values beyond ±3; compare the counts with the IQR method.
  - **Skills:** `np.mean()`, `np.std()`, vectorized arithmetic
  - **Expected output:** A table of outlier counts by method and feature.

- [ ] **Task 36 — Compare Major and Minor Tracks**
  - **Objective:** See whether musical mode is associated with popularity or mood.
  - **Requirements:** Group by `mode`; compare count, median popularity, mean valence and mean energy; label the groups clearly as major or minor.
  - **Skills:** `groupby().agg()`, `map()`
  - **Expected output:** A two-row comparison with a cautious interpretation.

- [ ] **Task 37 — Profile Musical Keys**
  - **Objective:** Check how tracks are distributed across keys.
  - **Requirements:** Inspect the `key` values for undetected-key codes and decide how to treat them; count tracks per key; calculate median popularity per key.
  - **Skills:** `value_counts()`, `groupby()`
  - **Expected output:** A key summary table with counts and median popularity.

- [ ] **Task 38 — Measure Genre Consistency**
  - **Objective:** Find genres whose popularity is consistent and those driven by a few hits.
  - **Requirements:** For genres above a minimum track count, calculate the standard deviation and coefficient of variation of popularity; handle a zero mean safely; list the five most and least consistent genres.
  - **Skills:** `groupby().agg()`, `np.where()`
  - **Expected output:** Two ranked lists of genres.

- [ ] **Task 39 — Bootstrap the Explicit Popularity Gap**
  - **Objective:** Estimate how uncertain the explicit vs non-explicit difference is.
  - **Requirements:** Use a seeded NumPy random generator to resample each group (for example, 1,000 times); calculate the difference in median popularity each time; report a 95% percentile interval.
  - **Skills:** `np.random.default_rng()`, `np.percentile()`, loops or vectorized resampling
  - **Expected output:** A point estimate, an interval and an interpretation that avoids causal language.

- [ ] **Task 40 — Measure the Impact of Repeated Track IDs**
  - **Objective:** Decide how repeated `track_id` values should be treated.
  - **Requirements:** Create a version with one row per `track_id`; compare mean popularity, explicit share and track counts between the two versions; document which version later tasks use and why.
  - **Skills:** `drop_duplicates(subset=...)`, comparison tables
  - **Expected output:** A before-and-after comparison and a written decision.

#### Level 5 — Data Visualization (Tasks 41–50)

> Every chart needs a clear title, labeled axes with units, and must be saved to `figures/` with `dpi=150` and `bbox_inches="tight"`.

- [ ] **Task 41 — Plot the Popularity Distribution**
  - **Objective:** Show the overall shape of popularity.
  - **Requirements:** Create a histogram; add vertical lines for the mean and median; check for an unusual spike at zero and mention it in the title or a note.
  - **Skills:** `plt.subplots()`, `ax.hist()`, `axvline()`, legend
  - **Expected output:** A saved histogram.

- [ ] **Task 42 — Create Audio-Feature Small Multiples**
  - **Objective:** Compare the distributions of six 0–1 features at once.
  - **Requirements:** Build a 2×3 grid for danceability, energy, valence, acousticness, speechiness and liveness; use shared x-axis limits.
  - **Skills:** `plt.subplots(nrows, ncols)`, `sns.histplot()`, `tight_layout()`
  - **Expected output:** A saved multi-panel figure.

- [ ] **Task 43 — Rank Genres Visually**
  - **Objective:** Show which genres have the highest median popularity.
  - **Requirements:** Plot the top 15 genres (minimum track count applied) as a sorted horizontal bar chart; annotate each bar with its track count.
  - **Skills:** `ax.barh()`, `ax.annotate()` or `bar_label()`
  - **Expected output:** A saved horizontal bar chart.

- [ ] **Task 44 — Compare Explicit and Non-Explicit Popularity**
  - **Objective:** Show the full popularity distribution for both groups.
  - **Requirements:** Draw a box plot of popularity by `explicit`; include group sizes in the axis labels.
  - **Skills:** `sns.boxplot()`
  - **Expected output:** A saved box plot.

- [ ] **Task 45 — Visualize Energy and Loudness**
  - **Objective:** Show the relationship between two strongly related features.
  - **Requirements:** Plot a sample of tracks with a fixed seed; add a regression line; annotate the correlation coefficient.
  - **Skills:** `sns.regplot()`, `ax.text()`
  - **Expected output:** A saved scatter plot with a fitted line.

- [ ] **Task 46 — Draw a Correlation Heatmap**
  - **Objective:** Summarize all feature relationships in one chart.
  - **Requirements:** Mask the upper triangle; use a diverging palette centred at zero; show values to two decimals.
  - **Skills:** `sns.heatmap()`, `np.triu()`
  - **Expected output:** A saved heatmap.

- [ ] **Task 47 — Compare Tempo by Popularity Category**
  - **Objective:** See whether tempo differs between popularity groups.
  - **Requirements:** Treat tempo values of zero as invalid if they exist and document how many there are; plot tempo by popularity category in a logical category order.
  - **Skills:** `sns.boxplot()` or `sns.violinplot()`, category ordering
  - **Expected output:** A saved categorical chart.

- [ ] **Task 48 — Show Duration with Outlier Thresholds**
  - **Objective:** Visualize where unusually long tracks begin.
  - **Requirements:** Plot the duration distribution in minutes; mark the IQR thresholds from Task 23; note if the x-axis is limited for readability.
  - **Skills:** `sns.histplot()`, `axvline()`, axis limits
  - **Expected output:** A saved histogram with threshold lines.

- [ ] **Task 49 — Compare Top and Bottom 10% Visually**
  - **Objective:** Turn the Task 25 comparison into a chart.
  - **Requirements:** Use only features on the 0–1 scale; draw grouped bars for the top and bottom 10%.
  - **Skills:** `ax.bar()` with offsets, NumPy `arange()`, legend
  - **Expected output:** A saved grouped bar chart.

- [ ] **Task 50 — Build a Pair Plot on a Sample**
  - **Objective:** Explore several feature relationships at once.
  - **Requirements:** Use a seeded sample (for example, 2,000 tracks); include four audio features; colour by popularity category.
  - **Skills:** `sns.pairplot()`, `sample()`
  - **Expected output:** A saved pair plot.

#### Level 6 — Advanced Analysis and Portfolio Delivery (Tasks 51–60)

- [ ] **Task 51 — Investigate High-Popularity Genres**
  - **Objective:** Find out what audio profile the most popular genres share.
  - **Requirements:** Split genres into top and bottom quartiles by median popularity (minimum track count applied); compare their median audio features; write two to three sentences of conclusion.
  - **Skills:** `groupby()`, `pd.qcut()`, comparison tables
  - **Expected output:** A comparison table and a short conclusion.

- [ ] **Task 52 — Analyze Individual Artists**
  - **Objective:** Count each artist separately on collaborative tracks.
  - **Requirements:** Split `artists` into a list using its actual separator; give each artist their own row; rank artists by median popularity with a minimum track count; compare the result with Task 26.
  - **Skills:** `str.split()`, `explode()`, `groupby()`
  - **Expected output:** A ranked artist table and a note on what changed.

- [ ] **Task 53 — Analyze Albums**
  - **Objective:** Find the strongest albums by typical popularity.
  - **Requirements:** Group by artist and album name together (album names are not unique); apply a minimum track count; rank by median popularity.
  - **Skills:** Multi-column `groupby()`, `agg()`
  - **Expected output:** A ranked album table.

- [ ] **Task 54 — Find the Track-Length Sweet Spot**
  - **Objective:** See how popularity varies across duration ranges.
  - **Requirements:** Bin duration into documented ranges; report count and median popularity per bin; explain how genre could confound the pattern.
  - **Skills:** `pd.cut()`, `groupby()`
  - **Expected output:** A binned summary table and a caveat.

- [ ] **Task 55 — Find Tracks That Outperform Their Genre**
  - **Objective:** Compare each track with its own genre rather than the whole dataset.
  - **Requirements:** Calculate each track's popularity minus its genre median; rank tracks within their genre; list the 10 tracks with the largest positive gap.
  - **Skills:** `groupby().transform()`, `rank()`
  - **Expected output:** A table of genre-relative top performers.

- [ ] **Task 56 — Pivot Genre and Explicit Content**
  - **Objective:** Check whether the explicit gap is consistent across genres.
  - **Requirements:** Build a pivot table of median popularity by genre (top 15 by count) and `explicit`; add a count table; flag genres where the gap reverses direction or a cell has too few tracks.
  - **Skills:** `pivot_table()`, `crosstab()`
  - **Expected output:** A pivot table with flagged genres.

- [ ] **Task 57 — Write a Data Validation Function**
  - **Objective:** Make the analysis safe to rerun on updated data.
  - **Requirements:** Check required columns, value ranges (0–1 features, popularity 0–100, positive duration and tempo) and duplicates; print a clear report; stop with a helpful message if a required column is missing.
  - **Skills:** Functions, Boolean checks, error messages
  - **Expected output:** A reusable validation function and its report.

- [ ] **Task 58 — Export Key Results**
  - **Objective:** Save reusable outputs separately from the raw data.
  - **Requirements:** Export the genre summary, artist ranking and duplicate report to `outputs/` with meaningful filenames; reload one file to confirm it saved correctly.
  - **Skills:** `to_csv()`, file paths
  - **Expected output:** CSV files in `outputs/`.

- [ ] **Task 59 — Write the Findings Report**
  - **Objective:** Communicate the most important results.
  - **Requirements:** Write five findings, each with its numbers, sample size and a caveat; add three limitations and three follow-up questions; avoid causal language.
  - **Skills:** Analytical writing
  - **Expected output:** A findings section in Markdown.

- [ ] **Task 60 — Finalize the Project README**
  - **Objective:** Present the project as a portfolio piece.
  - **Requirements:** Embed the key charts with relative paths; summarize methodology and cleaning decisions; include findings, limitations and instructions to run the analysis.
  - **Skills:** Markdown, documentation
  - **Expected output:** A complete project README.

### Progress Tracker
| Level | Tasks | Completed | Remaining |
|-------|:-----:|:---------:|:---------:|
| 1. Data Fundamentals | 1–10 | 10 | 0 |
| 2. Data Cleaning and Manipulation | 11–20 | 10 | 0 |
| 3. Aggregation and Feature Engineering | 21–30 | 10 | 0 |
| 4. Statistical and Analytical Methods | 31–40 | 0 | 10 |
| 5. Data Visualization | 41–50 | 0 | 10 |
| 6. Advanced Analysis and Portfolio Delivery | 51–60 | 0 | 10 |
| **Total** | **60** | **30** | **30** |

---

## Project 2: Netflix Titles

### Overview
This project analyzes the Netflix catalogue to understand the balance between movies and TV shows, how the catalogue grew over time, how release dates compare with addition dates, and how content differs by rating, country and genre. Much of the work involves cleaning text fields that hold several values or mixed units.

**Status:** 0 / 60 tasks completed

### Tasks
#### Level 1 — Data Fundamentals (Tasks 1–10)

- [ ] **Task 01 — Preview the Dataset**
  - **Objective:** Get a first look at the catalogue.
  - **Requirements:** Load the CSV; display the first 10 and last 5 rows.
  - **Skills:** `pd.read_csv()`, `head()`, `tail()`
  - **Expected output:** Two previews.

- [ ] **Task 02 — Confirm the Schema**
  - **Objective:** Make sure the file matches the expected 12 columns.
  - **Requirements:** Report rows and columns; compare the column names with the documented schema; list any differences.
  - **Skills:** `shape`, `columns`, set comparison
  - **Expected output:** Dimensions and a schema check result.

- [ ] **Task 03 — Identify Columns That Need Parsing**
  - **Objective:** Find columns whose stored type does not match their meaning.
  - **Requirements:** Review data types; identify which text columns actually represent dates or numbers.
  - **Skills:** `info()`, `dtypes`
  - **Expected output:** A short list of columns that need conversion, with reasons.

- [ ] **Task 04 — Count Unique Values**
  - **Objective:** Understand the variety in the catalogue.
  - **Requirements:** Count unique values in `show_id`, `title`, `type`, `rating` and `director`; compare unique `show_id` with total rows.
  - **Skills:** `nunique()`
  - **Expected output:** A table of unique counts.

- [ ] **Task 05 — Compare Movies and TV Shows**
  - **Objective:** Measure the content-type split.
  - **Requirements:** Count titles by `type`; express each as a percentage of all titles.
  - **Skills:** `value_counts(normalize=True)`
  - **Expected output:** Counts and percentages.

- [ ] **Task 06 — Explore Release Years**
  - **Objective:** Understand the time span of the catalogue.
  - **Requirements:** Find the earliest and latest release years; count titles released before 1980.
  - **Skills:** `min()`, `max()`, Boolean filtering
  - **Expected output:** Year range and a count.

- [ ] **Task 07 — Rank Columns by Missing Values**
  - **Objective:** Find where information is incomplete.
  - **Requirements:** Count and calculate the percentage of missing values per column; sort from most to least missing.
  - **Skills:** `isna()`, `sum()`, `sort_values()`
  - **Expected output:** A ranked missing-value table.

- [ ] **Task 08 — Check for Duplicates**
  - **Objective:** Make sure each title is recorded once.
  - **Requirements:** Count fully duplicated rows; check `show_id` uniqueness; check for repeated combinations of `title`, `type` and `release_year`, and inspect any you find.
  - **Skills:** `duplicated(subset=...)`
  - **Expected output:** Three duplicate counts and a short note.

- [ ] **Task 09 — Inspect Rating Values**
  - **Objective:** Check that the rating column contains only valid ratings.
  - **Requirements:** List all unique ratings with counts; identify any values that appear to belong in a different column.
  - **Skills:** `value_counts()`, `unique()`
  - **Expected output:** A rating frequency table and a list of suspicious values.

- [ ] **Task 10 — Apply Basic Filters**
  - **Objective:** Practise selecting subsets.
  - **Requirements:** Filter titles released in a year of your choice; filter TV shows with a rating of your choice; report both counts.
  - **Skills:** Boolean filtering, `.loc[]`
  - **Expected output:** Two filtered DataFrames and their counts.

#### Level 2 — Data Cleaning and Manipulation (Tasks 11–20)

- [ ] **Task 11 — Clean Text Whitespace**
  - **Objective:** Remove formatting problems before parsing.
  - **Requirements:** Strip leading and trailing whitespace from text columns; check whether any values changed and how many.
  - **Skills:** `str.strip()`, comparison
  - **Expected output:** A cleaned DataFrame and a count of changed values.

- [ ] **Task 12 — Parse the Date Added**
  - **Objective:** Convert `date_added` into a real date column.
  - **Requirements:** Inspect the text format first; convert with invalid values set to missing; count and inspect values that failed to parse.
  - **Skills:** `pd.to_datetime(errors="coerce")`
  - **Expected output:** A datetime column and a list of failed conversions.

- [ ] **Task 13 — Extract Date Parts**
  - **Objective:** Create features for time-based analysis.
  - **Requirements:** Extract the year, month number, month name and weekday from the parsed date.
  - **Skills:** `.dt` accessor
  - **Expected output:** Four new columns.

- [ ] **Task 14 — Parse Duration into Number and Unit**
  - **Objective:** Make duration usable without mixing minutes and seasons.
  - **Requirements:** Split `duration` into a numeric value and a unit; create separate columns for movie minutes and TV seasons; check for rows where the unit does not match the content type.
  - **Skills:** `str.extract()`, `pd.to_numeric()`, `np.where()`
  - **Expected output:** Two numeric columns and a mismatch count.

- [ ] **Task 15 — Fix Misplaced Values**
  - **Objective:** Resolve values stored in the wrong column.
  - **Requirements:** Find rows where `rating` contains duration-like text and `duration` is missing; decide how to treat them; document the decision and the number of rows affected.
  - **Skills:** `str.contains()`, `.loc[]` assignment
  - **Expected output:** Corrected rows and a written decision.

- [ ] **Task 16 — Decide How to Handle Missing Values**
  - **Objective:** Treat missing director, cast and country values deliberately.
  - **Requirements:** Compare two approaches (keeping them missing vs labelling them "Unknown"); show how each changes a top-10 count; choose one and document why.
  - **Skills:** `fillna()`, `value_counts(dropna=...)`
  - **Expected output:** A comparison and a documented decision.

- [ ] **Task 17 — Extract the Primary Country**
  - **Objective:** Create a single-country field for simple grouping.
  - **Requirements:** Take the first listed country into a new column; count how many titles list more than one country.
  - **Skills:** `str.split()`, `str[0]`, `str.count()`
  - **Expected output:** A primary-country column and a multi-country count.

- [ ] **Task 18 — Expand Multi-Country Entries**
  - **Objective:** Count every country a title is associated with.
  - **Requirements:** Split `country` into lists; give each country its own row; strip whitespace; compare row counts before and after.
  - **Skills:** `str.split()`, `explode()`, `str.strip()`
  - **Expected output:** A long country table and row-count comparison.

- [ ] **Task 19 — Expand Genre Labels**
  - **Objective:** Count each genre a title belongs to.
  - **Requirements:** Split `listed_in` into one row per genre; strip whitespace; count unique genres.
  - **Skills:** `str.split()`, `explode()`
  - **Expected output:** A long genre table and a unique-genre count.

- [ ] **Task 20 — Search Titles and Descriptions**
  - **Objective:** Find titles related to a chosen topic.
  - **Requirements:** Choose a keyword; search `title` and `description` case-insensitively; count matches by content type.
  - **Skills:** `str.contains(case=False)`, `groupby()`
  - **Expected output:** A matching subset and counts by type.

#### Level 3 — Aggregation and Feature Engineering (Tasks 21–30)

- [ ] **Task 21 — Count Titles by Release Year and Type**
  - **Objective:** See how release years differ between movies and TV shows.
  - **Requirements:** Count titles per release year and type; show the 15 most recent years.
  - **Skills:** `crosstab()` or `groupby().size().unstack()`
  - **Expected output:** A year-by-type table.

- [ ] **Task 22 — Count Titles Added per Year**
  - **Objective:** Measure catalogue growth on Netflix.
  - **Requirements:** Count titles added per year by type; note whether the final year in the data is complete.
  - **Skills:** `groupby()`, `unstack()`
  - **Expected output:** An additions-by-year table.

- [ ] **Task 23 — Calculate the Release-to-Addition Gap**
  - **Objective:** Measure how old titles are when they arrive on Netflix.
  - **Requirements:** Subtract `release_year` from the year added; describe the result; count and inspect negative gaps.
  - **Skills:** Vectorized arithmetic, `describe()`
  - **Expected output:** A gap column, its summary and a list of negative values.

- [ ] **Task 24 — Create a Release Decade**
  - **Objective:** Group release years into decades.
  - **Requirements:** Create a decade column; count titles and calculate catalogue share per decade.
  - **Skills:** Integer division, `value_counts(normalize=True)`
  - **Expected output:** A decade share table.

- [ ] **Task 25 — Classify Release Periods**
  - **Objective:** Create readable era labels.
  - **Requirements:** Define and document period boundaries; assign labels with `np.select()`; count titles per period and type.
  - **Skills:** `np.select()`, `crosstab()`
  - **Expected output:** A period column and a period-by-type table.

- [ ] **Task 26 — Group Ratings by Audience**
  - **Objective:** Simplify ratings into audience groups.
  - **Requirements:** Write and document a mapping from each rating to an audience group (for example, kids, teens, adults); put unmapped ratings in an explicit "Other/Unknown" group; count titles per group and type.
  - **Skills:** Dictionaries, `map()`, `fillna()`
  - **Expected output:** An audience-group column and its counts.

- [ ] **Task 27 — Rank Countries by Titles**
  - **Objective:** Find the countries most represented in the catalogue.
  - **Requirements:** Using the expanded country table, list the top 10 countries; calculate the movie share for each.
  - **Skills:** `groupby()`, `agg()`
  - **Expected output:** A top-10 country table with movie share.

- [ ] **Task 28 — Rank Genres by Content Type**
  - **Objective:** Compare genre labels for movies and TV shows.
  - **Requirements:** Using the expanded genre table, list the top 10 genres separately for movies and TV shows.
  - **Skills:** Filtering, `value_counts()`
  - **Expected output:** Two top-10 genre tables.

- [ ] **Task 29 — Analyze Directors**
  - **Objective:** Identify the most frequently listed directors.
  - **Requirements:** Split multi-director entries into individual names; list the top 10 directors; show how many of their titles are movies vs TV shows.
  - **Skills:** `str.split()`, `explode()`, `crosstab()`
  - **Expected output:** A director table with type counts.

- [ ] **Task 30 — Analyze Cast Frequency**
  - **Objective:** Identify the most frequently listed cast members.
  - **Requirements:** Expand `cast` into one row per actor; list the top 15; report the share of titles with no cast listed.
  - **Skills:** `explode()`, `value_counts()`
  - **Expected output:** A top-15 cast table and a missing-cast share.

#### Level 4 — Statistical and Analytical Methods (Tasks 31–40)

- [ ] **Task 31 — Summarize Movie Duration**
  - **Objective:** Describe typical movie length.
  - **Requirements:** Using movies only, calculate the mean, median, standard deviation, minimum, maximum and 10th/90th percentiles of minutes.
  - **Skills:** `np.mean()`, `np.median()`, `np.std()`, `np.percentile()`
  - **Expected output:** A summary statistics table.

- [ ] **Task 32 — Detect Movie Duration Outliers**
  - **Objective:** Find unusually short and long movies.
  - **Requirements:** Apply the IQR rule; list the shortest and longest flagged titles; consider whether they are genuine (for example, short films or specials).
  - **Skills:** `np.percentile()`, IQR method, filtering
  - **Expected output:** Thresholds, flagged titles and a short assessment.

- [ ] **Task 33 — Analyze TV Show Seasons**
  - **Objective:** Describe how long TV shows run.
  - **Requirements:** Calculate the share of shows with one, two and three or more seasons; report the median number of seasons.
  - **Skills:** `pd.cut()` or `np.select()`, `value_counts(normalize=True)`
  - **Expected output:** A season distribution table.

- [ ] **Task 34 — Compare Movie Duration by Decade**
  - **Objective:** Check whether movie length changes across release decades.
  - **Requirements:** Calculate count, mean and median minutes per decade; flag decades with too few movies for a reliable comparison.
  - **Skills:** `groupby().agg()`
  - **Expected output:** A decade duration table with flagged rows.

- [ ] **Task 35 — Analyze the Addition Gap by Type**
  - **Objective:** Compare how quickly movies and TV shows arrive on Netflix.
  - **Requirements:** Calculate the 25th, 50th, 75th and 90th percentiles of the gap by type; calculate the share of titles added within one year of release.
  - **Skills:** `groupby().quantile()`, `np.where()`
  - **Expected output:** A percentile table and two shares.

- [ ] **Task 36 — Find Ratings That Lean Toward One Type**
  - **Objective:** Identify ratings that are disproportionately movies or TV shows.
  - **Requirements:** Build a normalized rating-by-type crosstab; compare each rating's movie share with the overall movie share; apply a minimum count.
  - **Skills:** `crosstab(normalize=...)`, division
  - **Expected output:** A table of ratings with their deviation from the overall share.

- [ ] **Task 37 — Look for Seasonal Patterns in Additions**
  - **Objective:** Check whether titles are added more in certain months.
  - **Requirements:** Count additions per calendar month across all years; convert to shares; note which years are only partly covered.
  - **Skills:** `groupby()`, normalization
  - **Expected output:** A monthly share table.

- [ ] **Task 38 — Measure Country Concentration Correctly**
  - **Objective:** Calculate what share of titles involve the top five countries.
  - **Requirements:** Use the number of unique titles as the denominator, not the number of expanded rows; explain why the two denominators give different answers.
  - **Skills:** `nunique()`, filtering on exploded data
  - **Expected output:** A correct share and a short explanation.

- [ ] **Task 39 — Find Common Genre Pairs**
  - **Objective:** See which genres are most often listed together.
  - **Requirements:** Join the expanded genre table to itself on `show_id`; remove self-pairs and reversed duplicates; list the 10 most common pairs.
  - **Skills:** `merge()`, filtering, `value_counts()`
  - **Expected output:** A top-10 genre pair table.

- [ ] **Task 40 — Check Whether Missing Data Is Random**
  - **Objective:** Test whether missing directors are concentrated in certain kinds of titles.
  - **Requirements:** Compare content type, release decade and rating group for titles with and without a director; describe any differences.
  - **Skills:** `isna()`, `crosstab(normalize=...)`
  - **Expected output:** A comparison table and a note on possible bias.

#### Level 5 — Data Visualization (Tasks 41–50)

> Every chart needs a clear title, labeled axes with units, and must be saved to `figures/` with `dpi=150` and `bbox_inches="tight"`.

- [ ] **Task 41 — Plot the Movie and TV Show Split**
  - **Objective:** Show the content-type balance.
  - **Requirements:** Draw a count chart; annotate each bar with its percentage.
  - **Skills:** `sns.countplot()`, `bar_label()`
  - **Expected output:** A saved bar chart.

- [ ] **Task 42 — Plot Additions Over Time**
  - **Objective:** Show catalogue growth by type.
  - **Requirements:** Draw a line chart of titles added per year for each type; mark or exclude an incomplete final year.
  - **Skills:** `sns.lineplot()`, axis formatting
  - **Expected output:** A saved line chart.

- [ ] **Task 43 — Compare Release and Addition Years**
  - **Objective:** Show the difference between when titles were made and when they were added.
  - **Requirements:** Overlay the two year distributions on the same axis with transparency or step outlines.
  - **Skills:** `ax.hist()` with `alpha` or `histtype="step"`, legend
  - **Expected output:** A saved overlaid histogram.

- [ ] **Task 44 — Chart the Top Countries**
  - **Objective:** Show which countries are most represented.
  - **Requirements:** Draw a sorted horizontal bar chart of the top 10 countries; state the counting rule (each listed country counted) in the subtitle.
  - **Skills:** `ax.barh()`, `fig.suptitle()` or `ax.set_title()`
  - **Expected output:** A saved horizontal bar chart.

- [ ] **Task 45 — Compare Top Genres by Type**
  - **Objective:** Show genre differences between movies and TV shows.
  - **Requirements:** Create a two-panel figure with the top 10 genres for each type.
  - **Skills:** `plt.subplots(1, 2)`, `ax.barh()`
  - **Expected output:** A saved two-panel figure.

- [ ] **Task 46 — Plot the Rating Distribution**
  - **Objective:** Compare ratings across content types.
  - **Requirements:** Order ratings by overall frequency; split bars by type.
  - **Skills:** `sns.countplot(hue=..., order=...)`
  - **Expected output:** A saved grouped count chart.

- [ ] **Task 47 — Plot Movie Duration**
  - **Objective:** Show the shape of movie length.
  - **Requirements:** Draw a histogram of minutes; add a median line and the IQR thresholds.
  - **Skills:** `sns.histplot()`, `axvline()`
  - **Expected output:** A saved histogram.

- [ ] **Task 48 — Compare Duration Across Decades**
  - **Objective:** Visualize the Task 34 comparison.
  - **Requirements:** Draw a box plot of movie minutes by release decade; include only decades meeting the minimum count.
  - **Skills:** `sns.boxplot()`, filtering
  - **Expected output:** A saved box plot.

- [ ] **Task 49 — Build an Additions Heatmap**
  - **Objective:** Show additions by year and month together.
  - **Requirements:** Pivot counts into a year-by-month table; draw a heatmap with months in calendar order.
  - **Skills:** `pivot_table()`, `sns.heatmap()`
  - **Expected output:** A saved heatmap.

- [ ] **Task 50 — Plot the Addition Gap by Type**
  - **Objective:** Compare how old movies and TV shows are when added.
  - **Requirements:** Draw gap distributions for both types normalized separately so group sizes do not distort the comparison.
  - **Skills:** `sns.histplot(hue=..., stat="density", common_norm=False)`
  - **Expected output:** A saved histogram.

#### Level 6 — Advanced Analysis and Portfolio Delivery (Tasks 51–60)

- [ ] **Task 51 — Investigate the Shift Toward TV Shows**
  - **Objective:** Determine whether TV shows make up a growing share of additions.
  - **Requirements:** Calculate the TV share of additions per year; add a three-year rolling average; write a conclusion that notes the dataset is a single snapshot.
  - **Skills:** `groupby()`, `rolling()`
  - **Expected output:** A trend table, a chart and a short conclusion.

- [ ] **Task 52 — Investigate New vs Older Content**
  - **Objective:** Check whether additions lean toward recent releases or older titles.
  - **Requirements:** Classify additions as recent (gap of 0–1 years) or older (gap of 10+ years); track each share by year added; state clearly that this is a proxy, since the data has no "original content" field.
  - **Skills:** `np.select()`, `crosstab(normalize="index")`
  - **Expected output:** A share-by-year table and a written interpretation.

- [ ] **Task 53 — Compare Country Profiles**
  - **Objective:** Compare the catalogues of three leading countries.
  - **Requirements:** For three countries, compare type mix, audience-group mix, median movie length and top genres.
  - **Skills:** `pivot_table()`, filtering exploded data
  - **Expected output:** A country comparison table.

- [ ] **Task 54 — Build Genre Profiles**
  - **Objective:** Summarize the character of the main genres.
  - **Requirements:** For the eight most common genres, calculate title count, median release year, median movie minutes and median addition gap.
  - **Skills:** `groupby().agg()` on exploded data
  - **Expected output:** A genre profile table.

- [ ] **Task 55 — Compare Recent and Earlier Additions**
  - **Objective:** See how the latest full year of additions differs from earlier years.
  - **Requirements:** Identify the latest complete year; compare type mix, rating groups and median gap with all earlier years combined.
  - **Skills:** Filtering, comparison tables
  - **Expected output:** A two-column comparison table.

- [ ] **Task 56 — Identify Directors Who Work Across Types**
  - **Objective:** Find directors with both movies and TV shows in the catalogue.
  - **Requirements:** Using the expanded director table, find directors with at least one title of each type; list them with their counts.
  - **Skills:** `groupby()`, `nunique()`, filtering
  - **Expected output:** A table of cross-type directors.

- [ ] **Task 57 — Write a Data Validation Function**
  - **Objective:** Make the analysis safe to rerun on updated data.
  - **Requirements:** Check required columns, `show_id` uniqueness, date-parsing failures and duration units that do not match the type; print a clear report.
  - **Skills:** Functions, Boolean checks, error messages
  - **Expected output:** A reusable validation function and its report.

- [ ] **Task 58 — Export Cleaned Data and Summaries**
  - **Objective:** Save reusable outputs without overwriting the raw file.
  - **Requirements:** Save the cleaned dataset and key summary tables to `outputs/`; reload one file to confirm it saved correctly.
  - **Skills:** `to_csv()`, file paths
  - **Expected output:** CSV files in `outputs/`.

- [ ] **Task 59 — Write the Findings Report**
  - **Objective:** Communicate the most important results.
  - **Requirements:** Write five findings with supporting numbers and caveats; explain how missing director, cast and country data affects the conclusions; add three follow-up questions.
  - **Skills:** Analytical writing
  - **Expected output:** A findings section in Markdown.

- [ ] **Task 60 — Finalize the Project README**
  - **Objective:** Present the project as a portfolio piece.
  - **Requirements:** Embed key charts with relative paths; summarize cleaning decisions and methodology; include findings, limitations and instructions to run.
  - **Skills:** Markdown, documentation
  - **Expected output:** A complete project README.

### Progress Tracker
| Level | Tasks | Completed | Remaining |
|-------|:-----:|:---------:|:---------:|
| 1. Data Fundamentals | 1–10 | 0 | 10 |
| 2. Data Cleaning and Manipulation | 11–20 | 0 | 10 |
| 3. Aggregation and Feature Engineering | 21–30 | 0 | 10 |
| 4. Statistical and Analytical Methods | 31–40 | 0 | 10 |
| 5. Data Visualization | 41–50 | 0 | 10 |
| 6. Advanced Analysis and Portfolio Delivery | 51–60 | 0 | 10 |
| **Total** | **60** | **0** | **60** |

---

## Project 3: Formula 1

### Overview
This project analyzes Formula 1 race results to understand how starting position relates to finishing position, how points and wins are distributed among drivers and constructors, how often entries are not classified, and how fastest-lap performance relates to results.

The dataset identifies drivers, constructors, races and statuses by **ID only**. It contains no names, race dates or seasons. All core tasks work with the IDs. Analyses that need names or seasons are listed separately as optional extensions.

**Status:** 0 / 60 tasks completed

### Tasks
#### Level 1 — Data Fundamentals (Tasks 1–10)

- [ ] **Task 01 — Preview the Results**
  - **Objective:** Get a first look at the data.
  - **Requirements:** Load the CSV; display the first 10 rows and 5 random rows with a fixed seed.
  - **Skills:** `pd.read_csv()`, `head()`, `sample()`
  - **Expected output:** Two previews.

- [ ] **Task 02 — Confirm the Schema**
  - **Objective:** Check that the file matches the expected 18 columns.
  - **Requirements:** Report rows and columns; compare column names with the documented schema.
  - **Skills:** `shape`, `columns`
  - **Expected output:** Dimensions and a schema check.

- [ ] **Task 03 — Identify Columns Stored as Text**
  - **Objective:** Find columns that should be numeric but are stored as text.
  - **Requirements:** Review data types; list columns that represent numbers or times but are not numeric.
  - **Skills:** `info()`, `dtypes`
  - **Expected output:** A list of columns needing conversion.

- [ ] **Task 04 — Find Placeholder Values**
  - **Objective:** Detect non-numeric placeholders used for missing data.
  - **Requirements:** For each text column that should be numeric, find values that cannot be converted to numbers; count them per column.
  - **Skills:** `pd.to_numeric(errors="coerce")`, `isna()`, `value_counts()`
  - **Expected output:** A table of placeholder values and counts by column.

- [ ] **Task 05 — Count Unique IDs**
  - **Objective:** Understand the scale of the data.
  - **Requirements:** Count unique values of `resultId`, `raceId`, `driverId`, `constructorId` and `statusId`; confirm `resultId` is unique.
  - **Skills:** `nunique()`, `is_unique`
  - **Expected output:** A table of unique counts.

- [ ] **Task 06 — Measure Field Size per Race**
  - **Objective:** See how many entries each race has.
  - **Requirements:** Count result rows per `raceId`; report the minimum, median and maximum.
  - **Skills:** `groupby().size()`, `describe()`
  - **Expected output:** A field-size summary.

- [ ] **Task 07 — List Position Codes**
  - **Objective:** Understand how non-classified results are recorded.
  - **Requirements:** List all `positionText` values that are not numbers, with counts; record the codes without assuming their meaning.
  - **Skills:** `str.isnumeric()`, `value_counts()`
  - **Expected output:** A table of non-numeric position codes.

- [ ] **Task 08 — Summarize Points**
  - **Objective:** Describe how points are distributed.
  - **Requirements:** Describe `points`; calculate the share of results with zero points.
  - **Skills:** `describe()`, Boolean mean
  - **Expected output:** A summary and a share.

- [ ] **Task 09 — Summarize Laps**
  - **Objective:** Describe laps completed.
  - **Requirements:** Describe `laps`; count results with zero laps.
  - **Skills:** `describe()`, filtering
  - **Expected output:** A summary and a count.

- [ ] **Task 10 — Filter Wins and Pole Starts**
  - **Objective:** Practise selecting key subsets.
  - **Requirements:** Filter all race wins; filter all results starting from grid position 1; report both counts.
  - **Skills:** Boolean filtering, `.loc[]`
  - **Expected output:** Two filtered DataFrames and their counts.

#### Level 2 — Data Cleaning and Manipulation (Tasks 11–20)

- [ ] **Task 11 — Replace Placeholders with Missing Values**
  - **Objective:** Make missing data explicit.
  - **Requirements:** Replace the placeholders found in Task 04 with proper missing values; compare missing counts before and after.
  - **Skills:** `replace()`, `isna().sum()`
  - **Expected output:** A cleaned DataFrame and a before-and-after table.

- [ ] **Task 12 — Convert Columns to Numeric**
  - **Objective:** Make numeric columns usable for calculations.
  - **Requirements:** Convert `position`, `milliseconds`, `fastestLap`, `rank`, `fastestLapSpeed` and `number`; confirm that no valid values were lost in conversion.
  - **Skills:** `pd.to_numeric()`, validation checks
  - **Expected output:** Converted columns and a conversion check.

- [ ] **Task 13 — Flag Classified Results**
  - **Objective:** Separate classified results from the rest.
  - **Requirements:** Create a classified flag based on whether a numeric finishing position exists; report the classified share.
  - **Skills:** `notna()`, Boolean columns
  - **Expected output:** A flag column and a share.

- [ ] **Task 14 — Compare Position and Position Order**
  - **Objective:** Understand how the two position columns differ.
  - **Requirements:** Where `position` is numeric, check whether it equals `positionOrder`; explain why `positionOrder` is populated for every row.
  - **Skills:** Boolean comparison, filtering
  - **Expected output:** A match count and a short explanation.

- [ ] **Task 15 — Handle Grid Position Zero**
  - **Objective:** Decide how to treat results with no grid position.
  - **Requirements:** Count rows with `grid` equal to 0; create a cleaned grid column that treats 0 as missing for position comparisons; document the decision.
  - **Skills:** `np.where()`, `np.nan`
  - **Expected output:** A cleaned grid column and a written decision.

- [ ] **Task 16 — Convert Race Time to Minutes**
  - **Objective:** Make race duration readable.
  - **Requirements:** Convert `milliseconds` to minutes; check which results have a race time; explain why `time` text differs between the winner and other finishers.
  - **Skills:** Vectorized arithmetic, `notna()`
  - **Expected output:** A minutes column and a short explanation.

- [ ] **Task 17 — Parse Fastest Lap Time**
  - **Objective:** Convert lap time text into seconds.
  - **Requirements:** Split `fastestLapTime` into minutes and seconds; calculate total seconds; check that results without a fastest lap stay missing.
  - **Skills:** `str.split()`, `pd.to_numeric()`
  - **Expected output:** A lap-time-in-seconds column.

- [ ] **Task 18 — Check for Duplicate Entries**
  - **Objective:** Make sure each driver appears once per race.
  - **Requirements:** Check for repeated `driverId` within the same `raceId`; investigate any cases before deciding how to treat them.
  - **Skills:** `duplicated(subset=...)`
  - **Expected output:** A duplicate count and notes on any cases found.

- [ ] **Task 19 — Sort by Several Criteria**
  - **Objective:** Practise multi-key sorting.
  - **Requirements:** Sort results by points (descending), then laps (descending), then positionOrder (ascending); show the top 20.
  - **Skills:** `sort_values()` with multiple keys
  - **Expected output:** A sorted table.

- [ ] **Task 20 — Calculate Share of Race Completed**
  - **Objective:** Measure how much of each race every entry completed.
  - **Requirements:** For each race, find the maximum laps completed; divide each entry's laps by that maximum; handle races where the maximum is zero.
  - **Skills:** `groupby().transform("max")`, `np.where()`
  - **Expected output:** A laps-completed share column.

#### Level 3 — Aggregation and Feature Engineering (Tasks 21–30)

- [ ] **Task 21 — Count Driver Appearances**
  - **Objective:** Find how many results each driver has.
  - **Requirements:** Count results per `driverId`; show the 15 drivers with the most appearances.
  - **Skills:** `value_counts()`
  - **Expected output:** An appearance table.

- [ ] **Task 22 — Count Wins and Podiums by Driver**
  - **Objective:** Measure top-level success for each driver.
  - **Requirements:** Count wins and podium finishes (classified results in positions 1–3) per driver; rank by wins.
  - **Skills:** Boolean columns, `groupby().sum()`
  - **Expected output:** A driver success table.

- [ ] **Task 23 — Calculate Driver Points**
  - **Objective:** Compare total and average points.
  - **Requirements:** Calculate total points and points per appearance for each driver; apply a minimum number of appearances to the average ranking.
  - **Skills:** `groupby().agg()`, filtering
  - **Expected output:** A points table.

- [ ] **Task 24 — Summarize Constructors**
  - **Objective:** Compare teams.
  - **Requirements:** For each `constructorId`, calculate results, total points, wins and podiums; rank by total points.
  - **Skills:** `groupby().agg()`
  - **Expected output:** A constructor summary table.

- [ ] **Task 25 — Calculate Positions Gained**
  - **Objective:** Measure how many places each driver gained or lost during a race.
  - **Requirements:** Subtract finishing position from the cleaned grid position; use classified results only; describe the result.
  - **Skills:** Vectorized arithmetic, filtering
  - **Expected output:** A positions-gained column and its summary.

- [ ] **Task 26 — Classify Result Types**
  - **Objective:** Label each result by outcome.
  - **Requirements:** Use `np.select()` to label results as win, podium, points finish, classified without points, or not classified; count each label.
  - **Skills:** `np.select()`, `value_counts()`
  - **Expected output:** A result-class column and its counts.

- [ ] **Task 27 — Calculate Win and Podium Rates**
  - **Objective:** Compare drivers fairly using rates rather than totals.
  - **Requirements:** Calculate win rate and podium rate per driver; apply a minimum number of appearances; handle zero denominators safely.
  - **Skills:** Division, `np.where()`, filtering
  - **Expected output:** A rate table ranked by win rate.

- [ ] **Task 28 — Bucket Grid Positions**
  - **Objective:** Group starting positions for comparison.
  - **Requirements:** Create documented grid buckets (for example, pole, 2–3, 4–10, 11–20, 21+); count results in each.
  - **Skills:** `pd.cut()`
  - **Expected output:** A grid-bucket column and its counts.

- [ ] **Task 29 — Explore Status IDs**
  - **Objective:** Understand how outcomes are distributed by status.
  - **Requirements:** List the most common `statusId` values; check which ones occur with classified results, using the position columns rather than assuming a meaning.
  - **Skills:** `crosstab()`
  - **Expected output:** A status-by-classification table.

- [ ] **Task 30 — Build a Driver Summary**
  - **Objective:** Create one reusable driver-level table.
  - **Requirements:** Include appearances, wins, podiums, total points, points per appearance, median finishing position (classified only) and classification rate.
  - **Skills:** `groupby().agg()` with named aggregations
  - **Expected output:** A driver summary DataFrame.

#### Level 4 — Statistical and Analytical Methods (Tasks 31–40)

- [ ] **Task 31 — Correlate Grid and Finishing Position**
  - **Objective:** Measure how strongly starting position relates to the result.
  - **Requirements:** Use classified results with a valid grid position; calculate Pearson and Spearman correlations; explain what the relationship can and cannot show.
  - **Skills:** `corr(method=...)`, `np.corrcoef()`
  - **Expected output:** Two correlation values and an interpretation.

- [ ] **Task 32 — Calculate Win Share by Grid Position**
  - **Objective:** See how often each starting position produces the winner.
  - **Requirements:** For grid positions 1–10, calculate the share of starts that ended in a win; include the number of starts for each.
  - **Skills:** `groupby()`, Boolean mean
  - **Expected output:** A win-rate-by-grid table.

- [ ] **Task 33 — Compare Positions Gained by Grid Bucket**
  - **Objective:** Check whether drivers starting further back gain more places.
  - **Requirements:** Calculate the mean and median positions gained per grid bucket; explain why starting further back allows more room to gain.
  - **Skills:** `groupby().agg()`
  - **Expected output:** A bucket comparison table.

- [ ] **Task 34 — Compare Mean and Median Finishing Positions**
  - **Objective:** See where averages are distorted by unusual results.
  - **Requirements:** For drivers with a minimum number of classified results, calculate mean and median finishing position; list the drivers where the two differ most.
  - **Skills:** `groupby().agg()`, sorting
  - **Expected output:** A comparison table.

- [ ] **Task 35 — Measure Points Consistency**
  - **Objective:** Identify consistent and inconsistent scorers.
  - **Requirements:** For drivers with a minimum number of appearances, calculate the standard deviation and coefficient of variation of points per race; handle zero means.
  - **Skills:** `np.std()`, `np.where()`
  - **Expected output:** A consistency ranking.

- [ ] **Task 36 — Analyze Fastest-Lap Speed**
  - **Objective:** Describe fastest-lap speeds and their outliers.
  - **Requirements:** Calculate percentiles and IQR outliers for `fastestLapSpeed`; explain why speeds differ mainly because circuits differ.
  - **Skills:** `np.percentile()`, IQR method
  - **Expected output:** A percentile table, outlier count and caveat.

- [ ] **Task 37 — Relate Fastest-Lap Rank to Result**
  - **Objective:** Check whether faster laps go with better finishes.
  - **Requirements:** Using rows with both a fastest-lap `rank` and a classified position, calculate the correlation; report how many rows were used.
  - **Skills:** `dropna()`, `corr()`
  - **Expected output:** A correlation value and sample size.

- [ ] **Task 38 — Standardize Lap Times Within Each Race**
  - **Objective:** Compare fastest laps fairly across different circuits.
  - **Requirements:** Calculate a z-score of fastest-lap seconds within each race; compare drivers' median z-scores (minimum races applied).
  - **Skills:** `groupby().transform()`, NumPy arithmetic
  - **Expected output:** A within-race z-score column and a driver ranking.

- [ ] **Task 39 — Investigate Classified Results with Fewer Laps**
  - **Objective:** Understand classified finishers who did not complete the full race distance.
  - **Requirements:** Using the laps-completed share, count classified results below 100% and below 90%; compare them by status ID.
  - **Skills:** Filtering, `crosstab()`
  - **Expected output:** Counts and a status comparison.

- [ ] **Task 40 — Rank Constructor Consistency**
  - **Objective:** Find teams that score points most consistently.
  - **Requirements:** Calculate each constructor's share of results that scored points; apply a minimum number of results; rank.
  - **Skills:** `groupby()`, Boolean mean, filtering
  - **Expected output:** A ranked constructor table.

#### Level 5 — Data Visualization (Tasks 41–50)

> Every chart needs a clear title, labeled axes with units, and must be saved to `figures/` with `dpi=150` and `bbox_inches="tight"`. Driver and constructor labels will show IDs unless the optional name tables are joined.

- [ ] **Task 41 — Plot the Points Distribution**
  - **Objective:** Show how points are spread across results.
  - **Requirements:** Plot points per result; handle the large number of zero-point results so the rest of the distribution remains visible.
  - **Skills:** `ax.hist()`, axis scaling or separate panels
  - **Expected output:** A saved chart.

- [ ] **Task 42 — Plot Field Size per Race**
  - **Objective:** Show how many entries races typically have.
  - **Requirements:** Draw a histogram of entries per race; mark the median.
  - **Skills:** `sns.histplot()`, `axvline()`
  - **Expected output:** A saved histogram.

- [ ] **Task 43 — Build a Grid vs Finish Heatmap**
  - **Objective:** Show where drivers finish given where they start.
  - **Requirements:** Count classified results for grid 1–20 against finishing position 1–20; normalize each grid row; draw a heatmap.
  - **Skills:** `crosstab(normalize="index")`, `sns.heatmap()`
  - **Expected output:** A saved heatmap.

- [ ] **Task 44 — Compare Finishing Position by Grid Bucket**
  - **Objective:** Show the spread of results for each starting group.
  - **Requirements:** Draw a box plot of finishing position by grid bucket in logical order; invert the y-axis so better positions are at the top.
  - **Skills:** `sns.boxplot()`, `ax.invert_yaxis()`
  - **Expected output:** A saved box plot.

- [ ] **Task 45 — Plot Win Rate by Grid Position**
  - **Objective:** Visualize the Task 32 results.
  - **Requirements:** Draw a bar chart for grid positions 1–10; annotate each bar with its number of starts.
  - **Skills:** `ax.bar()`, `bar_label()`
  - **Expected output:** A saved bar chart.

- [ ] **Task 46 — Plot Positions Gained**
  - **Objective:** Show the distribution of places gained and lost.
  - **Requirements:** Draw a histogram of positions gained; add a vertical reference line at zero.
  - **Skills:** `sns.histplot()`, `axvline()`
  - **Expected output:** A saved histogram.

- [ ] **Task 47 — Chart the Top Drivers by Wins**
  - **Objective:** Show the most successful drivers.
  - **Requirements:** Draw a sorted horizontal bar chart of the top 15 drivers by wins; annotate each bar with the win rate.
  - **Skills:** `ax.barh()`, annotations
  - **Expected output:** A saved horizontal bar chart.

- [ ] **Task 48 — Plot Result Classes**
  - **Objective:** Show how often each outcome occurs.
  - **Requirements:** Draw counts of the result classes from Task 26 in a logical order.
  - **Skills:** `sns.countplot(order=...)`
  - **Expected output:** A saved bar chart.

- [ ] **Task 49 — Compare Within-Race Lap Pace**
  - **Objective:** Visualize the Task 38 z-scores.
  - **Requirements:** For the 10 drivers with the most appearances, draw box plots of within-race fastest-lap z-scores; add a reference line at zero.
  - **Skills:** `sns.boxplot()`, `axhline()`
  - **Expected output:** A saved box plot.

- [ ] **Task 50 — Build a Driver Profile Panel**
  - **Objective:** Summarize one driver in a single figure.
  - **Requirements:** Choose one driver; build a three-panel figure showing grid vs finish, result-class counts and positions gained. Do not use `raceId` as a time axis, since its order is not verified to be chronological.
  - **Skills:** `plt.subplots(1, 3)`, mixed Matplotlib and Seaborn
  - **Expected output:** A saved multi-panel figure.

#### Level 6 — Advanced Analysis and Portfolio Delivery (Tasks 51–60)

- [ ] **Task 51 — Investigate How Much Grid Position Matters**
  - **Objective:** Answer one question with several pieces of evidence.
  - **Requirements:** Combine Tasks 31–33 and 43–45 into a short investigation; state the conclusion, the supporting numbers and the caveat that results from different eras are mixed together.
  - **Skills:** Analytical synthesis
  - **Expected output:** A short written investigation with supporting tables.

- [ ] **Task 52 — Identify Consistent Overtakers**
  - **Objective:** Find drivers who regularly gain places, fairly.
  - **Requirements:** Rank drivers by median positions gained (minimum classified results); then compare each driver with others in the same grid bucket to account for starting position.
  - **Skills:** `groupby()`, `transform()`, multi-level grouping
  - **Expected output:** Two rankings and a note on how they differ.

- [ ] **Task 53 — Compare Classification Rates by Constructor**
  - **Objective:** See which teams most often have entries that are not classified.
  - **Requirements:** Calculate each constructor's non-classified share (minimum results); note that the data cannot separate mechanical failures from accidents without the status table.
  - **Skills:** `groupby()`, Boolean mean
  - **Expected output:** A ranked table and a caveat.

- [ ] **Task 54 — Compare Teammates**
  - **Objective:** Compare drivers in the same car in the same race.
  - **Requirements:** Join results to themselves on `raceId` and `constructorId`; keep pairs of different drivers where both were classified; count head-to-head finishes for pairs with a minimum number of shared races.
  - **Skills:** `merge()`, filtering, `groupby()`
  - **Expected output:** A head-to-head teammate table.

- [ ] **Task 55 — Relate Fastest Lap to Winning**
  - **Objective:** Check how often the driver with the fastest lap wins.
  - **Requirements:** Among races where `rank` is recorded, calculate the share in which the fastest-lap holder won; report how many races have no fastest-lap data.
  - **Skills:** Filtering, `groupby()`
  - **Expected output:** A share, a race count and a coverage note.

- [ ] **Task 56 — Detect Different Scoring Systems**
  - **Objective:** Show why points totals cannot be compared directly across races.
  - **Requirements:** List the distinct points values awarded for a win and how many races used each; explain what this means for comparing career totals.
  - **Skills:** Filtering, `value_counts()`
  - **Expected output:** A table of winner points values and an explanation.

- [ ] **Task 57 — Write a Data Validation Function**
  - **Objective:** Make the analysis safe to rerun on updated data.
  - **Requirements:** Check required columns, placeholder values, `resultId` uniqueness, duplicate driver entries per race and impossible values (negative laps or points); print a clear report.
  - **Skills:** Functions, Boolean checks, error messages
  - **Expected output:** A reusable validation function and its report.

- [ ] **Task 58 — Export Results**
  - **Objective:** Save reusable outputs separately from the raw data.
  - **Requirements:** Export the cleaned results, driver summary, constructor summary and teammate table to `outputs/`; reload one file to confirm it saved correctly.
  - **Skills:** `to_csv()`, file paths
  - **Expected output:** CSV files in `outputs/`.

- [ ] **Task 59 — Write the Findings Report**
  - **Objective:** Communicate the most important results.
  - **Requirements:** Write five findings with numbers and caveats; explain the limits of comparing results across eras and scoring systems; add three follow-up questions.
  - **Skills:** Analytical writing
  - **Expected output:** A findings section in Markdown.

- [ ] **Task 60 — Finalize the Project README**
  - **Objective:** Present the project as a portfolio piece.
  - **Requirements:** Embed key charts with relative paths; summarize cleaning decisions and methodology; include findings, limitations and instructions to run.
  - **Skills:** Markdown, documentation
  - **Expected output:** A complete project README.

#### Optional Extensions (Require Supplementary Data)

These are not part of the 60 tasks. They need additional tables from the same source as the results file.

| Extension | Additional file needed | Join key | What it enables |
|-----------|------------------------|----------|-----------------|
| Driver names | Drivers table | `driverId` | Readable chart labels and driver rankings by name |
| Constructor names | Constructors table | `constructorId` | Readable team names |
| Seasons and dates | Races table | `raceId` | Season-by-season trends, champions per season, chronological charts |
| Status descriptions | Status table | `statusId` | Separating finishes, accidents and mechanical failures |

### Progress Tracker
| Level | Tasks | Completed | Remaining |
|-------|:-----:|:---------:|:---------:|
| 1. Data Fundamentals | 1–10 | 0 | 10 |
| 2. Data Cleaning and Manipulation | 11–20 | 0 | 10 |
| 3. Aggregation and Feature Engineering | 21–30 | 0 | 10 |
| 4. Statistical and Analytical Methods | 31–40 | 0 | 10 |
| 5. Data Visualization | 41–50 | 0 | 10 |
| 6. Advanced Analysis and Portfolio Delivery | 51–60 | 0 | 10 |
| **Total** | **60** | **0** | **60** |

---

## Project 4: International Football

### Overview
This project analyzes international men's football match results to measure home advantage, compare neutral and non-neutral venues, track scoring trends over time, compare tournaments, and summarize team performance. A key part of the work is analyzing teams consistently from both the home and away side.

**Status:** 0 / 60 tasks completed

### Tasks
#### Level 1 — Data Fundamentals (Tasks 1–10)

- [ ] **Task 01 — Preview the Matches**
  - **Objective:** Get a first look at the data.
  - **Requirements:** Load the CSV; display the first 10 and last 10 rows.
  - **Skills:** `pd.read_csv()`, `head()`, `tail()`
  - **Expected output:** Two previews.

- [ ] **Task 02 — Inspect Size and Types**
  - **Objective:** Understand the structure of the dataset.
  - **Requirements:** Report rows and columns; review data types; note which columns need conversion.
  - **Skills:** `shape`, `info()`
  - **Expected output:** Dimensions and a short type review.

- [ ] **Task 03 — Parse Match Dates**
  - **Objective:** Turn the date column into a real date.
  - **Requirements:** Convert with invalid values set to missing; count failures; report the earliest and latest dates.
  - **Skills:** `pd.to_datetime(errors="coerce")`, `min()`, `max()`
  - **Expected output:** A datetime column, a failure count and a date range.

- [ ] **Task 04 — Count Teams**
  - **Objective:** Find how many national teams appear.
  - **Requirements:** Count unique home teams, unique away teams and unique teams across both columns combined.
  - **Skills:** `nunique()`, `pd.concat()` or set union
  - **Expected output:** Three counts.

- [ ] **Task 05 — Explore Tournaments**
  - **Objective:** See which competitions are included.
  - **Requirements:** Count unique tournaments; list the 10 with the most matches and their share of all matches.
  - **Skills:** `value_counts(normalize=True)`
  - **Expected output:** A top-10 tournament table.

- [ ] **Task 06 — Check Missing Values**
  - **Objective:** Find incomplete records.
  - **Requirements:** Count missing values per column; inspect any rows without scores and describe what they appear to be.
  - **Skills:** `isna()`, filtering
  - **Expected output:** A missing-value table and a short note.

- [ ] **Task 07 — Check for Duplicates**
  - **Objective:** Make sure each match is recorded once.
  - **Requirements:** Count fully duplicated rows; check for repeated combinations of date, home team and away team; inspect any cases found.
  - **Skills:** `duplicated(subset=...)`
  - **Expected output:** Two counts and notes.

- [ ] **Task 08 — Summarize Scores**
  - **Objective:** Describe typical goals for home and away teams.
  - **Requirements:** Describe `home_score` and `away_score`; compare their means and medians.
  - **Skills:** `describe()`
  - **Expected output:** A side-by-side summary.

- [ ] **Task 09 — Inspect the Neutral Flag**
  - **Objective:** Understand how often matches are played at neutral venues.
  - **Requirements:** Check the data type and values of `neutral`; calculate the neutral share.
  - **Skills:** `value_counts(normalize=True)`, `dtype`
  - **Expected output:** Counts and a share.

- [ ] **Task 10 — Apply Basic Filters**
  - **Objective:** Practise selecting subsets.
  - **Requirements:** Filter matches in a year of your choice; filter matches played in a country of your choice; report both counts.
  - **Skills:** Boolean filtering, `.dt.year`
  - **Expected output:** Two filtered DataFrames and their counts.

#### Level 2 — Data Cleaning and Manipulation (Tasks 11–20)

- [ ] **Task 11 — Separate Unplayed Matches**
  - **Objective:** Keep only matches with a result for outcome analysis.
  - **Requirements:** Move rows without scores into a separate DataFrame; document how many were set aside and why.
  - **Skills:** `notna()`, filtering
  - **Expected output:** A played-matches DataFrame and a written decision.

- [ ] **Task 12 — Validate Scores**
  - **Objective:** Make sure scores are valid whole numbers.
  - **Requirements:** Check for negative or non-integer scores; convert scores to an integer type.
  - **Skills:** Boolean checks, `astype()`
  - **Expected output:** Validated score columns and a check result.

- [ ] **Task 13 — Create Goal Columns**
  - **Objective:** Build the core calculated fields.
  - **Requirements:** Create total goals and goal difference from the home team's perspective.
  - **Skills:** Vectorized arithmetic, `assign()`
  - **Expected output:** Two new columns.

- [ ] **Task 14 — Label Match Outcomes**
  - **Objective:** Classify each match result.
  - **Requirements:** Use `np.select()` to label home win, away win or draw; check that the three counts add up to the number of played matches.
  - **Skills:** `np.select()`
  - **Expected output:** An outcome column and a check.

- [ ] **Task 15 — Extract Date Features**
  - **Objective:** Prepare columns for time-based analysis.
  - **Requirements:** Extract year, decade, month and weekday.
  - **Skills:** `.dt` accessor, integer division
  - **Expected output:** Four new columns.

- [ ] **Task 16 — Check Team Name Consistency**
  - **Objective:** Find formatting problems in team names.
  - **Requirements:** Check for leading or trailing spaces and case differences; list any suspected variants; do not merge historical names without a reliable source.
  - **Skills:** `str.strip()`, `str.lower()`, comparison
  - **Expected output:** A list of issues and a documented decision.

- [ ] **Task 17 — Build a Team-Perspective Table**
  - **Objective:** Analyze every team consistently, whether listed as home or away.
  - **Requirements:** Create one row per team per match with team, opponent, goals for, goals against, a home/away indicator, the neutral flag and the result (W/D/L) from that team's perspective; combine home and away views.
  - **Skills:** `rename()`, `pd.concat()`, `np.select()`
  - **Expected output:** A long team-perspective DataFrame.

- [ ] **Task 18 — Validate the Team-Perspective Table**
  - **Objective:** Confirm the reshape is correct.
  - **Requirements:** Check that it has exactly twice as many rows as played matches; check that total goals for equals total goals against; check that wins equal losses overall.
  - **Skills:** Assertions, aggregation
  - **Expected output:** Three passed checks.

- [ ] **Task 19 — Filter One Team's Matches**
  - **Objective:** Retrieve every match for a chosen team.
  - **Requirements:** Use the team-perspective table to select one team's matches; confirm the count equals its home plus away appearances in the original data.
  - **Skills:** `.query()`, filtering
  - **Expected output:** A filtered table and a matching count check.

- [ ] **Task 20 — Group Tournaments into Categories**
  - **Objective:** Create broader competition categories.
  - **Requirements:** Write documented text rules to group tournaments (for example, friendly, World Cup, World Cup qualification, continental championship, other); list tournaments that fall into "other" so the rules can be reviewed.
  - **Skills:** `str.contains()`, `np.select()`
  - **Expected output:** A category column and a list of unmapped tournaments.

#### Level 3 — Aggregation and Feature Engineering (Tasks 21–30)

- [ ] **Task 21 — Calculate Outcome Percentages**
  - **Objective:** Measure how often home wins, away wins and draws occur.
  - **Requirements:** Calculate each outcome's share of played matches.
  - **Skills:** `value_counts(normalize=True)`
  - **Expected output:** Three percentages.

- [ ] **Task 22 — Measure Goals per Match**
  - **Objective:** Describe scoring overall and by decade.
  - **Requirements:** Calculate average total goals per match overall and per decade with match counts.
  - **Skills:** `groupby().agg()`
  - **Expected output:** A decade scoring table.

- [ ] **Task 23 — Build Team Records**
  - **Objective:** Summarize every team's results.
  - **Requirements:** Using the team-perspective table, calculate matches, wins, draws, losses, goals for and goals against per team.
  - **Skills:** `groupby().agg()`, Boolean sums
  - **Expected output:** A team record table.

- [ ] **Task 24 — Rank Teams by Win Rate**
  - **Objective:** Compare teams fairly.
  - **Requirements:** Calculate win rate per team; apply a minimum number of matches; rank teams.
  - **Skills:** Division, filtering, `rank()`
  - **Expected output:** A ranked win-rate table.

- [ ] **Task 25 — Calculate Goals per Match by Team**
  - **Objective:** Compare attacking and defensive output.
  - **Requirements:** Calculate goals scored and conceded per match for each team meeting the minimum matches.
  - **Skills:** `groupby().agg()`, division
  - **Expected output:** A per-match goals table.

- [ ] **Task 26 — Summarize Tournaments**
  - **Objective:** Compare competitions.
  - **Requirements:** For each tournament with a minimum number of matches, calculate match count, average goals, draw share and home-win share.
  - **Skills:** `groupby().agg()`, filtering
  - **Expected output:** A tournament summary table.

- [ ] **Task 27 — Summarize Each Year**
  - **Objective:** Track activity and scoring over time.
  - **Requirements:** Calculate matches per year and average goals per match per year.
  - **Skills:** `groupby()`
  - **Expected output:** An annual summary table.

- [ ] **Task 28 — Split a Team's Record by Venue**
  - **Objective:** See how a chosen team performs at home, away and at neutral venues.
  - **Requirements:** For one team, calculate matches, win rate and goal difference per match in each venue type.
  - **Skills:** `np.select()`, `groupby()`
  - **Expected output:** A three-row venue comparison.

- [ ] **Task 29 — Check Whether the Home Team Is Hosting**
  - **Objective:** Identify matches where the listed home team plays in its own country.
  - **Requirements:** Flag non-neutral matches where `home_team` matches `country`; count matches where they differ and inspect examples; note naming mismatches as a caveat.
  - **Skills:** Column comparison, `np.where()`
  - **Expected output:** A hosting flag and a short note.

- [ ] **Task 30 — Summarize a Head-to-Head Rivalry**
  - **Objective:** Compare two chosen teams directly.
  - **Requirements:** Select all matches between two teams regardless of home/away order; calculate wins for each side, draws and goals.
  - **Skills:** Combined Boolean filtering
  - **Expected output:** A head-to-head summary.

#### Level 4 — Statistical and Analytical Methods (Tasks 31–40)

- [ ] **Task 31 — Summarize the Goals Distribution**
  - **Objective:** Describe how many goals matches usually have.
  - **Requirements:** Calculate mean, median, standard deviation (state which convention) and the 25th, 75th and 90th percentiles of total goals.
  - **Skills:** `np.mean()`, `np.median()`, `np.std()`, `np.percentile()`
  - **Expected output:** A statistics table.

- [ ] **Task 32 — Define High-Scoring Matches**
  - **Objective:** Identify unusually high-scoring matches and how their frequency has changed.
  - **Requirements:** Set thresholds at the 95th and 99th percentiles; calculate the share of matches above each threshold by decade.
  - **Skills:** `np.quantile()`, `groupby()`
  - **Expected output:** Thresholds and a share-by-decade table.

- [ ] **Task 33 — Compare Neutral and Non-Neutral Matches**
  - **Objective:** Measure how home advantage changes at neutral venues.
  - **Requirements:** Compare home-win, draw and away-win shares and average goal difference for neutral vs non-neutral matches; include counts.
  - **Skills:** `crosstab(normalize="index")`, `groupby()`
  - **Expected output:** A comparison table.

- [ ] **Task 34 — Track Home Advantage Over Time**
  - **Objective:** See whether home advantage has changed.
  - **Requirements:** Using non-neutral matches only, calculate home-win share and average goal difference by decade with counts.
  - **Skills:** `groupby().agg()`
  - **Expected output:** A decade trend table.

- [ ] **Task 35 — Smooth the Scoring Trend**
  - **Objective:** Reduce year-to-year noise in average goals.
  - **Requirements:** Resample matches by year; calculate average goals per match; add a 10-year rolling average; explain the choice of window.
  - **Skills:** `set_index()`, `resample()`, `rolling()`
  - **Expected output:** A yearly series with a rolling average.

- [ ] **Task 36 — Analyze Winning Margins**
  - **Objective:** Understand how often matches are one-sided.
  - **Requirements:** List the 10 largest winning margins; calculate the share of matches with a margin of five or more by tournament category.
  - **Skills:** `np.abs()`, `nlargest()`, `groupby()`
  - **Expected output:** A top-10 table and a share table.

- [ ] **Task 37 — Compare Draw Rates by Category**
  - **Objective:** See whether some competitions produce more draws.
  - **Requirements:** Calculate draw share by tournament category with a minimum match count; rank categories.
  - **Skills:** `groupby()`, Boolean mean
  - **Expected output:** A ranked draw-rate table.

- [ ] **Task 38 — Compare a Team's Earlier and Later Periods**
  - **Objective:** Measure how a team's performance has changed.
  - **Requirements:** Split one team's matches into two periods using a documented cut-off; compare win rate and goals for and against per match; note that opponent strength may differ between periods.
  - **Skills:** `np.where()`, `groupby()`
  - **Expected output:** A two-period comparison and a caveat.

- [ ] **Task 39 — Find the Most Common Scorelines**
  - **Objective:** Identify typical final scores.
  - **Requirements:** Cap scores at 5 to group high values; build a home-score by away-score count table; list the five most common scorelines and their shares.
  - **Skills:** `np.clip()`, `crosstab()`
  - **Expected output:** A scoreline table and top-five list.

- [ ] **Task 40 — Measure Team Consistency Across Decades**
  - **Objective:** Identify teams whose performance is stable over time.
  - **Requirements:** For teams with enough matches per decade, calculate win rate per decade and the standard deviation across decades; rank by consistency.
  - **Skills:** `groupby()`, `pivot_table()`, `std()`
  - **Expected output:** A consistency ranking.

#### Level 5 — Data Visualization (Tasks 41–50)

> Every chart needs a clear title, labeled axes with units, and must be saved to `figures/` with `dpi=150` and `bbox_inches="tight"`.

- [ ] **Task 41 — Plot Goals per Match**
  - **Objective:** Show how many goals matches usually have.
  - **Requirements:** Draw a histogram of total goals with one bar per whole number.
  - **Skills:** `sns.histplot(discrete=True)`
  - **Expected output:** A saved histogram.

- [ ] **Task 42 — Plot the Scoring Trend**
  - **Objective:** Show how average goals have changed.
  - **Requirements:** Plot yearly average goals as a faint line and the 10-year rolling average as a bold line.
  - **Skills:** `ax.plot()`, legend, styling
  - **Expected output:** A saved line chart.

- [ ] **Task 43 — Plot Matches per Year**
  - **Objective:** Show how the volume of recorded matches has grown.
  - **Requirements:** Draw a line chart of matches per year; annotate one or two notable features.
  - **Skills:** `ax.plot()`, `ax.annotate()`
  - **Expected output:** A saved line chart.

- [ ] **Task 44 — Compare Outcomes by Venue Type**
  - **Objective:** Visualize the Task 33 comparison.
  - **Requirements:** Draw grouped bars of outcome shares for neutral and non-neutral matches; include counts in the legend or labels.
  - **Skills:** `ax.bar()` with offsets or `sns.barplot(hue=...)`
  - **Expected output:** A saved grouped bar chart.

- [ ] **Task 45 — Plot Home Advantage Over Time**
  - **Objective:** Visualize the Task 34 trend.
  - **Requirements:** Draw the home-win share by decade for non-neutral matches; add a horizontal line at the overall share.
  - **Skills:** `sns.lineplot()`, `axhline()`
  - **Expected output:** A saved line chart.

- [ ] **Task 46 — Draw a Scoreline Heatmap**
  - **Objective:** Show the most common final scores.
  - **Requirements:** Use the capped scoreline table from Task 39; show shares with labels; mark the capped "5+" category clearly.
  - **Skills:** `sns.heatmap(annot=True)`
  - **Expected output:** A saved heatmap.

- [ ] **Task 47 — Rank Tournaments by Goals**
  - **Objective:** Show which tournaments produce the most goals.
  - **Requirements:** Draw a sorted horizontal bar chart of average goals for tournaments meeting the minimum match count; annotate match counts.
  - **Skills:** `ax.barh()`, annotations
  - **Expected output:** A saved horizontal bar chart.

- [ ] **Task 48 — Compare Goals Across Decades**
  - **Objective:** Show the spread of goals per match by decade.
  - **Requirements:** Draw a box plot of total goals by decade in chronological order.
  - **Skills:** `sns.boxplot(order=...)`
  - **Expected output:** A saved box plot.

- [ ] **Task 49 — Compare Three Teams**
  - **Objective:** Compare several metrics for three chosen teams.
  - **Requirements:** Show win rate, goals scored per match and goals conceded per match in a multi-panel figure with consistent team colours.
  - **Skills:** `plt.subplots(1, 3)`, `ax.bar()`
  - **Expected output:** A saved multi-panel figure.

- [ ] **Task 50 — Plot a Rivalry Over Time**
  - **Objective:** Show how a head-to-head record developed.
  - **Requirements:** For the Task 30 rivalry, plot cumulative wins for each team and cumulative draws by date.
  - **Skills:** `cumsum()`, `ax.plot()`
  - **Expected output:** A saved line chart.

#### Level 6 — Advanced Analysis and Portfolio Delivery (Tasks 51–60)

- [ ] **Task 51 — Investigate Home Advantage**
  - **Objective:** Answer one question with several pieces of evidence.
  - **Requirements:** Combine the overall, venue-type, decade and tournament-category results; state the conclusion; list possible contributing factors (team strength, travel, crowd, scheduling) without claiming any single cause.
  - **Skills:** Analytical synthesis
  - **Expected output:** A short written investigation with supporting tables.

- [ ] **Task 52 — Investigate Scoring Trends Fairly**
  - **Objective:** Check whether changes in average goals are explained by changes in the mix of competitions.
  - **Requirements:** Calculate the share of friendlies per decade; compare average goals per decade for friendlies and competitive matches separately.
  - **Skills:** `pivot_table()`, `groupby()`
  - **Expected output:** Two trend tables and a conclusion.

- [ ] **Task 53 — Profile the Strongest Teams**
  - **Objective:** Compare top teams in competitive matches and friendlies.
  - **Requirements:** For the top 10 teams by win rate (minimum matches), calculate win rate and goal difference per match separately for competitive matches and friendlies.
  - **Skills:** `pivot_table()`, filtering
  - **Expected output:** A team profile table.

- [ ] **Task 54 — Measure the Hosting Effect**
  - **Objective:** Compare team performance when hosting, playing away and at neutral venues.
  - **Requirements:** Using the hosting flag from Task 29, calculate each top team's win rate in each situation; apply minimum counts.
  - **Skills:** `groupby()`, `unstack()`
  - **Expected output:** A team-by-situation table.

- [ ] **Task 55 — Analyze Tournament Evolution**
  - **Objective:** See how competition categories have changed over time.
  - **Requirements:** Build pivot tables of average goals and draw share by tournament category and decade; mark cells with too few matches.
  - **Skills:** `pivot_table()`, masking
  - **Expected output:** Two pivot tables.

- [ ] **Task 56 — Track a Team's Form**
  - **Objective:** Show how one team's results change over time.
  - **Requirements:** Sort the team's matches by date; calculate a rolling win rate over a documented number of matches.
  - **Skills:** `sort_values()`, `rolling()`
  - **Expected output:** A rolling win-rate series.

- [ ] **Task 57 — Write a Data Validation Function**
  - **Objective:** Make the analysis safe to rerun on updated data.
  - **Requirements:** Check required columns, date parsing failures, missing and negative scores, duplicate matches and the team-perspective row count; print a clear report.
  - **Skills:** Functions, Boolean checks, error messages
  - **Expected output:** A reusable validation function and its report.

- [ ] **Task 58 — Export Results**
  - **Objective:** Save reusable outputs separately from the raw data.
  - **Requirements:** Export the team-perspective table, team summary, tournament summary and annual summary to `outputs/`; reload one file to confirm it saved correctly.
  - **Skills:** `to_csv()`, file paths
  - **Expected output:** CSV files in `outputs/`.

- [ ] **Task 59 — Write the Findings Report**
  - **Objective:** Communicate the most important results.
  - **Requirements:** Write five findings with numbers and caveats; explain how data coverage (more recorded matches in recent decades) affects comparisons; add three follow-up questions.
  - **Skills:** Analytical writing
  - **Expected output:** A findings section in Markdown.

- [ ] **Task 60 — Finalize the Project README**
  - **Objective:** Present the project as a portfolio piece.
  - **Requirements:** Embed key charts with relative paths; explain how home and away perspectives are handled; include findings, limitations and instructions to run.
  - **Skills:** Markdown, documentation
  - **Expected output:** A complete project README.

### Progress Tracker
| Level | Tasks | Completed | Remaining |
|-------|:-----:|:---------:|:---------:|
| 1. Data Fundamentals | 1–10 | 0 | 10 |
| 2. Data Cleaning and Manipulation | 11–20 | 0 | 10 |
| 3. Aggregation and Feature Engineering | 21–30 | 0 | 10 |
| 4. Statistical and Analytical Methods | 31–40 | 0 | 10 |
| 5. Data Visualization | 41–50 | 0 | 10 |
| 6. Advanced Analysis and Portfolio Delivery | 51–60 | 0 | 10 |
| **Total** | **60** | **0** | **60** |

---

## Project 5: World Happiness 2019

### Overview
This project analyzes the World Happiness Report 2019 country data to understand how happiness scores are distributed, how higher- and lower-ranked countries differ, and how strongly the score is associated with each indicator. Because the data is at country level, the project also focuses on what such data can and cannot tell us about individuals or causes.

**Status:** 0 / 60 tasks completed

### Tasks
#### Level 1 — Data Fundamentals (Tasks 1–10)

- [ ] **Task 01 — Preview the Dataset**
  - **Objective:** Get a first look at the data.
  - **Requirements:** Load the CSV; display the first 10 and last 10 rows.
  - **Skills:** `pd.read_csv()`, `head()`, `tail()`
  - **Expected output:** Two previews.

- [ ] **Task 02 — Rename Columns for Analysis**
  - **Objective:** Make column names easier to work with.
  - **Requirements:** Report rows and columns; create a renamed copy using lowercase names with underscores; keep the mapping as a documented dictionary.
  - **Skills:** `shape`, `rename()`
  - **Expected output:** A renamed DataFrame and the mapping.

- [ ] **Task 03 — Check Types and Missing Values**
  - **Objective:** Confirm the data is complete and numeric where expected.
  - **Requirements:** Review data types; count missing values per column.
  - **Skills:** `info()`, `isna().sum()`
  - **Expected output:** A type and missing-value summary.

- [ ] **Task 04 — Check Country Uniqueness**
  - **Objective:** Make sure each country appears once.
  - **Requirements:** Compare unique country names with the row count; list any repeated names.
  - **Skills:** `nunique()`, `duplicated()`
  - **Expected output:** A uniqueness check.

- [ ] **Task 05 — Describe All Numeric Columns**
  - **Objective:** Get an overview of every indicator.
  - **Requirements:** Generate descriptive statistics; note which indicators have the widest relative spread.
  - **Skills:** `describe()`
  - **Expected output:** A statistics table and a short note.

- [ ] **Task 06 — Verify Rank Order**
  - **Objective:** Confirm that the rank column matches the score.
  - **Requirements:** Sort by `Score` descending; check whether `Overall rank` follows the same order; identify any ties.
  - **Skills:** `sort_values()`, `rank()`, comparison
  - **Expected output:** A check result and any exceptions.

- [ ] **Task 07 — List the 10 Happiest Countries**
  - **Objective:** Identify the top of the ranking.
  - **Requirements:** Show the 10 highest-scoring countries with their scores.
  - **Skills:** `nlargest()`
  - **Expected output:** A top-10 table.

- [ ] **Task 08 — List the 10 Least Happy Countries**
  - **Objective:** Identify the bottom of the ranking.
  - **Requirements:** Show the 10 lowest-scoring countries with their scores.
  - **Skills:** `nsmallest()`
  - **Expected output:** A bottom-10 table.

- [ ] **Task 09 — Filter by Score Thresholds**
  - **Objective:** Practise threshold filtering.
  - **Requirements:** Count countries with a score above 7 and below 4; express each as a share of all countries.
  - **Skills:** Boolean filtering
  - **Expected output:** Two counts and shares.

- [ ] **Task 10 — Look Up One Country**
  - **Objective:** Practise retrieving one record.
  - **Requirements:** Choose a country; show its score, rank and indicator values; calculate its score percentile among all countries.
  - **Skills:** `.loc[]`, `rank(pct=True)`
  - **Expected output:** A one-country profile.

#### Level 2 — Data Cleaning and Manipulation (Tasks 11–20)

- [ ] **Task 11 — Investigate Zero Values**
  - **Objective:** Decide whether zeros are real values or missing data.
  - **Requirements:** Count exact zeros in each indicator; inspect the countries involved; document how they will be treated.
  - **Skills:** Boolean filtering, `sum()`
  - **Expected output:** A zero-value table and a written decision.

- [ ] **Task 12 — Validate Value Ranges**
  - **Objective:** Check for impossible values.
  - **Requirements:** Confirm indicators are non-negative and scores fall within 0–10; report any failures.
  - **Skills:** Boolean checks, `any()`
  - **Expected output:** A validation result.

- [ ] **Task 13 — Flag Above- and Below-Average Countries**
  - **Objective:** Create simple comparison labels.
  - **Requirements:** Use `np.where()` to label each country as above or below average for score and for GDP.
  - **Skills:** `np.where()`, `np.mean()`
  - **Expected output:** Two label columns and their counts.

- [ ] **Task 14 — Classify Score–GDP Quadrants**
  - **Objective:** Group countries by score and GDP together.
  - **Requirements:** Use the medians of score and GDP to assign four quadrant labels with `np.select()`; count countries in each.
  - **Skills:** `np.select()`, `np.median()`
  - **Expected output:** A quadrant column and its counts.

- [ ] **Task 15 — Calculate Score Percentile Ranks**
  - **Objective:** Express each country's position as a percentile.
  - **Requirements:** Calculate the percentile rank of every country's score.
  - **Skills:** `rank(pct=True)`
  - **Expected output:** A percentile-rank column.

- [ ] **Task 16 — Rank Every Indicator**
  - **Objective:** Compare countries' positions across indicators.
  - **Requirements:** Rank countries on each indicator (1 = highest); add the ranks as new columns.
  - **Skills:** `rank(ascending=False)`, loops or `apply()` on columns
  - **Expected output:** Six rank columns.

- [ ] **Task 17 — Calculate the Happiness–GDP Rank Gap**
  - **Objective:** Find countries ranked very differently on happiness and GDP.
  - **Requirements:** Subtract the GDP rank from the happiness rank; list the 10 largest positive and negative gaps.
  - **Skills:** Vectorized arithmetic, sorting
  - **Expected output:** Two top-10 tables.

- [ ] **Task 18 — Filter with a Query**
  - **Objective:** Practise readable multi-condition filtering.
  - **Requirements:** Use `.query()` to find countries with above-median social support but below-median score.
  - **Skills:** `.query()`
  - **Expected output:** A filtered table.

- [ ] **Task 19 — Check Country Name Formatting**
  - **Objective:** Make sure names are clean for joining or display.
  - **Requirements:** Check for leading or trailing spaces and unusual characters; trim whitespace only; document any other issues found.
  - **Skills:** `str.strip()`, `str.contains()`
  - **Expected output:** A short list of issues and the action taken.

- [ ] **Task 20 — Sort by Several Indicators**
  - **Objective:** Practise multi-key sorting.
  - **Requirements:** Sort countries by freedom (descending), then generosity (descending); show the top 15.
  - **Skills:** `sort_values()` with multiple keys
  - **Expected output:** A sorted table.

#### Level 3 — Aggregation and Feature Engineering (Tasks 21–30)

- [ ] **Task 21 — Create Happiness Bands with NumPy**
  - **Objective:** Group countries into four score bands.
  - **Requirements:** Calculate quartile boundaries with `np.percentile()`; assign bands with `pd.cut()`; count countries per band.
  - **Skills:** `np.percentile()`, `pd.cut()`
  - **Expected output:** A band column and its counts.

- [ ] **Task 22 — Compare with Quantile-Based Bands**
  - **Objective:** Check whether a different method gives the same bands.
  - **Requirements:** Create bands with `pd.qcut()`; compare with Task 21; explain any differences at the boundaries.
  - **Skills:** `pd.qcut()`, `crosstab()`
  - **Expected output:** A comparison table and explanation.

- [ ] **Task 23 — Summarize Indicators by Band**
  - **Objective:** See how indicators change from the lowest to highest band.
  - **Requirements:** Calculate the mean and median of each indicator per band.
  - **Skills:** `groupby().agg()`
  - **Expected output:** A band summary table.

- [ ] **Task 24 — Compare the Top 10 and Bottom 10**
  - **Objective:** Measure the gap between the highest- and lowest-ranked countries.
  - **Requirements:** Calculate average indicators for each group; add the difference and ratio for each indicator; handle a zero denominator safely.
  - **Skills:** Filtering, division, `np.where()`
  - **Expected output:** A comparison table.

- [ ] **Task 25 — Create GDP Tiers**
  - **Objective:** Group countries by GDP level.
  - **Requirements:** Define three tiers using terciles of GDP; assign them with `np.select()`; calculate median score and country count per tier.
  - **Skills:** `np.quantile()`, `np.select()`, `groupby()`
  - **Expected output:** A tier column and a tier summary.

- [ ] **Task 26 — Cross-Tabulate Bands and GDP Tiers**
  - **Objective:** See how happiness bands and GDP tiers overlap.
  - **Requirements:** Build a crosstab of happiness band by GDP tier; show both counts and row percentages.
  - **Skills:** `crosstab(normalize=...)`
  - **Expected output:** Two crosstabs.

- [ ] **Task 27 — Compare the Indicator Total with the Score**
  - **Objective:** Check how much of the score the six indicator columns add up to.
  - **Requirements:** Sum the six indicators per country; subtract the total from the score; describe the remainder and note that it is not explained by any column in this file.
  - **Skills:** `sum(axis=1)`, `describe()`
  - **Expected output:** A remainder column and its summary.

- [ ] **Task 28 — Calculate Indicator Shares**
  - **Objective:** See which indicators make up the largest share of the score.
  - **Requirements:** Divide each indicator by the score for every country; calculate the average share per indicator; compare top and bottom bands.
  - **Skills:** Vectorized division, `groupby()`
  - **Expected output:** A share table.

- [ ] **Task 29 — Build a Country Summary**
  - **Objective:** Create one reusable country-level table.
  - **Requirements:** Include country, score, rank, band, GDP tier, quadrant, GDP, social support, healthy life expectancy and freedom.
  - **Skills:** Column selection, `assign()`
  - **Expected output:** A country summary DataFrame.

- [ ] **Task 30 — Find Countries Happy Despite Low GDP**
  - **Objective:** Identify countries with high scores relative to economic output.
  - **Requirements:** Filter countries with below-median GDP and a top-quartile score; show their other indicators.
  - **Skills:** Combined Boolean filtering
  - **Expected output:** A filtered table.

#### Level 4 — Statistical and Analytical Methods (Tasks 31–40)

- [ ] **Task 31 — Summarize the Score Distribution**
  - **Objective:** Describe the centre and spread of happiness.
  - **Requirements:** Calculate mean, median, standard deviation (state whether sample or population), range and IQR.
  - **Skills:** `np.mean()`, `np.median()`, `np.std(ddof=...)`, `np.percentile()`
  - **Expected output:** A statistics table.

- [ ] **Task 32 — Calculate Score Percentiles**
  - **Objective:** Describe the score distribution in detail.
  - **Requirements:** Calculate the 10th, 25th, 50th, 75th and 90th percentiles.
  - **Skills:** `np.percentile()`
  - **Expected output:** A percentile table.

- [ ] **Task 33 — Detect Outliers with IQR**
  - **Objective:** Find unusual values in the score and every indicator.
  - **Requirements:** Apply the IQR rule to each column; list the outlying countries and the column involved.
  - **Skills:** `np.percentile()`, loops, filtering
  - **Expected output:** An outlier table.

- [ ] **Task 34 — Build a Correlation Matrix**
  - **Objective:** Measure associations between all numeric columns.
  - **Requirements:** Calculate Pearson correlations for score and all indicators; rank indicators by their correlation with score.
  - **Skills:** `corr()`, sorting
  - **Expected output:** A correlation matrix and ranked list.

- [ ] **Task 35 — Compare Pearson and Spearman**
  - **Objective:** Check whether the indicator ranking depends on the method.
  - **Requirements:** Calculate Spearman correlations with score; compare with Pearson; explain any change in order.
  - **Skills:** `corr(method="spearman")`
  - **Expected output:** A side-by-side table and interpretation.

- [ ] **Task 36 — Find Related Indicators**
  - **Objective:** Identify indicators that move closely together.
  - **Requirements:** List the three most strongly correlated indicator pairs (excluding score); explain why strongly related indicators make it hard to separate their individual associations with score.
  - **Skills:** NumPy masking, `stack()`
  - **Expected output:** A ranked pair table and explanation.

- [ ] **Task 37 — Standardize Indicators with Z-Scores**
  - **Objective:** Compare countries across indicators on the same scale.
  - **Requirements:** Calculate z-scores for each indicator (state the standard deviation convention); find the countries with the most extreme values.
  - **Skills:** `np.mean()`, `np.std()`, vectorized arithmetic
  - **Expected output:** A z-score table and a list of extreme profiles.

- [ ] **Task 38 — Fit Score Against GDP**
  - **Objective:** Find countries that differ from what GDP alone would suggest.
  - **Requirements:** Fit a straight line of score on GDP with NumPy; calculate each country's residual; list the 10 largest positive and negative residuals.
  - **Skills:** `np.polyfit()`, `np.polyval()`
  - **Expected output:** Fit coefficients and two residual tables.

- [ ] **Task 39 — Check Whether the GDP Relationship Flattens**
  - **Objective:** See whether the association with GDP differs between poorer and richer countries.
  - **Requirements:** Split countries at the GDP median; calculate the score–GDP correlation in each half with sample sizes.
  - **Skills:** Filtering, `corr()`
  - **Expected output:** Two correlations and an interpretation.

- [ ] **Task 40 — Compare Mean and Median by Band**
  - **Objective:** Check whether skewed indicators distort band averages.
  - **Requirements:** For generosity and perceptions of corruption, compare mean and median within each band; note where they differ most.
  - **Skills:** `groupby().agg(["mean", "median"])`
  - **Expected output:** A comparison table.

#### Level 5 — Data Visualization (Tasks 41–50)

> Every chart needs a clear title, labeled axes with units, and must be saved to `figures/` with `dpi=150` and `bbox_inches="tight"`.

- [ ] **Task 41 — Plot the Score Distribution**
  - **Objective:** Show the shape of happiness scores.
  - **Requirements:** Draw a histogram with a density curve; add mean and median lines.
  - **Skills:** `sns.histplot(kde=True)`, `axvline()`
  - **Expected output:** A saved histogram.

- [ ] **Task 42 — Compare the Top and Bottom 10**
  - **Objective:** Show the extremes of the ranking.
  - **Requirements:** Create a two-panel figure with horizontal bars for the top 10 and bottom 10 countries on the same x-axis scale.
  - **Skills:** `plt.subplots(1, 2, sharex=True)`, `ax.barh()`
  - **Expected output:** A saved two-panel figure.

- [ ] **Task 43 — Draw a Correlation Heatmap**
  - **Objective:** Summarize all associations in one chart.
  - **Requirements:** Mask the upper triangle; use a diverging palette centred at zero; show values to two decimals.
  - **Skills:** `sns.heatmap()`, `np.triu()`
  - **Expected output:** A saved heatmap.

- [ ] **Task 44 — Rank Indicator Correlations**
  - **Objective:** Show which indicators are most associated with score.
  - **Requirements:** Draw a sorted bar chart of each indicator's correlation with score; add a reference line at zero.
  - **Skills:** `ax.barh()`, `axvline()`
  - **Expected output:** A saved bar chart.

- [ ] **Task 45 — Plot Score Against GDP**
  - **Objective:** Visualize the main relationship and its exceptions.
  - **Requirements:** Draw a scatter plot with a fitted line; annotate the countries with the largest residuals from Task 38.
  - **Skills:** `sns.regplot()`, `ax.annotate()`
  - **Expected output:** A saved scatter plot.

- [ ] **Task 46 — Plot Score Against Social Support**
  - **Objective:** Show a second key relationship by band.
  - **Requirements:** Draw a scatter plot coloured by happiness band in logical band order.
  - **Skills:** `sns.scatterplot(hue=..., hue_order=...)`
  - **Expected output:** A saved scatter plot.

- [ ] **Task 47 — Compare Scores by GDP Tier**
  - **Objective:** Show the score spread within each GDP tier.
  - **Requirements:** Draw a box plot with individual country points overlaid.
  - **Skills:** `sns.boxplot()`, `sns.stripplot()`
  - **Expected output:** A saved box plot.

- [ ] **Task 48 — Build a Pair Plot**
  - **Objective:** Explore all relationships at once.
  - **Requirements:** Include score and the indicators most related to it; colour by happiness band.
  - **Skills:** `sns.pairplot()`
  - **Expected output:** A saved pair plot.

- [ ] **Task 49 — Compare Happiness and GDP Ranks**
  - **Objective:** Show where the two rankings disagree.
  - **Requirements:** Plot happiness rank against GDP rank; add a diagonal reference line; label the five largest gaps.
  - **Skills:** `ax.scatter()`, `ax.plot()`, `ax.annotate()`
  - **Expected output:** A saved scatter plot.

- [ ] **Task 50 — Plot the Largest Residuals**
  - **Objective:** Show which countries are happier or less happy than GDP suggests.
  - **Requirements:** Draw a diverging horizontal bar chart of the 10 largest positive and 10 largest negative residuals.
  - **Skills:** `ax.barh()`, conditional colours
  - **Expected output:** A saved bar chart.

#### Level 6 — Advanced Analysis and Portfolio Delivery (Tasks 51–60)

- [ ] **Task 51 — Investigate Which Indicators Matter Most**
  - **Objective:** Answer one question with several pieces of evidence.
  - **Requirements:** Combine the correlation, band and top/bottom comparisons; state which indicators are most strongly associated with score; explain why country-level associations do not describe individuals or prove causes.
  - **Skills:** Analytical synthesis
  - **Expected output:** A short written investigation with supporting tables.

- [ ] **Task 52 — Profile Over- and Under-Performers**
  - **Objective:** Describe countries that differ most from the GDP fit.
  - **Requirements:** Compare the median non-GDP indicators of the 10 largest positive residual countries with the 10 largest negative ones.
  - **Skills:** Filtering, `agg()`
  - **Expected output:** A comparison table and short interpretation.

- [ ] **Task 53 — Interpret Perceptions of Corruption Carefully**
  - **Objective:** Analyze an indicator whose direction must be confirmed.
  - **Requirements:** Confirm from the source documentation which direction indicates less corruption; then describe its relationship with score and identify countries that break the overall pattern.
  - **Skills:** `corr()`, filtering, documentation
  - **Expected output:** A verified interpretation and an exceptions table.

- [ ] **Task 54 — Investigate the Generosity Anomaly**
  - **Objective:** Understand why generosity is weakly associated with score.
  - **Requirements:** Identify countries with high generosity but a low score and the reverse; compare their other indicators.
  - **Skills:** `np.percentile()`, filtering
  - **Expected output:** Two tables and a cautious interpretation.

- [ ] **Task 55 — Measure Indicator Balance**
  - **Objective:** Check whether high scores come from strength across many indicators or just a few.
  - **Requirements:** Count how many indicators each country has above the median; compare the count with score and band.
  - **Skills:** Boolean arithmetic, `sum(axis=1)`, `groupby()`
  - **Expected output:** A balance column and summary table.

- [ ] **Task 56 — Test Whether Outliers Change the Conclusions**
  - **Objective:** Check how sensitive the correlation ranking is.
  - **Requirements:** Remove the IQR outliers found in Task 33; recalculate correlations with score; compare the ranking with the original.
  - **Skills:** Filtering, `corr()`
  - **Expected output:** A before-and-after comparison.

- [ ] **Task 57 — Write a Data Validation Function**
  - **Objective:** Make the analysis safe to rerun with another year's data.
  - **Requirements:** Check required columns (explaining that other years use different column names), country uniqueness, missing values and value ranges; print a clear report.
  - **Skills:** Functions, Boolean checks, error messages
  - **Expected output:** A reusable validation function and its report.

- [ ] **Task 58 — Export Results**
  - **Objective:** Save reusable outputs separately from the raw data.
  - **Requirements:** Export the country summary, correlation table and residual table to `outputs/`; reload one file to confirm it saved correctly.
  - **Skills:** `to_csv()`, file paths
  - **Expected output:** CSV files in `outputs/`.

- [ ] **Task 59 — Write the Findings Report**
  - **Objective:** Communicate the most important results.
  - **Requirements:** Write five findings with numbers and caveats; three limitations; three follow-up questions; and a short note on why correlation does not prove causation.
  - **Skills:** Analytical writing
  - **Expected output:** A findings section in Markdown.

- [ ] **Task 60 — Finalize the Project README**
  - **Objective:** Present the project as a portfolio piece.
  - **Requirements:** Embed key charts with relative paths; summarize methodology; include findings, limitations and instructions to run.
  - **Skills:** Markdown, documentation
  - **Expected output:** A complete project README.

#### Optional Extensions (Require Supplementary Data)

These are not part of the 60 tasks.

| Extension | Additional data needed | Join key | What it enables |
|-----------|------------------------|----------|-----------------|
| Regional comparisons | A verified country-to-region mapping | Country name (check unmatched names) | Comparing happiness and indicators by region |
| Changes over time | World Happiness data for other years | Country name (column names differ by year) | Trends in scores and rankings |

### Progress Tracker
| Level | Tasks | Completed | Remaining |
|-------|:-----:|:---------:|:---------:|
| 1. Data Fundamentals | 1–10 | 0 | 10 |
| 2. Data Cleaning and Manipulation | 11–20 | 0 | 10 |
| 3. Aggregation and Feature Engineering | 21–30 | 0 | 10 |
| 4. Statistical and Analytical Methods | 31–40 | 0 | 10 |
| 5. Data Visualization | 41–50 | 0 | 10 |
| 6. Advanced Analysis and Portfolio Delivery | 51–60 | 0 | 10 |
| **Total** | **60** | **0** | **60** |

---

## Roadmap

- [ ] Spotify Tracks: complete tasks 31–60
- [ ] Netflix Titles: complete all 60 tasks
- [ ] Formula 1: complete all 60 tasks
- [ ] International Football: complete all 60 tasks
- [ ] World Happiness 2019: complete all 60 tasks
- [ ] Add charts and findings to each project README as tasks are completed

## Author

**Anbit Bhattarai**
GitHub: [@NerdBhattarai98](https://github.com/NerdBhattarai98)
