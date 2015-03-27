'''
Created on 01.10.2014

@author: D
'''
from PyQt4.QtGui import QDialog, QFileDialog, QListView, QAbstractItemView, \
                        QTreeView, QRegExpValidator, QMessageBox
from PyQt4.QtCore import pyqtSignature, QRegExp

from ui.Ui_SettingsDialog import Ui_SettingsDialog
import urllib

try:
    import cjson
    parse_json = cjson.decode
except ImportError:
    import json
    parse_json = json.loads

class SettingsDialog(Ui_SettingsDialog, QDialog):
    '''
    classdocs
    '''

    def __init__(self, location=None, music_dirs=None, parent=None):
        '''
        Constructor
        '''
        QDialog.__init__(self, parent)
        self.setupUi(self)

        if location:
            self.location_edit.setText(location)

        if music_dirs:
            self.dir_edit.setText("; ".join(music_dirs))

    @pyqtSignature("")
    def on_ok_button_released(self):
        if self.location_edit.text().count(",") == 1:
            self.accept()
        else:
            QMessageBox.warning(self, "Incorrect location format",
                                "Location has to be CITY, COUNTRY.")

    @pyqtSignature("")
    def on_cancel_button_released(self):
        self.reject()

    def get_multiple_dirs(self, start_dir=""):
        dialog = QFileDialog(directory=start_dir)
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        dialog.setOption(QFileDialog.DontUseNativeDialog, True)

        list_view = dialog.findChild(QListView, "listView")
        if list_view:
            list_view.setSelectionMode(QAbstractItemView.MultiSelection)

        tree_view = dialog.findChild(QTreeView)
        if tree_view:
            tree_view.setSelectionMode(QAbstractItemView.MultiSelection)

        dirs = []
        if dialog.exec_():
            dirs = dialog.selectedFiles()

        return dirs

    @pyqtSignature("")
    def on_dir_button_released(self):
        music_dir = self.get_multiple_dirs(self.dir_edit.text().split(";")[0])
        if music_dir:
            self.dir_edit.setText(music_dir.join("; "))

    @pyqtSignature("")
    def on_location_button_released(self):
        city, country = self.get_location()
        text = self.format_location(city, country)
        self.location_edit.setText(text)

    def format_location(self, city, country):
        if city is not None and country is not None:
            return "{}, {}".format(city, country)
        if city is not None:
            return city
        if country is not None:
            return country

    def get_location(self):
        geo_data = parse_json(urllib.urlopen("http://www.telize.com/geoip").read())
        city = geo_data.get("city")

        if city is None:
            hostip_data = parse_json(urllib.urlopen('http://api.hostip.info/get_json.php').read())
            city = hostip_data.get("city")

        country = geo_data.get("country")

        if country is None:
            country = hostip_data.get("country_name", "")
        return city, country
