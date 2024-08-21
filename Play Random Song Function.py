import requests
import random

mood_songs = {
    "Sad": [
        "spotify:track:6WCVnARSUrBrfzod8oAAQ3",  # Track 1
        "spotify:track:3sziCSQnR8SbnuQ7N9OE8H"   # Track 2
    ],
    "Happy": [
        "spotify:track:1a1xLj9W8libnO9PvJf6ao",  # Track 1
        "spotify:track:3j9DrRebdWK1jkpOw9FZUy"   # Track 2
    ],
    "Dance": [
        "spotify:track:13F10CcLzSeXm0tPfyMrK6",  # Track 1
        "spotify:track:4iKGu3xtvm90eBw0EIPWJP"   # Track 2
    ]
}

access_token = 'BQAnumFQOucbTHTYQJGV6ncBhL3EmYGfcyP7WA-5w3AF0ymEuGA_wSkDAyoj_2wrhpdIV8xmMixd_jtGvjHwie0X_id1Ka99BxnPY9inApass2ioCPAIUDZkSOyzkuv66J3_uONiCGcy02IWNxNLiI8sL_wnF6_4NPbGEdZOdgFDBxbbjNzuZ7ARBVz5jm0Sr9-oPeF100FNdLfqVKo1XzleASY'

def play_random_song(selected_mood):
    # Choose a random song from the selected mood
    song_uri = random.choice(mood_songs[selected_mood])
    
    # Define the endpoint for playing a track
    endpoint = 'https://api.spotify.com/v1/me/player/play'
    
    # Define the request headers
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    # Define the request body
    body = {
        'uris': [song_uri]
    }
    
    # Make the API request
    response = requests.put(endpoint, headers=headers, json=body)
    
    if response.status_code == 204:
        print(f"Playing {selected_mood} song: {song_uri}")
    else:
        print(f"Failed to play song: {response.status_code}")
        print(response.json())
