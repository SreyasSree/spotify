import requests
from urllib.parse import urlencode
import base64
import webbrowser
import json

client_id = "713136e0d74344e7b5a874b0af012e99"
client_secret = "ed6a41452f9842d886eb97e6ff0795c0"

# auth_headers = {
#     "client_id": client_id,
#     "response_type": "code",
#     "redirect_uri": "http://localhost:7777/callback",
#     "scope": "user-library-read"
# }

# webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))

code = "AQC7a89JvuA0KRhWnE5eBTZW17jZAePI6EjEJflQfLyz5eG1YRh7aCAB7Qg0pGdCKkjZXVQiexJHYDTbZsn5kYdYczIe6up308Tsa5V5fVFvnkXKKY3uv-JOoRCigpHXKmamDiOtXL5EpRG0fVuebLHiUpQPcXn-qkJvrjrvabyRcSoQ1mk0T7YQXXgjDI7TJOln548"

encoded_credentials = base64.b64encode(client_id.encode() + b':' + client_secret.encode()).decode("utf-8")

token_headers = {
    "Authorization": "Basic " + encoded_credentials,
    "Content-Type": "application/x-www-form-urlencoded"
}

token_data = {
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": "http://localhost:7777/callback"
}

r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)

token = r.text

token = json.loads(token)
print(token)


# token = "BQBf1nfEcja63zaopFe_Wp4Jqkww1dRkSpRIrxH3LP4APNHwrdTKdBb7WWMIcEtDx0vLWQYcfHRt1E5Fdz_QNjdabFZH-r26WzDJ0p4RlNI5XCRiThe8smwk_ZgetxTR-pvdqhWhO1lzLl-swgphbE_zPmY6SahMaeBfYOy54QFI0V0kOavHuc1WZYXhlU8Fo4ItkORE8Cy223x2z7M"

# user_headers = {
#     "Authorization": "Bearer " + token,
#     "Content-Type": "application/json"
# }

# user_params = {
#     "limit": 50
# }

# user_tracks_response = requests.get("https://api.spotify.com/v1/search", params=user_params, headers=user_headers)

# print(user_tracks_response.json())