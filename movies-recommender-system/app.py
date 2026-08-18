import streamlit as st
import pickle
import pandas as pd
import requests
import time

API_KEY = "699f1bc37e9f3e42fb7834d15555f27e"   # Replace with your TMDB API key

# ---------------- Fetch Poster ---------------- #

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    for attempt in range(3):
        try:
            response = requests.get(
                url,
                params={
                    "api_key": API_KEY,
                    "language": "en-US"
                },
                headers={
                    "User-Agent": "Mozilla/5.0",
                    "Connection": "close"
                },
                timeout=20
            )

            response.raise_for_status()

            data = response.json()

            poster_path = data.get("poster_path")

            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"

            print(f"No poster available for Movie ID: {movie_id}")
            return "https://via.placeholder.com/500x750?text=No+Poster"

        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed for Movie ID {movie_id}: {e}")
            time.sleep(1)

    print(f"Failed to fetch poster for Movie ID {movie_id}")
    return "https://via.placeholder.com/500x750?text=Connection+Error"


# ---------------- Load Data ---------------- #

movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))

# ---------------- Streamlit UI ---------------- #

st.title("🎬 Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Choose a movie",
    movies["title"].values
)

# ---------------- Recommendation Function ---------------- #

def recommend(movie):

    movie_index = movies[movies["title"] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for movie in movies_list:

        movie_id = movies.iloc[movie[0]].movie_id
        movie_title = movies.iloc[movie[0]].title

        print(f"Fetching: {movie_title} | TMDB ID: {movie_id}")

        recommended_movies.append(movie_title)
        recommended_posters.append(fetch_poster(movie_id))

        # Small delay to avoid connection resets
        time.sleep(0.3)

    return recommended_movies, recommended_posters


# ---------------- Display Recommendations ---------------- #

if st.button("Recommend"):

    names, posters = recommend(selected_movie_name)

    cols = st.columns(len(names))

    for col, name, poster in zip(cols, names, posters):
        with col:
            st.write(f"**{name}**")
            st.image(
                poster,
                use_container_width=True
            )