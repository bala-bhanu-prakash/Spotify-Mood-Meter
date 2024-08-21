# spotify-mood-meter
This feature is built upon Spotify, where you can add an entire song or a portion of it to a custom mood that you create. Once you slide over the mood meter, the respective songs in the list play accordingly.


### Project Overview: Spotify Mood Player with GUI

This project aims to create a mood-based music player using Spotify's Web API, which allows users to play music based on their current mood. The project includes steps for authorization, token exchange, API interaction, and a user-friendly GUI for mood selection and music playback. The code is structured into several steps, each with a specific purpose and outcome.

### Step-by-Step Flow of the Project

#### **1. Authorization URL Generation**

**Objective:**  
To generate a Spotify authorization URL that the user can use to grant the application access to their Spotify account.

**Details:**
- **Explanation:** This step involves creating a URL that will redirect the user to Spotify's authorization page. The URL is constructed using the client ID, redirect URI, and the necessary scopes (permissions) that the application needs.
- **Key Components:**
  - **Client ID:** A unique identifier for your application provided by Spotify when you register your app on their developer dashboard.
  - **Redirect URI:** A URI where Spotify will redirect the user after they grant or deny permission. This URI must match what is registered in your Spotify Developer Dashboard.
  - **Scope:** The permissions your application needs (e.g., access to modify playback state, read playback state, etc.).
- **Outcome:**  
  After this step, you will have a URL that you can visit in a web browser to authenticate your app with Spotify and retrieve an authorization code. This code is essential for obtaining access and refresh tokens in the next step.

**How to Get Necessary Keys:**
1. Register your application on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. After registration, you'll receive a **Client ID** and **Client Secret**.
3. Set up a **Redirect URI** on the dashboard that matches the one in your code.

#### **2. Token Exchange**

**Objective:**  
To exchange the authorization code obtained in the previous step for access and refresh tokens.

**Details:**
- **Explanation:** This step involves sending a POST request to Spotify's token endpoint with the authorization code, client ID, client secret, and redirect URI. The server responds with an access token and a refresh token. The access token is used to make authenticated requests to Spotify's API.
- **Key Components:**
  - **Authorization Code:** The code received after the user grants permission through the authorization URL.
  - **Base64-encoded Client Credentials:** The client ID and client secret are combined and encoded in Base64 to authenticate the request.
- **Outcome:**  
  After completing this step, you will have the access token needed to make API requests (e.g., play a track, get devices) and a refresh token to obtain a new access token when the current one expires.

**How to Use the Tokens:**
- **Access Token:** This token will be used in the `Authorization` header for all subsequent API requests.
- **Refresh Token:** This token can be used to get a new access token without needing to re-authenticate the user.

#### **3. Play Random Song Function**

**Objective:**  
To implement functionality that plays a random song from a predefined list of tracks based on the user's selected mood.

**Details:**
- **Explanation:** This function selects a random track from a list associated with the chosen mood and makes an API request to Spotify to play that track. The list of moods (e.g., Sad, Happy, Dance) is predefined, and each mood has a corresponding list of Spotify track URIs.
- **Key Components:**
  - **Mood Songs Dictionary:** A dictionary that maps mood categories to lists of track URIs.
  - **API Request:** The `PUT` request to the `/me/player/play` endpoint starts playback on the user's active device.
- **Outcome:**  
  After this step, you will have the ability to play a randomly selected song based on a mood chosen by the user. This forms the core functionality of the mood player.

**How to Expand:**
- You can add more moods or update the track lists to include more songs as per your preference.

#### **4. Get Devices Function**

**Objective:**  
To retrieve and display a list of devices where the user can play music.

**Details:**
- **Explanation:** This step involves making a GET request to Spotify's `/me/player/devices` endpoint to get a list of all available playback devices connected to the user's Spotify account. This is necessary to ensure that the playback is initiated on the correct device.
- **Key Components:**
  - **API Request:** The `GET` request retrieves information about the user’s devices, such as device ID, name, type, and whether it’s currently active.
- **Outcome:**  
  After completing this step, you will know the available devices on which you can play music. You can select a device ID to control where the playback occurs.

**Why It's Important:**
- Ensuring playback happens on the desired device is crucial, especially when the user has multiple Spotify-connected devices.

#### **5. GUI Setup with Tkinter**

**Objective:**  
To create a graphical user interface (GUI) that allows users to interact with the Spotify mood player intuitively.

**Details:**
- **Explanation:** In this step, you build a simple Tkinter-based GUI where users can select their mood using a slider. Based on the mood selection, the application plays a corresponding track. The GUI also includes a button to play a test track and a label to display the current song.
- **Key Components:**
  - **Tkinter Widgets:** Labels, sliders, and buttons make the GUI interactive and user-friendly.
  - **Event Binding:** The slider is bound to a function that triggers playback when the user changes the slider position.
- **Outcome:**  
  After this step, you will have a fully functional mood-based music player with a GUI. Users can select a mood and control music playback through an intuitive interface.

**Further Enhancements:**
- You can add more features, such as displaying the current playing song, integrating volume control, or adding more moods.
- The GUI can be further styled and customized to enhance the user experience.

### Final Thoughts

After completing all these steps, you'll have a mood-based music player integrated with Spotify. This player can be controlled via a simple GUI and can randomly select songs based on the user's mood. Each step builds upon the previous one, ensuring that the application has the necessary authorization, can interact with Spotify's API, and provides a user-friendly interface for mood-based playback.
