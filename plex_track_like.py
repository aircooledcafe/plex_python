from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer
from plexapi.server import Playlist
import re

account = MyPlexAccount()

plex = PlexServer()

sample_key = '/playlists/20684'
complete_sample_title = ['Crap_From_Haydays','working','starred','sliked']
sample_title = ['90sAlternative']
def add_rating(track):
    track_object = plex.fetchItem(track)
    track_object.rate(rating=10.0)

def get_playlist(server):
    print(f"{'Title':<20}Key")
    for playlist in server.playlists():
        title = playlist.title
        key = playlist.key
        print(f"{title:<20}{key}")

# item = plex.fetchItem(19830)
# rated_item = plex.fetchItem(18927)

# print(item.userRating)
# print(rated_item.userRating)

# item.rate(rating=10.0)

# updated_item = plex.fetchItem(19830)

# print(updated_item.userRating)

# get_playlist(plex)

for playlist in plex.playlists():
    for dst_title in complete_sample_title:    
        title = playlist.title
        if title == dst_title:
            print("Title,Key")
            for track in playlist.items():
                track_title = track.title
                track_key = re.search('[0-9]+', track.key).group(0)
                print(f"{track_title},{track_key}")
                # add_rating(int(track_key))

