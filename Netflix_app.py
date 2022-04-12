import streamlit as st
import pandas as pd
import pickle



def recommendation(Title):
    movie_index=Netflix_mov[Netflix_mov['Title']==Title].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:21]
    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(Netflix_mov.iloc[i[0]].Title)
    return recommended_movies


Netflix_dict=pickle.load(open('Netflix_dict.pkl','rb'))
Netflix_mov=pd.DataFrame(Netflix_dict)


similarity=pickle.load(open('similarity.pkl','rb'))


st.title('Netflix Movie Recommender')
selected_movie=st.selectbox('Enter or Select a movie you have seen on Netflix before to get recommendations', Netflix_mov['Title'].values)

if st.button('Recommend'):
    names = recommendation(selected_movie)
    for i in names:
        st.write(i)