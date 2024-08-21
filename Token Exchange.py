import requests
import base64

client_id = '***************'
client_secret = 'enter your client_secret from your developer account'
redirect_uri = '*************'  # Ensure this matches the registered URI
authorization_code = 'enter the authorization_code'
# Encode client_id and client_secret in Base64
auth_str = f'{client_id}:{client_secret}'
b64_auth_str = base64.b64encode(auth_str.encode()).decode()

headers = {
    'Authorization': f'Basic {b64_auth_str}',
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
    'grant_type': 'authorization_code',
    'code': authorization_code,
    'redirect_uri': redirect_uri
}

response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
tokens = response.json()
access_token = tokens.get('access_token')
refresh_token = tokens.get('refresh_token')

print('Access Token:', access_token)
print('Refresh Token:', refresh_token)
