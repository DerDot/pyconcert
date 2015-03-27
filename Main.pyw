#!/usr/bin/python

from PyQt4.QtGui import QApplication, QIcon
from MainWindow import MainWindow
import os

def main():
    import sys
    QApplication.setGraphicsSystem("raster")
    app = QApplication(sys.argv)
    app.setApplicationName('pyconcert')
    app.setOrganizationName("Me Corp.");
    #icon = QIcon(os.path.join("icons", "rss.ico"))
    #app.setWindowIcon(icon)
    #app.setQuitOnLastWindowClosed(False)
    wnd = MainWindow()
    #wnd.setWindowIcon(icon)
    wnd.showMaximized()
    app.exec_()

if __name__ == '__main__':
    main()
