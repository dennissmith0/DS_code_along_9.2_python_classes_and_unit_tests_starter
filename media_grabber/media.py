from spotify import get_album, get_track


class Media:
    pass


class Song(Media):
    pass


if __name__ == '__main__':

    # the Media class can be used for any type of media
    # A music album is just one example
    # We could also use this class to represent books, movies, blog posts, etc.
    album = get_album('5BWl0bB1q0TqyFmkBEupZy')

    print(album['id'])
    print(album['name'])
    print(album['release_date'])
    print(album['external_urls']['spotify'])

    #------------------------------------------------------------------------#

    # We can create a child class that represents a more specific type of media
    # for example, a specific song on Spotify.com
    # We want this song to inherit all of the attributes of the parent
    # but also have additional attributes that are specific to the child class.

    track = get_track('75FEaRjZTKLhTrFGsfMUXR')

    print(track['id'])
    print(track['name'])
    print(track['album']['release_date'])
    print(track['external_urls']['spotify'])
    print(track['explicit'])
    print(track['duration_ms'])
    print(track['disc_number'])
    print(track['popularity'])
