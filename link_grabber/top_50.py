import requests
from spotify import authenticate

# Spotify global top 50 playlist: https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF


def query_api(query_url, query_type='song'):

    # Get an authentication token
    token = authenticate()

    # Add authentication token to the request headers
    headers = {
        'Authorization': 'Bearer {token}'.format(token=token)
    }

    # Query the Spotify API for the playlist
    response = requests.get(query_url, headers=headers)
    # Parse the response into a dictionary (JSON)
    response = response.json()

    # Exploring the response object's structure

    # print(response)
    # print(len(response))
    # print(response.keys())
    # print(response['tracks'])
    # print(len(response['tracks']))
    # print(response['tracks'].keys())
    # print(response['tracks']['items'])
    # print(len(response['tracks']['items']))
    # print(len(response['tracks']['items'][0].keys()))
    # print(response['tracks']['items'][0]['track']['external_urls']['spotify'])

    # get links to all of the songs in this playlist

    if query_type == 'playlist':
        song_links = [song['track']['external_urls']['spotify']
                      for song in response['tracks']['items']]

        return song_links

    else:
        return response


if __name__ == '__main__':
    print(get_top_50_links())
