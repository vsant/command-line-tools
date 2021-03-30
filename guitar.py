#!/usr/bin/env python3
# 
# Vivek Sant <vsant@hcs.harvard.edu>
# March 7, 2011
# 

from subprocess import Popen, PIPE
from platform import system as getOSType

URL_SEARCH = 'http://www.ultimate-guitar.com/search.php?search_type=title&value='

def usage():
  print("Usage: guitar.py (uses current iTunes track)")

def main(argv):
  if len(argv) != 1 or getOSType() != 'Darwin':
    usage()
    return -1
  song_data = Popen(["osascript", "-e", 'tell application "iTunes"', "-e", 'if player state is playing then', "-e", 'set theTrack to current track', "-e", 'artist of theTrack & "||||||" & name of theTrack', "-e", 'else if selection is not {} then', "-e", 'set theTrack to (item 1 of selection)', "-e", 'artist of theTrack & "||||||" & name of theTrack', "-e", 'end if', "-e", 'end tell'], stdout=PIPE).communicate()[0].strip()
  (song_artist, song_title) = song_data.split("||||||")
  terms = song_artist + " " + song_title
  encoded_search = '+'.join(terms.split(' '))
  url = URL_SEARCH + encoded_search
  Popen(["osascript", "-e", "open location \"" + url + "\""], stdout=PIPE).communicate()[0].strip()

if __name__ == "__main__":
  import sys
  sys.exit(main(sys.argv))
