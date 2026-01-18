import streamlit as st
import pickle

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="centered")

# Load saved data
movies = pickle.load(open("movies.pkl", "rb"))          # DataFrame: movie_id, title, tags
similarity = pickle.load(open("similarity.pkl", "rb"))  # cosine similarity matrix

st.title("🎬 Movie Recommendation System (Content-Based)")
st.write("Select a movie and get 5 similar recommendations.")

selected_movie = st.selectbox("Choose a movie", movies["title"].values)

def recommend(movie_title, n=5):
    idx = movies[movies["title"] == movie_title].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:n+1]
    return [movies.iloc[i[0]]["title"] for i in scores]

if st.button("Recommend"):
    recs = recommend(selected_movie)
    st.subheader("Recommended Movies:")
    for r in recs:
        st.write("✅", r)
