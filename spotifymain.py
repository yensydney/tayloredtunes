from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
load_dotenv(dotenv_path="/Users/yensydney/Desktop/sbhacks25/.env")
client_id = "8b401bcc929d47698526bd8b1b9caf42"
client_secret = "0eb09d2379ea4a8387c9861176e2eba1"

print("CLIENT_ID:", client_id)
print("CLIENT_SECRET:", client_secret)

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64, 
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers = headers, data = data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_track(token, track_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q=track:{track_name} artist:Taylor Swift&type=track&limit=1"

    query_url = url + query 
    result = get(query_url, headers = headers)
    json_result = json.loads(result.content)
    return json_result['tracks']['items'][0]['external_urls']['spotify']



token = get_token()
print(token)
print(search_for_track(token, "You Belong With Me") )




