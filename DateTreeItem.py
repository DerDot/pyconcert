'''
Created on 01.10.2014

@author: D
'''
from PyQt4.QtGui import QTreeWidgetItem
from PyQt4.QtCore import QLocale, QDate

class DateTreeItem(QTreeWidgetItem):
    '''
    classdocs
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QTreeWidgetItem.__init__(self, parent)
        
    def __lt__(self, otherItem):
        column = self.treeWidget().sortColumn()
        try:
            locale = QLocale()
            mydate = QDate.fromString(self.text(column), locale.dateFormat())
            otherdate = QDate.fromString(otherItem.text(column), locale.dateFormat())
            return mydate < otherdate
        except ValueError:
            return QTreeWidgetItem.__lt__(self, otherItem)
        
