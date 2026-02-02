import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests


with open('movie.pkl','rb') as file:
    movies,cosine_sim=pickle.load(file)
    
    
def get_recommendation(title, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = movies[movies['title'] == title].index[0]
    
    # Get the pairwise similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort the movies based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the scores of the 10 most similar movies (excluding itself)
    sim_scores = sim_scores[1:11]
    
    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]
    
    # Return the top 10 most similar movies as a DataFrame
    return movies.iloc[movie_indices]  # This should return a DataFrame, not a string

import requests

def fetch_poster(movie_id):
    api_key = "YOUR_TMDB_API_KEY"  # Get free API key from themoviedb.org
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if 'poster_path' in data and data['poster_path']:
            poster_path = data['poster_path']
            full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
            return full_path
        else:
            return "https://via.placeholder.com/300x450?text=No+Poster"
    except:
        return "https://via.placeholder.com/300x450?text=No+Poster"

st.title("Movie Recommentation System")

selected_movie = st.selectbox("Select a Movie", movies['title'].values)

if st.button("Recommend"):
    recommendations =get_recommendation(selected_movie)
    st.write("Top 10 recommended movies:")
    
    #create a 2*5 grid layout
    
    for i in range(0,10,5):
        cols=st.columns(5)
        for col,j in zip(cols,range(i,i+5)):
            if j < len(recommendations):
                movie_title=recommendations.iloc[j]['title']
                movie_id=recommendations.iloc[j]['movie_id']
                poster_url=fetch_poster(movie_id)
                with col:
                    st.image(poster_url,width=130)
                    st.write(movie_title)