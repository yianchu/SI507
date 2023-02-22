#########################################
##### Name: Yi-An Chu               #####
##### Uniqname: yianchu             #####
#########################################
import json
import requests
import webbrowser

class Media:

    def __init__(self, title="No Title", author="No Author", release_year = "No Release Year", url = "No URL", json = None):
        if json is None:
            self.title = title
            self.author = author
            self.release_year = release_year
            self.url = url
        else:
            try:
                self.title = json["collectionName"]
            except:
                self.title = title
            
            try:
                self.author = json["artistName"]
            except:
                self.author = author
            
            try:
                self.release_year = json["releaseDate"][:4]
            except:
                self.release_year = release_year

            try:
                self.url = json["collectionViewUrl"]
            except:
                self.url = url


    def info(self):
        return f"{self.title} by {self.author} ({self.release_year})"
    def length(self):
        return 0



class Song(Media):
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", album="No Album", genre="No Genre", track_length=0, json = None):
        if json is None:
            super().__init__(title, author, release_year, url)
            self.album = album
            self.genre = genre
            self.track_length = track_length
        else:
            super().__init__(json = json)
            self.title = json['trackName']
            self.album = json["collectionName"]
            self.genre = json["primaryGenreName"]
            self.track_length = int(json["trackTimeMillis"])

    def info(self):
        return f"{self.title} by {self.author} ({self.release_year}) [{self.genre}]"
    def length(self):
        return round(self.track_length/1000)

class Movie(Media):
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", rating="No Rating", movie_length=0, json = None):
        if json is None:
            super().__init__(title, author, release_year, url)
            self.rating = rating
            self.movie_length = movie_length
        else:
            super().__init__(json = json)
            self.title = json["trackName"]
            self.rating = json["contentAdvisoryRating"]
            self.movie_length = int(json["trackTimeMillis"])

    def info(self):
        return f"{self.title} by {self.author} ({self.release_year}) [{self.rating}]"
    def length(self):
        return round(self.movie_length/60/1000)



# Other classes, functions, etc. should go here




if __name__ == "__main__":
    # your control code for Part 4 (interactive search) should go here
    # data = requests.get('https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/')
    # print(data.text)
##===========part 1/ part 2 ================##
    f = open("sample_json.json","r")
    sample_data = json.loads(f.read())
    f.close()
    # print(sample_data[2]['artistName'])

    media = Media(json = sample_data[2])
    # print(media.info())
    song = Song(json = sample_data[1])
    # print(song.info())
    movie = Movie(json = sample_data[0])
    # print(movie.info())

##===========part 3/ part 4 ================##
    
    term = input('Enter a search term, or "exit" to quit:')
    query = {'term':term}
    # query = {"term":"Beatles"}

    while(term != "exit"):
        itunes_url = 'https://itunes.apple.com/search'
        itunes = requests.get(itunes_url, query)
        itunes_json = itunes.json()['results']
        songs =[]
        movies =[]
        medias = []
        total_num = 0
        for itune in itunes_json:
            if itune['wrapperType'] == 'track':
                if itune['kind'] == 'song':
                    data = Song(json=itune)
                    songs.append(data)
                elif itune['kind'] == 'feature-movie':
                    data = Movie(json=itune)
                    movies.append(data)
            else:
                    data = Media(json=itune)
                    medias.append(data)

        print('SONGS')
        total_num = 1
        for song in songs:
            print(total_num, " ", song.info())
            total_num = total_num + 1
        print('MOVIES')
        for movie in movies:
            print(total_num, " ", movie.info())
            total_num = total_num + 1
        print('OTHER MEDIA')
        for media in medias:
            print(total_num, " ", media.info())
            total_num = total_num + 1

        num = input("Enter a number for more info, or another search term, or \"exit\" to quit: ")
        while(num.isnumeric() and int(num) >= 1 and int(num) <= total_num):
            num = int(num)
            if num > len(songs)+len(movies):
                url = medias[num-len(songs)-len(movies)-1].url
            elif num > len(songs):
                url = movies[num-len(songs)-1].url
            else:
                url = songs[num-1].url
            
            print("Launching")
            print(url)
            print("in web browser")
            webbrowser.open(url)
    print("Bye!")

        



