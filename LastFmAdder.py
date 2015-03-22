'''
Created on 08.02.2015

@author: D
'''
from PyQt4.QtCore import pyqtSignal, QThread, QString
import pylast

class LastFmAdder(QThread):
    adding_artist = pyqtSignal(str)
    adding_failed = pyqtSignal(str)
    
    def __init__(self, artists, retries=3):
        QThread.__init__(self)
        self.artists = sorted(artists)
        self.retries = retries
        
        api_key = "949aab11f2971086829016aea57494c1"
        api_secret = "0ef33b5d1af2e693f8789731065a12f5"

        username = "wahlholzer"
        password_hash = pylast.md5("mstr0013")
        
        self.network = pylast.LastFMNetwork(api_key=api_key,
                                            api_secret=api_secret,
                                            username=username,
                                            password_hash=password_hash)
    
        self.library = pylast.Library(user=username,
                                      network=self.network)
    
    def run(self):
        for artist_str in self.artists:
            retry = 0
            while True:
                try:
                    artist = pylast.Artist(artist_str, self.network)
                    self.adding_artist.emit(QString(artist_str))
                    self.library.add_artist(artist)
                    break
                except:
                    if retry < self.retries:
                        retry += 1
                    else:
                        self.adding_failed.emit(QString(artist_str))
                        break