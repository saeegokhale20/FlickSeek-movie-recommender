# importing the required libraries
import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image


# display of  the web app icon and the web app title on the tab which we open
image = Image.open('movieappbackgroundimage.png')
st.set_page_config(page_title='FlickSeek', page_icon=image, layout="wide")

# to hide the footer and the MainMenu
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden; }
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

#  display of the image of the web app
image = Image.open('movieappbackgroundimage.png')
st.image(image, caption='FIND MOVIES SIMILAR TO YOUR FAVOURITE MOVIES')

# display of the audio
st.markdown('''**If you want hint about how to get the similar movies, you can hear the audio provided!**''')
audio_file = open('audio.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3')


# to obtain the poster of each movie
def obtainposter(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=c4bcb0ee9d3a8c89e2c74e987d9f1690&language=en-US'.format(
        movie_id)
    information = requests.get(url)
    information = information.json()
    poster_path = information['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


# to obtain the status of each movie(whether it is 'Released' or not)
def obtainstatus(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=c4bcb0ee9d3a8c89e2c74e987d9f1690&language=en-US'.format(
        movie_id)
    information = requests.get(url)
    information = information.json()
    status = information['status']
    return status


# to obtain the overview of each movie
def obtainoverview(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=c4bcb0ee9d3a8c89e2c74e987d9f1690&language=en-US'.format(
        movie_id)
    information = requests.get(url)
    information = information.json()
    overview = information['overview']
    return overview


# to obtain the runtime of each movie in minutes
def obtainruntime(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=c4bcb0ee9d3a8c89e2c74e987d9f1690&language=en-US'.format(
        movie_id)
    information = requests.get(url)
    information = information.json()
    runtime = information['runtime']
    return runtime


def obtainoriglanguage(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=c4bcb0ee9d3a8c89e2c74e987d9f1690&language=en-US'.format(
        movie_id)
    information = requests.get(url)
    information = information.json()
    origlanguage = information['original_language']
    return origlanguage


# to recommend the movie
def recommend(movie):
    movie_index = mvs[mvs['title'] == movie].index[0]
    distances = similar[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:9]
    suggest_movies = []
    suggest_movieposters = []
    suggest_moviestatus = []
    suggest_moviesoverview = []
    suggest_movieruntime = []
    suggest_language = []

    for i in movies_list:
        movie_id = mvs.iloc[i[0]].movie_id
        suggest_movies.append(mvs.iloc[i[0]].title)  # calling of the function recommend
        suggest_moviestatus.append(obtainstatus(movie_id))  # calling of the function obtainstatus
        suggest_movieposters.append(obtainposter(movie_id))  # calling of the function obtainposter
        suggest_moviesoverview.append(obtainoverview(movie_id))  # calling of the function obtainoverview
        suggest_movieruntime.append(obtainruntime(movie_id))  # calling of the function obtainruntime
        suggest_language.append(obtainoriglanguage(movie_id))  # calling of the function obtainoriglanguage
    return suggest_movies, suggest_movieposters, suggest_moviestatus, suggest_moviesoverview, suggest_movieruntime, suggest_language


# title of the app
st.markdown('''
# _FlickSeek_''')

# storing the pkl file into variable called 'mvs'
moviediction = pickle.load(open('moviediction.pkl', 'rb'))
mvs = pd.DataFrame(moviediction)

# storing of the pkl
similar = pickle.load(open('similar.pkl', 'rb'))

# diplaying of the selectbox
option = st.selectbox(
    'HEY THERE! WHICH MOVIE DO YOU WANT TO SEARCH ?',
    mvs['title'].values)

# display the recommended movies if 'seek' button is pressed
if st.button('SEEK'):
    st.subheader('More movies that you would love:')
    suggest_movies, suggest_movieposters, suggest_moviestatus, suggest_moviesoverview, suggest_moviesruntime, suggest_language = recommend(
        option)

    # display of the movies in the columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(suggest_movieposters[0])
        st.markdown("""**Status:**""")
        st.text(suggest_moviestatus[0])
        st.markdown("""**Runtime in minutes:**""")
        st.text(suggest_moviesruntime[0])
        st.markdown("""**Original language:**""")
        st.text(suggest_language[0])

    with col2:
        st.image(suggest_movieposters[1])
        st.markdown("""**Status:**""")
        st.text(suggest_moviestatus[1])
        st.markdown("""**Runtime in minutes:**""")
        st.text(suggest_moviesruntime[1])
        st.markdown("""**Original language:**""")
        st.text(suggest_language[1])

    with col3:
        st.image(suggest_movieposters[2])
        st.markdown("""**Status:**""")
        st.text(suggest_moviestatus[2])
        st.markdown("""**Runtime in minutes:**""")
        st.text(suggest_moviesruntime[2])
        st.markdown("""**Original language:**""")
        st.text(suggest_language[2])

    col4, col5, col6 = st.columns(3)

    with col4:
        st.image(suggest_movieposters[3])
        st.markdown("""**Status:**""")
        st.text(suggest_moviestatus[3])
        st.markdown("""**Runtime in minutes:**""")
        st.text(suggest_moviesruntime[3])
        st.markdown("""**Original language:**""")
        st.text(suggest_language[3])

    with col5:
        st.image(suggest_movieposters[4])
        st.markdown("""**Status:**""")
        st.text(suggest_moviestatus[4])
        st.markdown("""**Runtime in minutes:**""")
        st.text(suggest_moviesruntime[4])
        st.markdown("""**Original language:**""")
        st.text(suggest_language[4])

    with col6:
        st.image(suggest_movieposters[5])
        st.markdown("""**Status:**""")
        st.text(suggest_moviestatus[5])
        st.markdown("""**Runtime in minutes:**""")
        st.text(suggest_moviesruntime[5])
        st.markdown("""**Original language:**""")
        st.text(suggest_language[5])

    col7, col8, col9 = st.columns(3)

    with col7:
        st.image(suggest_movieposters[6])
        st.markdown("""**Status:**""")
        st.text(suggest_moviestatus[6])
        st.markdown("""**Runtime in minutes:**""")
        st.text(suggest_moviesruntime[6])
        st.markdown("""**Original language:**""")
        st.text(suggest_language[6])

    with col8:
        st.image(suggest_movieposters[7])
        st.markdown("""**Status:**""")
        st.text(suggest_moviestatus[7])
        st.markdown("""**Runtime in minutes:**""")
        st.text(suggest_moviesruntime[7])
        st.markdown("""**Original language:**""")
        st.text(suggest_language[7])

    with col9:
        st.image(suggest_movieposters[8])
        st.markdown("""**Status:**""")
        st.text(suggest_moviestatus[8])
        st.markdown("""**Runtime in minutes:**""")
        st.text(suggest_moviesruntime[8])
        st.markdown("""**Original language:**""")
        st.text(suggest_language[8])


    # usage of the expander to display
    my_expander = st.expander(
        'Expand me for the overview of the movie you searched and also the overview of the recommended movies')
    with my_expander:
        st.text(suggest_movies[0])
        st.text(suggest_moviesoverview[0])

        st.text(suggest_movies[1])
        st.text(suggest_moviesoverview[1])

        st.text(suggest_movies[2])
        st.text(suggest_moviesoverview[2])

        st.text(suggest_movies[3])
        st.text(suggest_moviesoverview[3])

        st.text(suggest_movies[4])
        st.text(suggest_moviesoverview[4])

        st.text(suggest_movies[5])
        st.text(suggest_moviesoverview[5])

        st.text(suggest_movies[6])
        st.text(suggest_moviesoverview[6])

        st.text(suggest_movies[7])
        st.text(suggest_moviesoverview[7])

        st.text(suggest_movies[8])
        st.text(suggest_moviesoverview[8])







