import tkinter as tk
from tkinter import ttk
import requests
import json
import random

# Your Spotify access token
access_token = 'enter your access token here'

# Spotify API URLs
transfer_playback_url = "https://api.spotify.com/v1/me/player"
playback_url = "https://api.spotify.com/v1/me/player/play"

# List of mood tracks
mood_tracks = [
    ['spotify:track:1a1xLj9W8libnO9PvJf6ao', 'spotify:track:3j9DrRebdWK1jkpOw9FZUy'], # Happy
    ['spotify:track:6WCVnARSUrBrfzod8oAAQ3', 'spotify:track:3sziCSQnR8SbnuQ7N9OE8H'], # Sad
    ['spotify:track:13F10CcLzSeXm0tPfyMrK6', 'spotify:track:4iKGu3xtvm90eBw0EIPWJP']  # Dance
]

# Function to start playback
def start_playback(device_id, track_uri):
    play_data = json.dumps({"uris": [track_uri]})
    response = requests.put(
        playback_url,
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        },
        data=play_data
    )
    if response.status_code == 204:
        print(f"Playback started for track: {track_uri}")
    else:
        print(f"Error: {response.json()}")

# Function to transfer playback to the specified device
def transfer_playback(device_id):
    transfer_data = json.dumps({"device_ids": [device_id], "play": True})
    response = requests.put(
        transfer_playback_url,
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        },
        data=transfer_data
    )
    if response.status_code == 204:
        print("Playback transferred")
    else:
        print(f"Error: {response.json()}")

# Device ID from your device list
device_id = 'enter your device_id'

# Transfer playback to the selected device
transfer_playback(device_id)

# Tkinter GUI setup
root = tk.Tk()
root.title("Spotify Mood Player")
root.geometry("400x300")  # Set the window size

# Mood Slider
mood_label = ttk.Label(root, text="Mood Slider:", font=("Helvetica", 16))
mood_label.pack(pady=10)

mood_slider = ttk.Scale(root, from_=0, to=2, orient='horizontal', length=300)
mood_slider.pack(pady=10)

# Current Song Label
current_song_label = ttk.Label(root, text="Current Song:", font=("Helvetica", 16))
current_song_label.pack(pady=10)

# Play Button
def play_test_track():
    test_track_uri = 'spotify:track:1a1xLj9W8libnO9PvJf6ao' # Test track URI
    start_playback(device_id, test_track_uri)

play_button = ttk.Button(root, text="Play Test Track", command=play_test_track)
play_button.pack(pady=20)

# Function to handle mood slider change
def on_mood_change(event):
    mood_index = int(mood_slider.get())
    tracks = mood_tracks[mood_index]
    random_track = tracks[random.randint(0, len(tracks) - 1)]
    start_playback(device_id, random_track)

# Bind the slider change to the function
mood_slider.bind("<ButtonRelease-1>", on_mood_change)

root.mainloop()
