import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

CLIENT_ID = "70a9fb89662f4dac8d07321b259eaad7"
CLIENT_SECRET = "4d6710460d764fbbb8d8753dc094d131"

# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_album_cover_url(song_name, artist_name):
    """Fetch album cover URL from Spotify API"""
    try:
        search_query = f"track:{song_name} artist:{artist_name}"
        results = sp.search(q=search_query, type="track")

        if results and results["tracks"]["items"]:
            track = results["tracks"]["items"][0]
            album_cover_url = track["album"]["images"][0]["url"]
            return album_cover_url
        else:
            return "https://i.postimg.cc/0QNxYz4V/social.png"
    except Exception as e:
        print(f"Error fetching album cover: {e}")
        return "https://i.postimg.cc/0QNxYz4V/social.png"

def recommend(song):
    """Generate song recommendations based on similarity"""
    try:
        index = music[music['song'] == song].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        
        recommended_music_names = []
        recommended_music_posters = []
        
        for i in distances[1:6]:
            artist = music.iloc[i[0]].artist
            song_name = music.iloc[i[0]].song
            
            recommended_music_posters.append(get_song_album_cover_url(song_name, artist))
            recommended_music_names.append(song_name)

        return recommended_music_names, recommended_music_posters
    except Exception as e:
        st.error(f"Error generating recommendations: {e}")
        return [], []

# Streamlit UI
st.set_page_config(page_title="Music Recommender System", page_icon="🎵", layout="wide")

st.header('🎵 Music Recommender System')
st.write("Select a song and get 5 similar song recommendations!")

# Load the models
try:
    # Use absolute paths
    import sys
    script_dir = os.path.dirname(os.path.abspath(__file__))
    models_dir = os.path.join(script_dir, '..', 'models')
    models_dir = os.path.abspath(models_dir)
    
    df_path = os.path.join(models_dir, 'df.pkl')
    sim_path = os.path.join(models_dir, 'similarity.pkl')
    
    music = pickle.load(open(df_path, 'rb'))
    similarity = pickle.load(open(sim_path, 'rb'))
    
    music_list = music['song'].values
    selected_song = st.selectbox(
        "Type or select a song from the dropdown",
        music_list
    )

    if st.button('Show Recommendation'):
        with st.spinner('Generating recommendations...'):
            recommended_music_names, recommended_music_posters = recommend(selected_song)
            
            if recommended_music_names:
                st.success('Here are your recommendations!')
                col1, col2, col3, col4, col5 = st.columns(5)
                
                with col1:
                    st.text(recommended_music_names[0])
                    st.image(recommended_music_posters[0])
                with col2:
                    st.text(recommended_music_names[1])
                    st.image(recommended_music_posters[1])
                with col3:
                    st.text(recommended_music_names[2])
                    st.image(recommended_music_posters[2])
                with col4:
                    st.text(recommended_music_names[3])
                    st.image(recommended_music_posters[3])
                with col5:
                    st.text(recommended_music_names[4])
                    st.image(recommended_music_posters[4])
            
except FileNotFoundError:
    st.error("⚠️ Model files not found! Please run the training script first.")
    st.info("Run: `python src/model/train.py` from the project root directory")
except Exception as e:
    st.error(f"Error loading models: {e}")