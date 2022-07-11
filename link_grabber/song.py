from top_50 import query_api


class Song:
    def __init__(self, name, duration, explicit, popularity, track_number):
        self.name = name
        self.duration = duration
        self.explicit = explicit
        self.popularity = popularity
        self.track_number = track_number

    def __repr__(self):
        return f'| {self.name} |'


class WebSong(Song):
    def __init__(self, name, duration, explicit, popularity, track_number, link):
        super().__init__(name, duration, explicit, popularity, track_number)
        self.link = link

    def open_song(self):
        print("Copy link into address bar to open in browser.")
        return self.link


class AppSong(Song):
    def __init__(self, name, duration, explicit, popularity, track_number, uri):
        super().__init__(name, duration, explicit, popularity, track_number)
        self.uri = uri

    def open_song(self):
        print("Copy URI into address bar to open in app.")
        return self.uri


if __name__ == "__main__":
    top_song_link = query_api(
        'https://api.spotify.com/v1/playlists/37i9dQZEVXbMDoHDwVN2tF', query_type='playlist')[:1][0]
    top_song_id = top_song_link.split('/')[-1]

    top_song = query_api(
        f'https://api.spotify.com/v1/tracks/{top_song_id}', query_type='track')

    # print(top_song)
    # print(len(top_song))
    # print(top_song.keys())
    # This is the URL that we just made the query to
    # print(top_song['href'])
    # This is the URI that will try and open the song in the Spotify App
    # print(top_song['uri'])
    # This is the External URL that will open the song online
    # print(top_song['external_urls']['spotify'])
    # print("name", top_song['name'])
    # print("duration", top_song['duration_ms'])
    # print("explicit", top_song['explicit'])
    # print("popularity", top_song['popularity'])
    # print("track number", top_song['track_number'])

    web_song = WebSong(name=top_song['name'],
                       duration=top_song['duration_ms'],
                       explicit=top_song['explicit'],
                       popularity=top_song['popularity'],
                       track_number=top_song['track_number'],
                       link=top_song['external_urls']['spotify'])

    app_song = AppSong(name=top_song['name'],
                       duration=top_song['duration_ms'],
                       explicit=top_song['explicit'],
                       popularity=top_song['popularity'],
                       track_number=top_song['track_number'],
                       uri=top_song['uri'])

    # print(song.open_song_app())
    # print(song.open_song_web())
    # print(song.name)
    # print(song.duration)
    # print(song.explicit)
    # print(song.popularity)
    # print(song.track_number)

    # print(app_song.open_song())

    # print(web_song.open_song())

    # repr gets inherited
    # print(app_song)
