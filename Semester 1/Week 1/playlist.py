"""
-------------------
playlist.py
Author: James Bubb
Version 0.1
-------------------
Sends a request for data on the Radio 1 playlist.  Checks what's new and prints out the track title and artist.
"""
import urllib, json # urllib is used to open the connection to Radio 1
playlist_url = "http://www.bbc.co.uk/radio1/playlist.json" # The address of the Radio 1 Playlist data
try:
    playlist_data = json.loads(urllib.urlopen(playlist_url).read())["playlist"] # Get the 'playlist element of that JSON data
except (IOError, ValueError):
    print "Oops! There was a problem retrieving the playlist.  Are you connected to the Internet?"
    playlist_data = None
if playlist_data:
    print "What's new on the BBC Radio 1 Playlist?"
    print "-" * 39
    for playlist in playlist_data: # There are several playlists within the data so go through each one
        for track in playlist_data[playlist]: # Loop through each track on the playlist
            if track['status'] == 'new': # Print out the track info if the track's status is currently 'new'
                print track['title'] + ' by ' + track['artist']
