# Data Analysis Projects

![Python](https://img.shields.io/badge/Python-3-blue) ![Pandas](https://img.shields.io/badge/Pandas-data-green) ![NumPy](https://img.shields.io/badge/NumPy-numeric-lightblue) ![Matplotlib](https://img.shields.io/badge/Matplotlib-charts-orange) ![Seaborn](https://img.shields.io/badge/Seaborn-stats-teal)

A practical data analysis portfolio built with Python. Five real-world datasets are each explored with the same **8-step Exploratory Data Analysis (EDA) workflow**: ask a question, inspect, clean, explore, and report what the data actually supports.

---

## Portfolio Objectives

- Build job-ready skills for junior and associate Data Analyst roles.
- Clean and validate real datasets with documented, justified decisions.
- Use Pandas, NumPy, Matplotlib and Seaborn where each fits best.
- Report findings backed by numbers, with clear limitations and no causal overstatement.

---

## Projects

| # | Project | Dataset focus | Main question |
|---|---------|---------------|---------------|
| 1 | [Spotify Tracks](#project-1-spotify-tracks) | Popularity, genres, artists, audio features | What audio profile do popular tracks and genres share? |
| 2 | [Netflix Titles](#project-2-netflix-titles) | Movies vs TV shows, dates, ratings, countries, genres | How has the catalogue changed over time? |
| 3 | [Formula 1](#project-3-formula-1) | Race results, grid and finishing positions, points | How much does grid position relate to the result? |
| 4 | [International Football](#project-4-international-football) | Match results, teams, tournaments, venues | How large is home advantage, and how has scoring changed? |
| 5 | [World Happiness 2019](#project-5-world-happiness-2019) | Happiness scores and country indicators | Which indicators are most associated with happiness? |

### Progress

| Project | Steps done | Status |
|---------|-----------|--------|
| Spotify Tracks | 0 / 8 | In progress |
| Netflix Titles | 0 / 8 | Not started |
| Formula 1 | 0 / 8 | Not started |
| International Football | 0 / 8 | Not started |
| World Happiness 2019 | 0 / 8 | Not started |

---

## The EDA Workflow (used in every project)

| Step | Name | What I do | Key tools |
|------|------|-----------|-----------|
| 1 | **Define the question** | Write down what I want to learn before touching the data | Markdown notes |
| 2 | **Load and inspect** | Shape, head/tail, dtypes, summary stats, unique counts | `read_csv`, `shape`, `info`, `describe` |
| 3 | **Clean the data** | Fix types, handle missing values, duplicates and impossible values; log every decision | `to_datetime`, `astype`, `isna`, `duplicated` |
| 4 | **Univariate analysis + outliers** | Distribution of each variable; outliers by IQR or z-score | `hist`, `boxplot`, `value_counts`, `np.percentile` |
| 5 | **Bivariate analysis** | Relationships between pairs of variables | `corr`, `groupby`, `crosstab`, scatter plots |
| 6 | **Multivariate analysis** | Interactions between 3+ variables; watch for confounders | heatmap, `pairplot`, colour by a third variable |
| 7 | **Time and segments** | Trends, seasonality, comparisons across groups | `resample`, `rolling`, `pivot_table` |
| 8 | **Summarize findings** | Patterns, data issues, limitations, next steps | Markdown report |

---

## Technologies and Tools

| Tool | Used for |
|------|----------|
| Python 3 | Analysis scripts |
| Pandas | Loading, cleaning, grouping, reshaping, summarizing |
| NumPy | Percentiles, outlier detection, vectorized logic |
| Matplotlib | Custom charts and multi-panel figures |
| Seaborn | Distributions, box plots, heatmaps, pair plots |

---

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

Each project folder follows the same layout:

```
NN-project-name/
├── README.md               # Question, cleaning log, findings, limitations
├── <project>_analysis.py   # Analysis script (one section per EDA step)
├── data/                   # Source CSV
├── figures/                # Saved charts
└── outputs/                # Cleaned data and summary tables
```

---

## Installation and Execution

```bash
git clone https://github.com/NerdBhattarai98/Data_Analysis_Projects.git
cd Data_Analysis_Projects
pip install -r requirements.txt

cd 01-spotify-tracks
python spotify_analysis.py
```

Datasets may not be included because of file size. Download the CSV listed in each project's README and place it in that project's `data/` folder. Replacing a CSV with an updated version and rerunning the script recalculates all results.

---

## Project Standards

- Results are calculated from the current dataset; nothing is hardcoded.
- Every cleaning decision (missing values, duplicates, invalid values) is logged with a reason.
- Rates use sensible denominators and handle division by zero.
- Rankings apply minimum sample sizes so small groups do not dominate.
- Outliers are investigated before they are removed.
- Correlation is never presented as causation.
- Every chart has a title, labelled axes with units, and is saved with `dpi=150, bbox_inches="tight"`.
- Missing files or columns produce clear validation messages.

---

# Project 1: Spotify Tracks

**Question:** What audio profile do popular tracks and genres share, and how do explicit tracks compare?

### Step 1: Define the question
- [ ] Write the main question and 2–3 sub-questions (genre, explicit, duration/tempo/mode)

### Step 2: Load and inspect
- [ ] Preview head, tail and a seeded random sample; report rows and columns
- [ ] Review dtypes and non-null counts
- [ ] Count unique `track_id`, `artists` and `track_genre`

### Step 3: Clean the data
- [ ] Rank columns by missing values (count and %)
- [ ] Separate fully duplicated rows from repeated `track_id` values (the same track can appear in several genres); decide which version later steps use
- [ ] Validate ranges: 0–1 features, popularity 0–100, positive duration, tempo > 0
- [ ] Create `duration_min` from `duration_ms`

### Step 4: Univariate analysis + outliers
- [ ] Popularity histogram with mean and median; check for a spike at zero
- [ ] Six 0–1 audio features as small multiples
- [ ] Skewness of each feature; IQR outliers for duration and z-score outliers for tempo and loudness

### Step 5: Bivariate analysis
- [ ] Pearson and Spearman correlation of each audio feature with popularity
- [ ] Explicit vs non-explicit popularity (box plot with group sizes)
- [ ] Median popularity by genre (min track count) and by artist (min 10 tracks)
- [ ] Energy vs loudness scatter with regression line

### Step 6: Multivariate analysis
- [ ] Correlation heatmap (upper triangle masked)
- [ ] Pair plot on a seeded sample, coloured by popularity category
- [ ] Top 10% vs bottom 10% popularity: compare audio profiles
- [ ] Explicit gap by genre: does it hold within each genre?

### Step 7: Segments
- [ ] Genre summary table: count, median popularity, mean energy, mean danceability
- [ ] Popularity by duration bin and by major/minor mode (note genre as a confounder)
- [ ] Tracks that outperform their own genre median

### Step 8: Summarize findings
- [ ] Five findings with numbers and sample sizes, limitations, follow-up questions
- [ ] Export genre summary and cleaned data to `outputs/`; embed key charts in the README

---

# Project 2: Netflix Titles

**Question:** How has the catalogue changed over time, and does Netflix add recent or older titles?

### Step 1: Define the question
- [ ] Write the main question and sub-questions (growth, release vs addition date, country and genre mix)

### Step 2: Load and inspect
- [ ] Preview head and tail; confirm the 12-column schema
- [ ] Review dtypes; list text columns that really hold dates or numbers
- [ ] Movies vs TV shows split (count and %)

### Step 3: Clean the data
- [ ] Strip whitespace; parse `date_added` with `errors="coerce"` and inspect failures
- [ ] Split `duration` into number and unit (movie minutes vs TV seasons)
- [ ] Fix values stored in the wrong column (duration-like text in `rating`)
- [ ] Missing director, cast, country: keep as missing vs "Unknown", then document the choice
- [ ] Check duplicates (`show_id`, and title + type + year)

### Step 4: Univariate analysis + outliers
- [ ] Release year range; movie duration summary; TV season distribution
- [ ] Rating frequencies
- [ ] IQR outliers in movie duration (check whether they are genuine short films or specials)

### Step 5: Bivariate analysis
- [ ] Release year by type; ratings by type
- [ ] Release-to-addition gap by type (percentiles)
- [ ] Movie duration by release decade (flag decades with few movies)

### Step 6: Multivariate analysis
- [ ] Expand countries and genres to one row per value; compare row counts
- [ ] Top countries using the unique-title denominator (not expanded rows)
- [ ] Common genre pairs; country comparison of type mix, audience group and median movie length

### Step 7: Time and segments
- [ ] Titles added per year by type (note whether the final year is incomplete)
- [ ] Additions heatmap by year and month
- [ ] TV share of additions with a 3-year rolling average
- [ ] Share of recent (gap 0–1 years) vs older (10+ years) additions

### Step 8: Summarize findings
- [ ] Five findings with numbers; explain how missing director, cast and country data affects conclusions
- [ ] Export cleaned data and summaries; embed key charts in the README

---

# Project 3: Formula 1

**Question:** How much does grid position relate to the result, and who gains places consistently?

> The dataset uses IDs only (no driver names, dates or seasons). Core steps work with IDs; names and seasons are optional extensions below.

### Step 1: Define the question
- [ ] Write the main question and sub-questions (grid vs finish, positions gained, classification rates)

### Step 2: Load and inspect
- [ ] Preview head and a seeded sample; confirm the 18-column schema
- [ ] Count unique `resultId`, `raceId`, `driverId`, `constructorId`, `statusId`
- [ ] Field size per race (min, median, max)

### Step 3: Clean the data
- [ ] Find placeholder values in text columns that should be numeric, then replace them with proper missing values
- [ ] Convert position, milliseconds, fastestLap, rank, speed to numeric; confirm no valid values were lost
- [ ] Flag classified results (numeric finishing position exists)
- [ ] Treat grid = 0 as missing in a cleaned grid column; document the decision
- [ ] Parse `fastestLapTime` to seconds; check duplicate driver entries per race

### Step 4: Univariate analysis + outliers
- [ ] Points distribution (handle the many zeros); laps summary
- [ ] Positions gained distribution (classified results only)
- [ ] Fastest-lap speed percentiles and IQR outliers (circuits differ, so be careful)

### Step 5: Bivariate analysis
- [ ] Grid vs finishing position: Pearson and Spearman
- [ ] Win rate by grid position (1–10) with number of starts
- [ ] Positions gained by grid bucket

### Step 6: Multivariate analysis
- [ ] Grid vs finish heatmap (rows normalized)
- [ ] Fastest-lap rank vs finishing position; within-race z-scores of lap time
- [ ] Teammate head-to-head (self-join on race and constructor)

### Step 7: Segments
- [ ] Driver summary: appearances, wins, podiums, points per appearance, median finish, classification rate
- [ ] Constructor summary and non-classified share (minimum results applied)
- [ ] Consistent overtakers compared within the same grid bucket
- [ ] Distinct points awarded for a win (shows scoring systems changed, so career totals are not directly comparable)

### Step 8: Summarize findings
- [ ] Five findings with numbers; state that results from different eras are mixed
- [ ] Export cleaned results and summaries; embed key charts in the README

**Optional extensions** (need extra tables): drivers (names), constructors (team names), races (seasons and dates), status (reasons for not finishing).

---

# Project 4: International Football

**Question:** How large is home advantage, and how has scoring changed over time?

### Step 1: Define the question
- [ ] Write the main question and sub-questions (home advantage, neutral venues, scoring trends, tournaments)

### Step 2: Load and inspect
- [ ] Preview head and tail; review shape and dtypes
- [ ] Count unique home, away and combined teams
- [ ] Top 10 tournaments and their share of matches

### Step 3: Clean the data
- [ ] Parse dates with `errors="coerce"`; report the date range
- [ ] Set aside matches without scores (document why); validate scores as non-negative integers
- [ ] Check duplicates (date + home + away) and team-name formatting (do not merge historical names without a source)
- [ ] Create total goals, goal difference, outcome (home win / draw / away win), year and decade
- [ ] Group tournaments into categories (friendly, World Cup, qualification, continental, other) and review "other"
- [ ] Build the team-perspective table (one row per team per match) and validate it: twice the rows, goals for = goals against, wins = losses

### Step 4: Univariate analysis + outliers
- [ ] Home and away score summary; total goals distribution (one bar per integer)
- [ ] High-scoring thresholds (95th and 99th percentiles) and their share by decade
- [ ] Largest winning margins

### Step 5: Bivariate analysis
- [ ] Outcome shares overall, and neutral vs non-neutral
- [ ] Home advantage by decade (non-neutral only)
- [ ] Draw share and average goals by tournament category (minimum matches)

### Step 6: Multivariate analysis
- [ ] Scoreline heatmap (scores capped at 5+)
- [ ] Hosting effect: home team playing in its own country vs not
- [ ] Goals by decade and tournament category (mark cells with too few matches)

### Step 7: Time and segments
- [ ] Matches and average goals per year with a 10-year rolling average
- [ ] Share of friendlies per decade, so scoring trends are compared fairly
- [ ] Team records and win rates (minimum matches); one team's form with a rolling win rate
- [ ] One head-to-head rivalry with cumulative wins over time

### Step 8: Summarize findings
- [ ] Five findings with numbers; note that more matches are recorded in recent decades
- [ ] Export team-perspective table and summaries; embed key charts in the README

---

# Project 5: World Happiness 2019

**Question:** Which indicators are most associated with happiness, and which countries differ from what GDP suggests?

> Data is at country level. Findings describe countries, not individuals, and show association, not cause.

### Step 1: Define the question
- [ ] Write the main question and sub-questions (indicator associations, GDP vs happiness, over- and under-performers)

### Step 2: Load and inspect
- [ ] Preview head and tail; rename columns to lowercase with underscores (keep the mapping)
- [ ] Review dtypes and describe all numeric columns
- [ ] Top 10 and bottom 10 countries by score

### Step 3: Clean the data
- [ ] Confirm each country appears once; check missing values
- [ ] Investigate exact zeros in indicators and decide how to treat them
- [ ] Validate ranges (score 0–10, indicators non-negative); verify rank order matches score
- [ ] Trim whitespace in country names

### Step 4: Univariate analysis + outliers
- [ ] Score distribution with mean and median lines; score percentiles
- [ ] IQR outliers for score and every indicator
- [ ] Z-scores to find countries with extreme indicator profiles

### Step 5: Bivariate analysis
- [ ] Pearson correlation of each indicator with score, ranked; compare with Spearman
- [ ] Score vs GDP with a fitted line (`np.polyfit`) and residuals per country
- [ ] Score vs social support, coloured by happiness band

### Step 6: Multivariate analysis
- [ ] Correlation heatmap; strongest indicator pairs (explain why related indicators are hard to separate)
- [ ] Pair plot of score and top indicators, coloured by band
- [ ] Count how many indicators each country is above the median on (balance vs a few strong ones)

### Step 7: Segments
- [ ] Happiness bands (quartiles) and GDP tiers (terciles); crosstab of the two
- [ ] Top 10 vs bottom 10: indicator averages, differences and ratios
- [ ] Largest positive and negative GDP residuals: compare their other indicators
- [ ] Check the perceptions-of-corruption direction in the source documentation before interpreting it
- [ ] Re-run correlations without outliers to test how sensitive the ranking is

### Step 8: Summarize findings
- [ ] Five findings with numbers, three limitations, a note on why correlation is not causation
- [ ] Export country summary, correlation table and residuals; embed key charts in the README

**Optional extensions:** region mapping (regional comparisons) and other years of data (trends over time).

---

## Quick Tips I Follow

- Visualize everything: summary statistics can hide a lot (see Anscombe's quartet).
- Keep a log of every cleaning decision so the analysis is reproducible.
- Treat EDA findings as hypotheses, not conclusions.
- Auto-report tools (`ydata-profiling`, `sweetviz`) are for a first pass only; they do not replace Steps 1 and 8.

---

## Skills Demonstrated

- Data inspection, validation and cleaning
- Filtering, grouping, aggregation, reshaping and ranking with Pandas
- Statistical summaries, percentiles, outlier detection and correlation
- Purposeful visualization with Matplotlib and Seaborn
- Clear, evidence-based reporting with stated limitations

---

## Roadmap

- [ ] Spotify Tracks: finish Steps 1–8
- [ ] Netflix Titles
- [ ] Formula 1
- [ ] International Football
- [ ] World Happiness 2019
- [ ] Add charts and findings to each project README as steps are completed

---

## Author

**Anbit Bhattarai**
GitHub: [@NerdBhattarai98](https://github.com/NerdBhattarai98)
