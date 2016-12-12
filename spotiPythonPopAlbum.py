# This is based on spotiPython5h--the final working original grabbing albums and tracks.
# This version will also grab popularity for each album and track.

from urllib2 import urlopen
from json import load

aliceCooper = "3EhbVgyfGd7HkpsagwL9GS"
album_list = []
# create a text file in which to put albums
f = open("alice3.htm", "w")

#function to build URL
def build_artist_album_getting_url(rockstar):
    url = 'http://api.spotify.com'
    # key = '3afe326cd28144238acc48c5cff4c156'
    # url = url + key
    # add artist ID
    url += '/v1/artists/'
    url += rockstar #aliceCooper
    # GET artist's albums
    url += '/albums'
    # add USA market
    url += '?market=US'
    # type is album as opposed to single, etc
    url += '&album_type=album'
    # limit to 50 because geez there's a lot of compilations and stuff in no kind of order
    url += '&limit=50'
    return url
    # print url

# function to send URL and get albums
def call_artist_album_getting_url(url):
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
url = build_artist_album_getting_url(aliceCooper)
call_artist_album_getting_url(url)