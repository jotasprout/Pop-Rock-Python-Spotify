from urllib2 import urlopen
from json import load

# Artists I'll work with
aliceCooper = "3EhbVgyfGd7HkpsagwL9GS"
meatLoaf = ""
iggy = ""
iggyStooges = ""
stooges = ""
rollingStones = ""

# create a file in which to put data
f = open("alice6.htm", "w")

# function to build URL for getting artist's albums
def build_artist_albums_getting_url(rockstar):
    artistAlbumsURL = 'http://api.spotify.com'
    # key = '3afe326cd28144238acc48c5cff4c156'
    # url = url + key

    artistAlbumsURL += '/v1/artists/'
    # add artist ID
    artistAlbumsURL += rockstar
    # GET artist's albums
    artistAlbumsURL += '/albums'
    # add USA market
    artistAlbumsURL += '?market=US'
    # type is album as opposed to single, etc
    artistAlbumsURL += '&album_type=album'
    # limit to 50 because geez there's a lot of compilations and stuff in no kind of order
    artistAlbumsURL += '&limit=50'
    return artistAlbumsURL

# function to send URL and get artist's albums
def call_artist_albums_getting_url(url):
    json_obj = urlopen(url)
    artistAlbumsData = load(json_obj)
    
    # for each album ...
    for item in artistAlbumsData['items']:
        albumName = str(item['name'])
        f.write("<tr><td>" + albumName + "</td>")
        # use album id to get full album info  
        albumURL = build_album_getting_url(str(item['id']))        
        call_album_getting_url(albumURL))
        albumPop = str(albumData['popularity'])
        f.write("<td>" + albumPop + "</td></tr>" + "\n")
    f.write("</table>" + "\n" + "</body>" + "\n" + "</html>")

def build_album_getting_url(albumID):
    albumURL = 'http://api.spotify.com'
    albumURL += '/v1/albums/'
    albumURL += albumID
    albumURL += '?market=US'
    return albumURL

# function to send URL and get tracks
def call_album_getting_url(albumURL):
    json_obj2 = urlopen(albumURL)
    albumData = load(json_obj2)
    # moved album_pop lines into call_artist_albums loop
    # return albumData?
    # or maybe getAlbumPop function below?
    # I think variables in the loop might be more efficient than the functions

def getAlbumPop(albumData):
    # here albumData would be, for example, albumData
    albumPop = str(albumData['popularity'])
    # making each of these it's own function because return ends the process, correct?
    return albumPop

# And more functions modeled after getAlbumPop so I don't need descriptive comments

def getAlbumReleaseDate(albumData):
    albumReleased = str(albumData['release_date'])
    return albumReleased

def getAlbumName(albumData):
    # I don't think I'll need this one since I'll grab the album name from Artist's Albums or Track info
    # If using Track info, substitute albumData with trackData
    albumName = str(albumData['name'])
    return albumName

def getTrackName(trackData):
    trackName = str(trackData['name'])
    return trackName

def getTrackPop(trackData):
    trackPop = str(trackData['popularity'])
    return trackPop


def build_albumTracks_getting_url(albumID):
    albumTracksURL = 'http://api.spotify.com'
    albumTracksURL += '/v1/albums/'
    albumTracksURL += albumID
    albumTracksURL += '/tracks'
    albumTracksURL += '?market=US'
    albumTracksURL += '&limit=100'
    return albumTracksURL

# function to send URL and get tracks
def call_albumTracks_getting_url(albumTracksURL):
    json_obj3 = urlopen(albumTracksURL)
    albumTracksData = load(json_obj3)
    # see albumData comments
    # open file to insert tracks
    #g = open("alice.htm", "a")
    f.write("<ol>" + "\n")
    # for each track, get track name
    for item in albumTracksData['items']:
        # put track name in file
        f.write("<li>" + str(item['name'].encode("utf-8")) + "</li>" + '\n')       
    f.write("</ol>" + "\n")
    #g.close()

def build_track_getting_url(trackID):
    trackURL = 'http://api.spotify.com'
    # trackURL += '/v1/albums/'
    trackURL += trackID
    # trackURL += '/tracks'
    trackURL += '?market=US'
    return trackURL

# function to send URL and get tracks
def call_track_getting_url(trackURL):
    json_obj4 = urlopen(trackURL)
    trackData = load(json_obj4)
    # see albumData comments

    # open file to insert tracks
    #g = open("alice.htm", "a")
    f.write("<ol>" + "\n")
    # for each track, get track name
    for item in trackData['items']:
        # put track name in file
        f.write("<li>" + str(item['name'].encode("utf-8")) + "</li>" + '\n')       
    f.write("</ol>" + "\n")
    #g.close()

# put these somewhere
# create artistID, artistPop
albumID = str(albumData['id'].encode("utf-8"))
albumName = str(albumData['name'].encode("utf-8"))
albumPop = str(albumData['popularity'].encode("utf-8"))
albumReleased = str(albumData['release_date'].encode("utf-8"))
trackID = str(albumTracksData['id'].encode("utf-8"))
trackAlbumName = str(trackData['album']['name'].encode("utf-8"))
trackName = str(trackData['name'].encode("utf-8"))
trackPop = str(trackData['popularity'].encode("utf-8"))

def startWebPage():
    f.write("<html>" + "\n" + "\n" + "<head></head>" + "\n" + "\n" + "<body>" + "\n" + "\n")

def finishWebPage():
    f.write("\n" + "\n" + "</body>" + "\n" + "\n" + "</html>")

def artistTable():
    f.write("<table>" + "\n" + "<tr><th>" + "Artist" + "</th>" + "<th>" + "Popularity" + "</th>"  + "</tr>" + "\n")
    f.write("<tr><td>" + artistName + "</td>" + "<td>" + artistPop + "</td>"  + "</tr>" + "\n")
    endTable()


def startAlbumsTable():
    f.write("<table>" + "\n" + "<tr><th>" + "Album" + "</th>" + "<th>" + "Released" + "</th>"  + "<th>" + "Popularity" + "</th>"  + "</tr>" + "\n")

def albumsRow():
    f.write("<tr><td>" + albumName + "</td>" + "<td>" + albumReleased + "</td>"  + "<td>" + albumPop + "</td>"  + "</tr>" + "\n")

def startTracksTable():
    f.write("<table>" + "\n" + "<tr><th>" + "Track" + "</th>" + "<th>" + "Album" + "</th>"  + "<th>" + "Popularity" + "</th>"  + "</tr>" + "\n")

def tracksRow():
    f.write("<tr><td>" + albumName + "</td>" + "<td>" + trackName + "</td>"  + "<td>" + trackPop + "</td>"  + "</tr>" + "\n")

def endTable():
    f.write("</table>" + "\n")


# Get albums
artistAlbumsURL = build_artist_albums_getting_url(aliceCooper)
call_artist_albums_getting_url(artistAlbumsURL)