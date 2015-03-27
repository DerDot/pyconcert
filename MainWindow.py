'''
Created on 01.10.2014

@author: D
'''
from PyQt4.QtGui import QMainWindow, QProgressDialog
from PyQt4.QtCore import pyqtSignature, QSettings, Qt, QDate, QLocale

from AboutDialog import AboutDialog
from SettingsDialog import SettingsDialog

from ui.Ui_MainWindow import Ui_MainWindow
from EventCollector import EventCollector
from LastFmAdder import LastFmAdder
from DateTreeItem import DateTreeItem

try:
    import cPickle as pickle
except ImportError:
    import pickle

import webbrowser
import os

def safe_item_text(item, position, text):
    if text is None:
        text = ""
    try:
        item.setText(position, text)
    except TypeError:
        pass

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.event_tree.sortByColumn(1, Qt.AscendingOrder)

        self.settings = QSettings("my corp", "pyconcert")
        self.location = str(self.settings.value("location", "").toString())
        self.music_dirs = str(self.settings.value("music_dirs", "").toString()).split("; ")

        self.event_tree.itemDoubleClicked.connect(self.item_double_clicked)

        self.check_menu_activation()

    def check_menu_activation(self):
        know_dir = bool(self.music_dirs) and bool(self.music_dirs[0])
        have_library = os.path.exists("library.bin")

        self.actionUpdateLibrary.setEnabled(know_dir)
        self.actionUpdateEvents.setEnabled(have_library or know_dir)
        self.actionAddLastFm.setEnabled(have_library)


    @pyqtSignature("")
    def on_actionExit_triggered(self):
        """
        Calls the appropriate method if "Exit" in the menu is clicked.
        """
        self.close()

    @pyqtSignature("")
    def on_actionAbout_triggered(self):
        """
        Calls the appropriate method if "About" in the menu is clicked.
        """
        dialog = AboutDialog()
        dialog.exec_()

    @pyqtSignature("")
    def on_actionSettings_triggered(self):
        """
        Calls the appropriate method if "Settings" in the menu is clicked.
        """
        dialog = SettingsDialog(self.location, self.music_dirs)
        if dialog.exec_():
            location = dialog.location_edit.text()
            self.location = unicode(location) if location else None
            self.settings.setValue("location", location)

            music_dirs = dialog.dir_edit.text()
            self.music_dirs = str(music_dirs).split("; ") if music_dirs else []
            self.settings.setValue("music_dirs", music_dirs)

            self.check_menu_activation()

    def update_data(self, mode):
        self.event_tree.clear()

        self.event_collector = EventCollector(self.music_dirs, self.location)
        self.event_collector.new_artists.connect(self.found_new_artists)
        self.event_collector.getting_events.connect(self.show_getting_events)
        self.event_collector.finished.connect(self.update_finished)
        self.progress_dialog = QProgressDialog("Collecting data...", "", 0, 0, self)
        self.progress_dialog.setWindowTitle("Collecting data")
        self.progress_dialog.setWindowModality(Qt.WindowModal)
        self.progress_dialog.setCancelButton(None)
        self.progress_dialog.show()

        self.event_collector.mode = mode
        self.event_collector.start()

    @pyqtSignature("")
    def on_actionUpdateEvents_triggered(self):
        """
        Calls the appropriate method if "Update Events" in the menu is clicked.
        """
        self.update_data("events")
        self.actionAddLastFm.setEnabled(True)

    @pyqtSignature("")
    def on_actionUpdateLibrary_triggered(self):
        """
        Calls the appropriate method if "Update Library" in the menu is clicked.
        """
        self.update_data("library")
        self.actionAddLastFm.setEnabled(True)

    @pyqtSignature("")
    def on_actionAddLastFm_triggered(self):
        """
        Calls the appropriate method if "Update Library" in the menu is clicked.
        """
        with open("library.bin", "rb") as pklfile:
            artists = pickle.load(pklfile)

        self.lastfm_adder = LastFmAdder(artists)
        self.lastfm_adder.adding_artist.connect(self.add_artist)
        self.lastfm_adder.adding_failed.connect(self.add_artist_failed)
        self.lastfm_adder.finished.connect(self.adding_finished)

        self.progress_dialog = QProgressDialog("Adding artists...", "", 0, len(artists), self)
        self.progress_dialog.setWindowTitle("Adding artists")
        self.progress_dialog.setWindowModality(Qt.WindowModal)
        self.progress_dialog.setCancelButton(None)
        self.progress_dialog.show()

        self.lastfm_adder.start()

    @pyqtSignature("")
    def update_finished(self):
        self.show_events(self.event_collector.events)
        self.progress_dialog.close()

    @pyqtSignature("")
    def adding_finished(self):
        self.progress_dialog.close()

    @pyqtSignature("QTreeWidgetItem")
    def item_double_clicked(self, item):
        webbrowser.open(item.ticket_url)

    def show_events(self, events):
        for event in events:
            item = self.item_for_event(event)
            self.event_tree.addTopLevelItem(item)

        for column in xrange(self.event_tree.columnCount()):
            self.event_tree.resizeColumnToContents(column)

    def item_for_event(self, event):
        item = DateTreeItem()
        safe_item_text(item, 0, " ,".join(event.artists))
        safe_item_text(item, 1, event.date)
        safe_item_text(item, 2, event.time)
        safe_item_text(item, 3, event.venue)
        safe_item_text(item, 4, event.city)
        safe_item_text(item, 5, event.country)
        item.ticket_url = event.ticket_url
        return item

    @pyqtSignature("QString")
    def found_new_artists(self, new_artists):
        self.progress_dialog.setLabelText("Collecting data...\nFound new artitsts: " + new_artists)

    @pyqtSignature("QString")
    def add_artist(self, artist):
        self.progress_dialog.setLabelText("Adding artist: " + artist)
        self.progress_dialog.setValue(self.progress_dialog.value() + 1)

    @pyqtSignature("QString")
    def add_artist_failed(self, artist):
        self.statusBar().showMessage("Adding {} failed.".format(artist))

    @pyqtSignature("")
    def show_getting_events(self):
        self.progress_dialog.setLabelText("Getting events for artists...")
