def make_album(artist, name, songs = None):
    """Build an album and return it as a dictionary"""
    album = {'artist': artist, 'name': name}

    if songs:
        album['songs'] = songs

    return album

album = make_album('Eminem', 'Recovery')
print(album)

album = make_album('Kid Cudi', 'Man on the Moon II', 17)
print(album)