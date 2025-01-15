class Album:
    def __init__(self, artist, title, songs, year, downloads):
        self.artist = artist
        self.title = title
        self.songs = songs
        self.year = year
        self.downloads = downloads

    def __str__(self):
        return (f"{self.artist}\n"
                f"{self.title}\n"
                f"{self.songs}\n"
                f"{self.year}\n"
                f"{self.downloads}\n")

class MusicLibrary:
    def __init__(self):
        self.albums = []

    def load_file(self, path):
        try:
            with open(path, encoding="utf-8") as file:
                lines = file.readlines()
                for i in range(0, len(lines), 5):
                    artist = lines[i].strip()
                    title = lines[i + 1].strip()
                    songs = int(lines[i + 2].strip())
                    year = int(lines[i + 3].strip())
                    downloads = int(lines[i + 4].strip())
                    album = Album(artist, title, songs, year, downloads)
                    self.albums.append(album)
        except FileNotFoundError:
            print(f"Plik {path} nie został znaleziony.")

    def display_array(self):
        for album in self.albums:
            print(album)

if __name__ == "__main__":
    path = "dane1.txt"
    ml = MusicLibrary()
    ml.load_file(path)
    ml.display_array()