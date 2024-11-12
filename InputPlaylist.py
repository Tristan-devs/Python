def add_song(playlist, title, artist, genre):
    playlist[title] = {'artist': artist, 'genre': genre}
    print(f"Song '{title}' by {artist} (Genre: {genre}) added to the playlist.")

def view_playlist(playlist):
    if not playlist:
        print("The playlist is empty.")
    else:
        for title, details in playlist.items():
            artist = details['artist']
            genre = details['genre']
            print(f"Title: {title}, Artist: {artist}, Genre: {genre}")

def update_song(playlist, title, new_artist=None, new_genre=None):
    if title in playlist:
        if new_artist:
            playlist[title]['artist'] = new_artist
        if new_genre:
            playlist[title]['genre'] = new_genre
        print(f"Song '{title}' has been updated.")
    else:
        print(f"Song '{title}' not found in the playlist.")

def delete_song(playlist, title):
    if title in playlist:
        del playlist[title]
        print(f"Song '{title}' has been removed from the playlist.")
    else:
        print(f"Song '{title}' not found in the playlist.")

def main():
    playlist = {}

    while True:
        print("\nMenu:")
        print("1. View playlist")
        print("2. Add song")
        print("3. Update song")
        print("4. Delete song")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_playlist(playlist)
        elif choice == '2':
            title = input("Enter song title: ")
            artist = input("Enter song artist: ")
            genre = input("Enter song genre: ")
            add_song(playlist, title, artist, genre)
        elif choice == '3':
            title = input("Enter the title of the song to update: ")
            new_artist = input("Enter new artist (or leave blank to keep current): ")
            new_genre = input("Enter new genre (or leave blank to keep current): ")
            update_song(playlist, title, new_artist if new_artist else None, new_genre if new_genre else None)
        elif choice == '4':
            title = input("Enter the title of the song to delete: ")
            delete_song(playlist, title)
        elif choice == '5':
            print("Exiting the playlist manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
