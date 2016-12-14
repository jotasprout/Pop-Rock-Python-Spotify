from urllib2 import urlopen
from json import load
import time

date = time.strftime("%b %d, %y")

# Artists I'll work with
aliceCooper = "3EhbVgyfGd7HkpsagwL9GS"
meatLoaf = "7dnB1wSxbYa8CejeVg98hz"
iggy = "33EUXrFKGjpUSGacqEHhU4"
stooges = "4BFMTELQyWJU1SwqcXMBm3"
popwilliamson = "1l8grPt6eiOS4YlzjIs0LF"
rollingStones = "22bE4uQ6baNwSHPVcDxLCe"
acdc = "711MCceyCBcFnzjGY4Q7Un"
bowie = "0oSGxfWSnnOXhD2fKuz2Gy"
tinmachine = "3Hdx4fgVxsfEJLFaYCB6ql"

# create a file in which to put data
f = open("alicePop.htm", "w")

# function to build URL for getting artist's albums
def build_artist_albums_url(rockstar):
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
def get_artist_albums(artistAlbumsURL):
    json_obj = urlopen(artistAlbumsURL)
    artistAlbumsData = load(json_obj)
    # for each artist's album ...
    for item in artistAlbumsData['items']:
        albumURL = build_album_url(str(item['id']))
        get_album(albumURL)

def build_album_url(albumID):
    albumURL = 'http://api.spotify.com'
    albumURL += '/v1/albums/'
    albumURL += albumID
    albumURL += '?market=US'
    return albumURL

# function to send URL and get tracks
def get_album(albumURL):
    json_obj2 = urlopen(albumURL)
    albumData = load(json_obj2)
    # for item in albumData['items']:
    albumID = str(albumData['id'].encode("utf-8"))
    albumName = str(albumData['name'].encode("utf-8"))
    albumPop = str(albumData['popularity'])
    albumReleased = str(albumData['release_date'].encode("utf-8"))
    albumTracksURL = build_albumTracks_url(albumID)
    get_albumTracks(albumTracksURL)

def build_albumTracks_url(albumID):
    albumTracksURL = 'http://api.spotify.com'
    albumTracksURL += '/v1/albums/'
    albumTracksURL += albumID
    albumTracksURL += '/tracks'
    albumTracksURL += '?market=US'
    albumTracksURL += '&limit=100'
    return albumTracksURL

def get_albumTracks(albumTracksURL):
    json_obj3 = urlopen(albumTracksURL)
    albumTracksData = load(json_obj3)
    for item in albumTracksData['items']:
        trackID = str(albumTracksData['id'].encode("utf-8"))
        trackURL = build_track_url(trackID)
        get_track(trackURL)

def build_track_url(trackID):
    trackURL = 'http://api.spotify.com'
    trackURL += '/v1/tracks/'
    trackURL += trackID
    trackURL += '?market=US'
    return trackURL

def get_track(trackURL):
    json_obj4 = urlopen(trackURL)
    trackData = load(json_obj4)
    startTracksTable()
    for item in trackData['items']: 
        trackName = str(trackData['name'].encode("utf-8"))
        trackPop = str(trackData['popularity'])
        tracksRow()
    endTable()

def getAlbumPop(albumData):
    albumPop = str(albumData['popularity'])
    # making each of these it's own function because return ends the process, correct?
    return albumPop

def getAlbumReleaseDate(albumData):
    albumReleased = str(albumData['release_date'])
    return albumReleased

def getAlbumName(albumData):
    albumName = str(albumData['name'])
    return albumName

def getTrackName(trackData):
    trackName = str(trackData['name'])
    return trackName

def getTrackPop(trackData):
    trackPop = str(trackData['popularity'])
    return trackPop

def startWebPage():
    f.write("<!--" + date + "-->" + "\n")
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

# Start Here
startWebPage()
artistAlbumsURL = build_artist_albums_url(aliceCooper)
get_artist_albums(artistAlbumsURL)

finishWebPage()
