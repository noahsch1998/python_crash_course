# take user input about an album and make a dictionary

# function to build the dictionary
def make_album(artist, title):
    """Build a dictionary for album info"""
    album = {'artist': artist, 'title': title}
    return album

# while loop to retrieve user input and print dictionary
while True:
    print("\nEnter album info")
    print("Enter 'q' at any time to quit")

    artist = input("Artist: ")

    if artist == 'q':
        break

    title = input("Title: ")

    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)