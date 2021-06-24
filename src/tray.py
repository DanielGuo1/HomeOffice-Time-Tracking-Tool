import sys
from PySide2 import QtWidgets, QtGui
import progressBarTime


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    """
    CREATE A SYSTEM TRAY ICON CLASS AND ADD MENU
    """
    def __init__(self, icon, parent=None):

        self.isOpen = True
        self.window = progressBarTime.MainWindow()
        self.window.locationOnTheScreen()
        self.window.hide()

        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip(f'Arbeitszeit Tool')
        menu = QtWidgets.QMenu(parent)
        open_app = menu.addAction("Maximize/Minimize")
        open_app.triggered.connect(self.open_application)
        open_app.setIcon(QtGui.QIcon("images\wecker.png"))

        menu.addSeparator()
        self.setContextMenu(menu)
        self.activated.connect(self.onTrayIconActivated)

    def onTrayIconActivated(self, reason):
        """
        This function will trigger function on click or double click
        :param reason: click or double click
        """
        if reason == self.DoubleClick:
             self.open_application()


    def open_application(self):
        """
        this function maximize and minimize the application
        """
        if(self.isOpen):
            self.window.show()
            self.isOpen = False
        else:
            self.window.hide()
            self.isOpen = True


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("images\wecker.png"), w)
    tray_icon.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()