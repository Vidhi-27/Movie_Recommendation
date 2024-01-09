import streamlit as st
import pickle
import pandas as pd

def recommend(nmovie):
    movie_index = movies[movies['title']==nmovie].index[0]
    distances = similarity[movie_index] #array
    movie_list =sorted(list(enumerate(distances)),reverse =True , key =lambda x:x[1])[1:6]
    recomm = []
    for i in movie_list:
        recomm.append(movies.iloc[i[0]].title)
    return recomm

movies_list = pickle.load(open("C:/Users/vidhi/Untitled Folder/movie_dict.pkl",'rb'))
movies = pd.DataFrame(movies_list)

similarity = pickle.load(open("C:/Users/vidhi/Untitled Folder/similarity.pkl",'rb'))

st.title('Movie Recommender System')

option = st.selectbox(
    'Enter the movie name',
     movies['title'].values)

if st.button('Recommend'):
    recom = recommend(option)
    for i in recom:
        st.write(i)
else:
    st.write('')