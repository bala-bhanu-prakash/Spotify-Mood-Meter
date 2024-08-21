import urllib.parse

client_id = 'enter your client_id from your spotify developer account'
redirect_uri = 'enter the redirect_uri'  # Ensure this matches the registered URI
scope = 'streaming user-read-playback-state user-modify-playback-state'
auth_url = 'https://accounts.spotify.com/authorize'

params = {
    'client_id': client_id,
    'response_type': 'code',
    'redirect_uri': redirect_uri,
    'scope': scope
}

auth_request = f"{auth_url}?{urllib.parse.urlencode(params)}"
print(auth_request)
