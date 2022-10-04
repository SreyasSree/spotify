from flask import Flask , render_template , request
import requests

app = Flask('Spotify')

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        data = request.form.get('search')
        print(data)


        token = "BQCl_v9wyxxLiAoOeI_IGgdilZabsvi5hhUUd55-B5ENlANf7yNAk7VPhaSRv8LAoaVEEv4JKvwAFu4o99REYg_YQOtLYekWFP9uFmBezkjwH5USY3LU78zFOjuPu8qSbl-x4_Jc8E2Syard4GvIeYB_99E7Meg0E6PpBtGE9PIWR2kLfE8SzllS932llI2K9gGoDOgXfvwvhcSpE2c"

        user_headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        user_params = {
            "limit": 50
        }

        user_profile_response = requests.get(f'https://api.spotify.com/v1/me' , params=user_params, headers=user_headers)
        user_dict = user_profile_response.json()


        user_tracks_response = requests.get(f'https://api.spotify.com/v1/search?q={data}&type=artist', params=user_params, headers=user_headers)

        # print(user_tracks_response.json())

        api_response = user_tracks_response.json()
        user = user_dict['display_name']

        pro_pic = user_dict['images'][0]['url']
        


        result = user_tracks_response.json()

        id = result['artists']['items'][0]['id']
        
        user_track_albums = requests.get(f'https://api.spotify.com/v1/artists/{id}/albums?offset=5' ,params=user_params, headers=user_headers)

        songs = user_track_albums.json()

        # print(songs)
        

        return render_template('index.html' , user = user , pro_pic = pro_pic , songs = songs)

    else:
        return render_template('index.html')
    



app.run(port=8000)
