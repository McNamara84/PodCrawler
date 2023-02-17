import requests
import base64

client_id = "cb68bb0f66804f22be4e0ca5c6ca66b5"
client_secret = "1d8cc3a1e3104a359046751297c36b28"

data = {
    "grant_type": "client_credentials"
}

encoded_credentials = base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode()

headers = {
    "Authorization": f"Basic {encoded_credentials}"
}

response = requests.post("https://accounts.spotify.com/api/token", data=data, headers=headers)

access_token = response.json()["access_token"]

print(access_token)