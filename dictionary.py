playlist = {}

def add_song(artist, title, genre):
    try:
        title = str(title)
        playlist[title] = {'artist': artist, 'genre': genre}
        print(f"You have added '{title}' by {artist} to the playlist")
    except ValueError:
        print("Please make sure input is text.")
    except Exception as e:
        print(f"An error has occured {e}")

add_song("Juice WRLD", "armed & dangerous", "Rap")
add_song("Lil Uzi Vert", "Chill Bae", "Rap")
add_song("The Weekend", "Timeless", "Rap")

print(50 * "=")

''' This is another way to see if the playlist is empty
def view_playlist(playlist):
    if not playlist:
        print("The playlist is empty.")
    else:
        for title, details in playlist.items():
            artist = details['artist']
            genre = details['genre']
            print(f"Title: {title}, Artist: {artist}, Genre: {genre}")
'''

def view_playlist(playlist): 
    try:  
        next(iter(playlist)) 
        for title, details in playlist.items(): 
            artist = details['artist'] 
            genre = details['genre'] 
            print(f"Title: {title}, Artist: {artist}, Genre: {genre}") 
    except StopIteration: 
        print("The playlist is empty.") 
    except Exception as e: 
        print(f"An error occurred: {e}")


view_playlist(playlist)

print(50 * "=")

#def update_song(title,artist,genre):

def update_song(title, artist = None, genre = None):
    try:
        playlist[title]['artist'] = artist
        print(f"Updated artist for {title} to {artist}")
        playlist[title]['genre'] = genre
        print(f"Updated genre for {title} to {genre}")
    except ValueError:
        print("This song title does not exist.")


'''
def update_song(title, artist = None, genre = None):
    if title in playlist:
        if artist:
            playlist[title]['artist'] = artist
            print(f"Updated artist for {title} to {artist}")
        if genre:
            playlist[title]['genre'] = genre
            print(f"Updated genre for {title} to {genre}")
    else:
        print(f"Song {title} has been removed")
'''
update_song ("Timeless", genre = "Pop")


view_playlist(playlist)

print(50 * "=")

def delete_song(playlist, title):
    if title in playlist:
        del playlist[title]
        return f"Song '{title}' has been removed from the playlist."
    else:
        return f"Song '{title}' not found in the playlist."

print(delete_song(playlist, "Timeless"))

view_playlist(playlist)

print(50 * "=")
