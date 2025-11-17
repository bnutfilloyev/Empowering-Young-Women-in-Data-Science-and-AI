# 📊 Datasets Documentation

## Overview

Bu papkada loyiha uchun kerakli barcha datasets mavjud.

---

## Datasets

### 1. MovieLens 1M Dataset

**Source:** [GroupLens Research](https://grouplens.org/datasets/movielens/1m/)  
**License:** Free for research and education  
**Size:** ~6 MB (compressed)

#### Files:
- `movies.dat` - Movie information
- `ratings.dat` - User ratings (1-5 scale)
- `users.dat` - User demographic information

#### Format (`::`-separated):

**movies.dat:**
```
MovieID::Title::Genres
1::Toy Story (1995)::Animation|Children's|Comedy
```

**ratings.dat:**
```
UserID::MovieID::Rating::Timestamp
1::1193::5::978300760
```

**users.dat:**
```
UserID::Gender::Age::Occupation::Zip-code
1::F::1::10::48067
```

#### Statistics:
- **Users:** 6,040
- **Movies:** 3,706
- **Ratings:** 1,000,209
- **Sparsity:** 95.5% (most users rate few movies)
- **Scale:** 1-5 stars
- **Timeframe:** 2000-2003

---

### 2. TMDB 5000 Movies Dataset

**Source:** [The Movie Database](https://www.themoviedb.org/)  
**License:** CC BY-NC-SA 4.0  
**Size:** ~5 MB

#### Files:
- `tmdb_5000_movies.csv` - Movie metadata
- `tmdb_5000_credits.csv` - Cast and crew information

#### Columns:

**tmdb_5000_movies.csv:**
- `id` - Movie ID
- `title` - Movie title
- `overview` - Plot description
- `genres` - List of genres (JSON)
- `keywords` - Key themes (JSON)
- `budget` - Production budget
- `revenue` - Box office revenue
- `popularity` - Popularity score
- `release_date` - Release date
- `vote_average` - Average rating
- `vote_count` - Number of votes

**tmdb_5000_credits.csv:**
- `movie_id` - Movie ID
- `cast` - Actors (JSON)
- `crew` - Directors, producers, etc. (JSON)

#### Statistics:
- **Movies:** 4,803
- **Languages:** 45+
- **Time Range:** 1916-2017
- **Rich metadata:** Genres, keywords, cast, crew

---

## Download Instructions

### Option 1: Automatic (Recommended)
```bash
cd datasets/
bash download_data.sh
```

### Option 2: Manual

**MovieLens 1M:**
```bash
curl -O http://files.grouplens.org/datasets/movielens/ml-1m.zip
unzip ml-1m.zip
```

**TMDB 5000:**
```bash
# Movies
curl -L -o tmdb_5000_movies.csv https://raw.githubusercontent.com/luoqd/TMDB-5000-Movie-Dataset/master/tmdb_5000_movies.csv

# Credits
curl -L -o tmdb_5000_credits.csv https://raw.githubusercontent.com/luoqd/TMDB-5000-Movie-Dataset/master/tmdb_5000_credits.csv
```

---

## Data Quality

### MovieLens 1M:
- ✅ Clean, well-structured
- ✅ No missing values in key fields
- ✅ Timestamps for temporal analysis
- ⚠️ Old data (2000-2003)
- ⚠️ Limited movie metadata

### TMDB 5000:
- ✅ Rich metadata (genres, keywords, cast)
- ✅ Recent data (up to 2017)
- ✅ Budget/revenue information
- ⚠️ Some missing values
- ⚠️ JSON fields need parsing

---

## Usage in Notebooks

### Notebook 1: Data Exploration
- Load and understand both datasets
- EDA and statistics
- Visualizations

### Notebook 2: Data Preprocessing
- Merge MovieLens + TMDB
- Handle missing values
- Feature engineering

### Notebooks 3-6:
- Use prepared data for modeling

---

## Data Merging Strategy

**Challenge:** MovieLens and TMDB use different IDs

**Solution:**
1. Match by **movie title** and **year**
2. Clean titles (remove special characters)
3. Use fuzzy matching for close matches
4. Keep MovieLens ratings + TMDB metadata

---

## File Structure After Download

```
datasets/
├── download_data.sh              # This script
├── README.md                     # This file
├── ml-1m/                        # MovieLens folder
│   ├── movies.dat
│   ├── ratings.dat
│   ├── users.dat
│   └── README
├── tmdb_5000_movies.csv          # TMDB movies
├── tmdb_5000_credits.csv         # TMDB credits
└── ml-1m.zip                     # Original archive (can delete)
```

---

## Data Privacy & Ethics

### MovieLens:
- ✅ Anonymized user IDs
- ✅ No personally identifiable information
- ✅ Users opted-in to share ratings

### TMDB:
- ✅ Public movie information
- ✅ No user data
- ✅ Properly licensed

**Safe for educational use!** ✅

---

## Citation

If you use these datasets in research/publications:

**MovieLens:**
```
F. Maxwell Harper and Joseph A. Konstan. 2015. 
The MovieLens Datasets: History and Context. 
ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4: 19:1–19:19.
```

**TMDB:**
```
Data provided by The Movie Database (TMDb)
https://www.themoviedb.org/
```

---

## Troubleshooting

### Download fails?
- Check internet connection
- Try manual download links above
- Use VPN if blocked in your country

### Extraction fails?
```bash
# Install unzip (macOS/Linux)
brew install unzip  # macOS
sudo apt install unzip  # Linux
```

### File not found errors?
- Make sure you're in correct directory
- Run `ls` to check files exist
- Check file paths in notebooks

---

## Need Help?

1. Check download_data.sh output for errors
2. Verify files exist: `ls -lh`
3. See Notebook 1 for data loading examples
4. Contact instructor if issues persist

---

**Total Download Size:** ~11 MB  
**Total Extracted Size:** ~25 MB  
**Download Time:** 1-2 minutes (depending on connection)

**Ready!** Start with `notebooks/1_data_exploration.ipynb` 🚀
