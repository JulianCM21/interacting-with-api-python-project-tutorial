import pandas as pd
import seaborn as sns
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt

# load the .env file variables
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

#print(f"Client ID: {client_id}")
#print(f"Client Secret: {client_secret}")

Con = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

#Artist ID:
artist_id = '4q3ewBCX7sLwd24euuV69X' #Bad Bunny

#Obtain Top 10 songs
top_tracks = Con.artist_top_tracks(artist_id)

#Extract name and popularity into a dict list
track_data = []
for track in top_tracks['tracks'][:10]:  # Limit to the top 10 tracks
    track_data.append({
        'Track Name': track['name'],
        'Popularity': track['popularity'],
        'Duration (Minutes)': track['duration_ms'] / 60000  #Convert ms to Minutes
    })
#Convert dictionaries list into a Pandas DataFrame
df_tracks = pd.DataFrame(track_data)

#DataFrame by popularity
df_sorted = df_tracks.sort_values(by='Popularity', ascending=False)

# Display the top 3 tracks
print(df_sorted.head(3))

# Create a scatter plot with seaborn
sns.scatterplot(data=df_tracks, x='Duration (Minutes)', y='Popularity')
plt.title('Duration vs Popularity of Songs')
plt.savefig("duration_vs_popularity_plot.png")
plt.show()