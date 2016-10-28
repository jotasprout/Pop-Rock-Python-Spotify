from urllib2 import urlopen
from json import load

aliceCooper = "3EhbVgyfGd7HkpsagwL9GS"

# create a text file in which to put albums
f = open("alice.htm", "w")

#function to build URL
def build_album_getting_url(rockstar):
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
def call_album_getting_url(url):
    json_obj = urlopen(url)
    data = load(json_obj)
    
    f.write("<html>" + "\n" + "<head></head>" + "\n" + "<body>" + "\n")
    # for each album ...
    for item in data['items']:
        # put album name in file
        f.write("<h2>" + str(item['name']) + "</h2>" + '\n')
        # ... build track-getting URL with album ID
        url2 = build_track_getting_url(str(item['id']))
        # ... use it to get tracks
        call_track_getting_url(url2)
    f.write("</body></html>")
    f.close()


def build_track_getting_url(album):
    url2 = 'http://api.spotify.com'
    url2 += '/v1/albums/'
    url2 += album
    url2 += '/tracks'
    url2 += '?market=US'
    url2 += '&limit=20'
    return url2

# function to send URL and get tracks
def call_track_getting_url(url2):
    json_obj2 = urlopen(url2)
    data2 = load(json_obj2)
    # open file to insert tracks
    #g = open("alice.htm", "a")
    f.write("<ol>" + "\n")
    # for each track, get track name
    for item in data2['items']:
        # put track name in file
        f.write("<li>" + str(item['name'].encode("utf-8")) + "</li>" + '\n')       
    f.write("</ol>" + "\n")
    #g.close()

# Get albums
url = build_album_getting_url(aliceCooper)
call_album_getting_url(url)
