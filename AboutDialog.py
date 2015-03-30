'''
Created on 01.10.2014

@author: D
'''
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from ui.Ui_AboutDialog import Ui_AboutDialog

class AboutDialog(Ui_AboutDialog, QDialog):
    '''
    classdocs
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QDialog.__init__(self, parent)
        self.setupUi(self)
       
    @pyqtSignature("") 
    def on_ok_button_released(self):
        self.accept()       
