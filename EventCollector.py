'''
Created on 01.10.2014

@author: D
'''
from ApiCalls import events_for_artists_songkick, events_for_artists_bandsintown

from PyQt4.QtCore import pyqtSignal, QString, QThread
from mutagen.easyid3 import EasyID3
import os

try:
    import cPickle as pickle
except ImportError:
    import pickle

class EventCollector(QThread):
    '''
    classdocs
    '''
    new_artists = pyqtSignal(str)
    getting_events = pyqtSignal()

    def __init__(self, musicdirs, location, api="bandsintown"):
        '''
        Constructor
        '''
        QThread.__init__(self)
        self.musicdirs = musicdirs
        self.location = location
        self.events = None
        self.artists = None
        self.mode = "Library"
        self.api = api

    def run(self):
        self.artists = self.collect_artists()
        self.getting_events.emit()
        if self.api == "songkick":
            self.events = events_for_artists_songkick(self.artists,
                                                      self.location)
        else:
            self.events = events_for_artists_bandsintown(self.artists,
                                                         self.location)

    def get_artists(self, audiopath):
        try:
            id3 = EasyID3(audiopath)
            artists = id3.get("artist", [])
            normalized_artists = [artist.lower().decode() for artist in artists]
            return normalized_artists
        except:
            return []

    def collect_artists(self):
        if os.path.exists("library.bin") and self.mode != "library":
            with open("library.bin", "rb") as pklfile:
                return pickle.load(pklfile)

        all_artists = set()
        for musicdir in self.musicdirs:
            for root, _, files in os.walk(musicdir):
                for audiopath in files:
                    audiopath = os.path.join(root, audiopath)
                    artists = self.get_artists(audiopath)

                    old_size = len(all_artists)
                    all_artists.update(artists)
                    if len(all_artists) > old_size:
                        self.new_artists.emit(QString(" ,".join(artists)))

        with open("library.bin", "wb") as pklfile:
            pickle.dump(all_artists, pklfile, protocol=-1)

        return all_artists
