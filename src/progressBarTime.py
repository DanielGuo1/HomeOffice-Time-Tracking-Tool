import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar, QLabel, QDesktopWidget, QMessageBox
from PyQt5.QtCore import Qt
from datetime import datetime
import Time

now = datetime.now()
str_begin = Time.WorkingTime.getTime(1)
str_now = now.strftime("%H:%M:%S")
str_end = Time.WorkingTime.getTime(2)
str_max = Time.WorkingTime.getTime(3)
FMT = '%H:%M:%S'

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.isOverRegelarbeitszeit = False
        self.isOverMaximalArbeitszeit = False

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # calculate length of progressbar in sec
        # e.g:
        #   End: 16:50:49, Begin: 8:10:49 -> 31200 Seconds Difference
        maxSec = self.calcTime(1)

        # current time in seconds
        nowTime = self.calcTime(2)
        nowSec = nowTime.total_seconds()

        # Progressbar
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(20,60, 350, 30)
        self.pbar.setValue(int(nowSec))
        self.pbar.setMaximum(int(maxSec))
        self.pbar.setFormat(str(nowTime))
        self.pbar.setAlignment(Qt.AlignCenter)
        self.pbar.setFont(QFont('Arial',16))

        # Titel
        self.txt_titel = QLabel(self)
        self.txt_titel.setText("Zeitwächter ")
        self.txt_titel.move(20,15)
        self.txt_titel.setFont(QFont('Arial', 16))
        self.txt_titel.setFixedWidth(350)
        self.txt_titel.setAlignment(Qt.AlignCenter)
        self.txt_titel.setStyleSheet("color: white;")

        # Logo left in Title
        self.txt_logo = QLabel(self)
        self.txt_logo.move(80, 15)
        self.txt_logo.setFixedWidth(350)
        self.txt_logo.setAlignment(Qt.AlignLeft)
        self.pixmap = QPixmap('images\wecker.png')
        self.smaller_pixmap = self.pixmap.scaled(32,32, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.txt_logo.setPixmap(self.smaller_pixmap)

        # "Arbeitsbeginn" String
        self.txt_begin_string = QLabel(self)
        self.txt_begin_string.setText("Arbeitsbeginn: ")
        self.txt_begin_string.move(20,100)
        self.txt_begin_string.setFont(QFont('Arial', 13))
        self.txt_begin_string.setFixedWidth(220)
        self.txt_begin_string.setAlignment(Qt.AlignLeft)
        self.txt_begin_string.setStyleSheet("color: white;")

        # "Arbeitsbeginn" Value
        self.txt_begin_value = QLabel(self)
        self.txt_begin_value.setText(str_begin)
        self.txt_begin_value.move(20, 100)
        self.txt_begin_value.setFont(QFont('Arial', 13))
        self.txt_begin_value.setFixedWidth(350)
        self.txt_begin_value.setAlignment(Qt.AlignRight)
        self.txt_begin_value.setStyleSheet("color: white;")

        # "Arbeitsende" String
        self.txt_end_string = QLabel(self)
        self.txt_end_string.setText("Arbeitsende: ")
        self.txt_end_string.move(20, 125)
        self.txt_end_string.setFont(QFont('Arial', 13))
        self.txt_end_string.setFixedWidth(220)
        self.txt_end_string.setAlignment(Qt.AlignLeft)
        self.txt_end_string.setStyleSheet("color: white;")

        # "Arbeitsende" Value
        self.txt_end_value = QLabel(self)
        self.txt_end_value.setText(str_end)
        self.txt_end_value.move(20, 125)
        self.txt_end_value.setFont(QFont('Arial', 13))
        self.txt_end_value.setFixedWidth(350)
        self.txt_end_value.setAlignment(Qt.AlignRight)
        self.txt_end_value.setStyleSheet("color: white;")

        # "Höchstens" String
        self.txt_end_string = QLabel(self)
        self.txt_end_string.setText("Höchstens: ")
        self.txt_end_string.move(20, 150)
        self.txt_end_string.setFont(QFont('Arial', 13))
        self.txt_end_string.setFixedWidth(220)
        self.txt_end_string.setAlignment(Qt.AlignLeft)
        self.txt_end_string.setStyleSheet("color: white;")

        # "Höchstens" Value
        self.txt_end_value = QLabel(self)
        self.txt_end_value.setText(str_max)
        self.txt_end_value.move(20, 150)
        self.txt_end_value.setFont(QFont('Arial', 13))
        self.txt_end_value.setFixedWidth(350)
        self.txt_end_value.setAlignment(Qt.AlignRight)
        self.txt_end_value.setStyleSheet("color: white;")

        # "Arbeitszeit" String
        self.txt_workingTime_string = QLabel(self)
        self.txt_workingTime_string.setText("Arbeitszeit: ")
        self.txt_workingTime_string.move(20,175)
        self.txt_workingTime_string.setFont(QFont('Arial', 13))
        self.txt_workingTime_string.setFixedWidth(220)
        self.txt_workingTime_string.setAlignment(Qt.AlignLeft)
        self.txt_workingTime_string.setStyleSheet("color: white;")

        # "Arbeitszeit" Value
        self.txt_workingTime_value = QLabel(self)
        self.txt_workingTime_value.setText(str(self.calcTime(2)))
        self.txt_workingTime_value.move(20, 175)
        self.txt_workingTime_value.setFont(QFont('Arial', 13))
        self.txt_workingTime_value.setFixedWidth(350)
        self.txt_workingTime_value.setAlignment(Qt.AlignRight)
        self.txt_workingTime_value.setStyleSheet("color: white;")

        self.setWindowTitle("Arbeitszeit-Tool")
        self.setGeometry(1000, 1000, 380, 195)
        self.show()

        self.timer = QTimer()
        self.timer.timeout.connect(self.handleTimer)
        self.timer.start(1000)


    def locationOnTheScreen(self):
        '''
        this function displays the application on the 
        right bottom corner of the Monitor
        '''
        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()
    
        widget = self.geometry()
        x = ag.width() - widget.width()
        y = 2 * ag.height()-sg.height()-widget.height()
        self.move(x,y)

    def handleTimer(self):
        '''
        This function is responsible for the turn after Working Hours exceeded.
        Workingtime in the progress bar is not counting down to 0 anymore, it will start counting up again.
        e.g.
            -00:02, -00:01, -00:00, +00:01, +00:02
        '''
        regularTimeSec = self.calcTime(1)
        timeOnProgressBar = self.calcTime(3)
        nowInSec = self.calcTime(2).total_seconds()
        overTimeOnProgressBar = self.calcTime(4)
        maxTimeSec = self.calcTime(5)

        if nowInSec <= regularTimeSec:
            self.pbar.setValue(int(nowInSec))
            self.pbar.setFormat(str(timeOnProgressBar))
            self.txt_workingTime_value.setText(str(self.calcTime(2)))


        else:
            # changing the color of process bar
            self.pbar.setStyleSheet("QProgressBar::chunk "
                                    "{"
                                    "background-color: red;"
                                    "}")
            self.pbar.setFormat("+" + str(overTimeOnProgressBar))
            self.txt_workingTime_value.setText(str(self.calcTime(2)))

            if(self.isOverRegelarbeitszeit==False):
                reg_txt = "Die Regelarbeitszeit ist erreicht"
                self.showPopup(reg_txt)
                self.isOverRegelarbeitszeit = True

            # 15min before "Höchstens"
            elif nowInSec >= (maxTimeSec.total_seconds()-15*60):
                if(self.isOverMaximalArbeitszeit==False):
                    max_txt = "Die Maximalzeit ist bald erreicht"
                    self.showPopup(max_txt)
                    self.isOverMaximalArbeitszeit=True


    def calcTime(self,parameter):
        '''
        Calculate the time diffrences between actual time and End time, etc.
        '''
        
        now = datetime.now()
        str_begin = Time.WorkingTime.getTime(1)
        str_now = now.strftime("%H:%M:%S")
        str_end = Time.WorkingTime.getTime(2)
        str_max = Time.WorkingTime.getTime(3)

        if(parameter==1):
            return (datetime.strptime(str_end, FMT) - datetime.strptime(str_begin, FMT)).total_seconds()

        elif(parameter==2):
            return datetime.strptime(str_now, FMT) - datetime.strptime(str_begin, FMT)

        elif (parameter==3):
            return datetime.strptime(str_end, FMT) - datetime.strptime(str_now, FMT)

        elif (parameter==4):
            return datetime.strptime(str_now, FMT) - datetime.strptime(str_end, FMT)

        elif (parameter==5):
            return datetime.strptime(str_max, FMT) - datetime.strptime(str_begin, FMT)

    def showPopup(self,s):
        '''
        A pop up is triggered after working hour exceeds and 15 min before max time 
        '''
        message = "<p style='text-align: center;'><strong>" + s + "</strong></p>" \
                  "<p style='text-align: center;'><img src='images\wecker.png' alt='' width='42' height='42'></p> "

        msg = QMessageBox()
        msg.setText(message)
        msg.setWindowFlags(Qt.FramelessWindowHint)
        msg.setFont(QFont('Arial', 12))
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setStyleSheet(
            "QMessageBox{border-radius: 8px; background-color: grey; border: 1px solid white;} "
            "QLabel{color: white; "
            "margin-right: 15%;}"
            "QPushButton{background-color: white; "
            "border-radius: 8px;"
            "margin-right: 120%;"
            "margin-left: 0%;"
            "color: black;"
            "width: 90%;"
            "height: 25%;}")

        x = msg.exec_()

    def overTime(self,overTimeOnProgressBar):
        '''
        Progressbar will change its color after working hour exceeds
        '''
        self.pbar.setStyleSheet("QProgressBar::chunk "
                                "{"
                                "background-color: red;"
                                "}")
        self.pbar.setFormat("+" + str(overTimeOnProgressBar))
        self.txt_workingTime_value.setText(str(self.calcTime(2)))

def displayWindow():
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.locationOnTheScreen()
    mw.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    displayWindow()


