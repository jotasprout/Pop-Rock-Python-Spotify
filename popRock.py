from urllib2 import urlopen
from json import load

# Artists I'll work with
aliceCooper = "3EhbVgyfGd7HkpsagwL9GS"

# create a file in which to put data
f = open("alice5.htm", "w")

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
    data = load(json_obj)
    f.write("<html>" + "\n" + "<head></head>" + "\n" + "<body>" + "\n" + "<table>" + "\n")
    # for each album ...
    for item in data['items']:
        album_name = str(item['name'])
        f.write("<tr><td>" + album_name + "</td>")
        # use album id to get full album info  
        url2 = build_album_getting_url(str(item['id']))
        album_pop = str(call_album_getting_url(url2))
        f.write("<td>" + album_pop + "</td></tr>" + "\n")
    f.write("</table>" + "\n" + "</body>" + "\n" + "</html>")

def build_album_getting_url(album):
    url2 = 'http://api.spotify.com'
    url2 += '/v1/albums/'
    url2 += album
    url2 += '?market=US'
    return url2

# function to send URL and get tracks
def call_album_getting_url(url2):
    json_obj2 = urlopen(url2)
    data2 = load(json_obj2)
    album_pop = data2['popularity']
    return album_pop    


# Get albums
artistAlbumsURL = build_artist_albums_getting_url(aliceCooper)
call_artist_albums_getting_url(artistAlbumsURL)