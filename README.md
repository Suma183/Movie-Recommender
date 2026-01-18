# Movie-Recommender
# 🎬 Movie Recommendation System (Content-Based)

A content-based movie recommender that suggests similar movies based on movie metadata such as **overview, genres, keywords, cast, and director**.  
Users select a movie in the Streamlit app and get the Top 5 recommended movies using cosine similarity.
===============================================================================================
## Features
- Select a movie from a dropdown
- Get **5 similar movie recommendations**
- Fast and simple UI using **Streamlit**
- Uses CountVectorizer + Cosine Similarity for recommendations

===============================================================================================
## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit

==============================================================================================

##  Dataset
Uses the TMDB 5000 Movie Dataset:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

(These are merged using the `title` column.)
================================================================================================
##  How It Works
1. Load and merge TMDB movies + credits data
================================================================================================
3. Create a combined `tags` column from:
   - overview
   - genres
   - keywords
   - top 3 cast
   - director
===============================================================================================
4. Convert tags into vectors using CountVectorizer
==============================================================================================
5. Compute similarity using Cosine Similarity
=============================================================================================
7. Recommend top 5 movies with highest similarity scores
============================================================================================
<img width="1763" height="963" alt="image" src="https://github.com/user-attachments/assets/5a77da10-e8c1-466c-9417-a4efcc095882" />

##  Run Locally

### 1) Clone the repository
```bash
git clone <your-repo-link>
cd <your-repo-folder>
