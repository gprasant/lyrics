import re
from collections import defaultdict
import httplib
import json
import musixmatch
from musixmatch import *

def main():
    stop_file = open('stopwords.txt')
    stop_words = stop_file.read().split("\n")
    lyrics_file = open('lyrics_50cents.txt')
    print lyrics_file.read()
    lyrics_words = re.findall(r'\w+', lyrics_file.read())
    #print lyrics_words
    lyrics_words = [word.lower() for word in lyrics_words]
    words = list(set(lyrics_words) - set(stop_words))
    
    
    
    wordCount = defaultdict(int)
    for word in words:
        wordCount[word] += lyrics_words.count(word)
    
    for key in sorted(wordCount, key=wordCount.__getitem__, reverse=True):
        print key, " : ",  wordCount[key]
   
def parse_musix_url():
#snoop dogg - 106
#bob marley - 140038
#50 cent - 8347
    apikey = 'aea7c70a32c3b8d56a07c99ef9d56ffa'
    artists = musixmatch.ws.artist.albums.get(artist_id=8347, apikey=apikey)
    albums = []
    for album in artists["body"]["album_list"]:
        albums.append(album["album"]["album_id"])

    tracks = []
    for album_id in albums:
        album_tracks = musixmatch.ws.album.tracks.get(album_id=album_id, apikey=apikey)
        for track in album_tracks["body"]["track_list"]:
            tracks.append(track["track"]["track_id"])
    # print tracks
    
    lyrics=[]
    for trackid in tracks:
        lyric = musixmatch.ws.track.lyrics.get(track_id = trackid, apikey=apikey)
        if lyric["header"]["status_code"] == 200:
            print lyric["body"]["lyrics"]["lyrics_body"]
        # lyrics.append(lyric["lyrics_body"])   
    print lyrics
    
if __name__ == "__main__":
    main()
    
    
  