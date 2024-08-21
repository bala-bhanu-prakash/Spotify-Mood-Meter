access_token = 'enter your access_token here'

def get_devices():
    endpoint = 'https://api.spotify.com/v1/me/player/devices'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(endpoint, headers=headers)
    devices = response.json()
    print(f"Response Status Code: {response.status_code}")
    print(f"Response JSON: {devices}")
    return devices

devices = get_devices()
