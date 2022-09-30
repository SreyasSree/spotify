from flask import Flask , render_template , request
import requests

app = Flask('Spotify')

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        data = request.form.get('search')
        print(data)


        token = "BQCim8510xqFPPUt6qIYsphAY33xf_1COesUBFJnYTE-OKGNG9B4l6TDjZnZhx2-9dNRGKsJmAcbzH_PGK1qnB2tOR3GkPzq4OFycW8ARm-8pVSHGe16ML5UJEHN31_vuW8AMKEzZyt4_2x0OkZbn6B7tkkSyOoQf0PQP5Osp-G5oZsYuDMs6DK7ECz7sU1Iqn6dviExTiszTOgxiKo"

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
