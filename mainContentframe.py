# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Mar 04 13:13:06 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class BreakPointFrame(QtGui.QFrame):
    def __init__(self,parent,text):
        super(BreakPointFrame,self).__init__(parent)
        self.HourText = QtGui.QLabel(self)
        self.HourText.setText(str(text)+" h")
        self.HourText.setGeometry(QtCore.QRect(2,10,35,10))
        self.HourText.show()
        

class Ui_MainView(object):
    breakpointElements = []
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(846, 408)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.ModusViewBox = QtGui.QComboBox(self.centralWidget)
        self.ModusViewBox.setGeometry(QtCore.QRect(660, 10, 171, 22))
        self.ModusViewBox.setObjectName("ModusViewBox")
        self.BreakpointsFrame = QtGui.QFrame(self.centralWidget)
        self.BreakpointsFrame.setGeometry(QtCore.QRect(10, 50, 641, 221))
        self.BreakpointsFrame.setStyleSheet("Background-Color:rgb(40,40,40);")
        self.BreakpointsFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.BreakpointsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.BreakpointsFrame.setObjectName("BreakpointsFrame")
        #
        self.konstantModeSlider = QtGui.QSlider(self.BreakpointsFrame)
        self.konstantModeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.konstantModeSlider.hide()
        #
        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(660, 39, 171, 231))
        self.groupBox.setObjectName("groupBox")
        self.Userlbl = QtGui.QLabel(self.groupBox)
        self.Userlbl.setGeometry(QtCore.QRect(10, 100, 150, 16))
        self.Userlbl.setObjectName("Userlbl")
        self.TimeLbl = QtGui.QLabel(self.groupBox)
        self.TimeLbl.setGeometry(QtCore.QRect(40, 10, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.TimeLbl.setFont(font)
        self.TimeLbl.setObjectName("TimeLbl")
        self.Sunriselbl = QtGui.QLabel(self.groupBox)
        self.Sunriselbl.setGeometry(QtCore.QRect(10, 120, 150, 16))
        self.Sunriselbl.setObjectName("Sunsriselbl")
        self.Sunsetlbl = QtGui.QLabel(self.groupBox)
        self.Sunsetlbl.setGeometry(QtCore.QRect(10, 140, 150, 16))
        self.Sunsetlbl.setObjectName("Sunsetlbl")
        self.Locationlbl = QtGui.QLabel(self.groupBox)
        self.Locationlbl.setGeometry(QtCore.QRect(10, 160, 150, 16))
        self.Locationlbl.setObjectName("Locationlbl")
        self.ColoTemplbl = QtGui.QLabel(self.groupBox)
        self.ColoTemplbl.setGeometry(QtCore.QRect(10, 180, 170, 16))
        self.ColoTemplbl.setObjectName("ColoTemplbl")
        self.startModusBtn = QtGui.QPushButton(self.centralWidget)
        self.startModusBtn.setGeometry(QtCore.QRect(10, 20, 93, 28))
        self.startModusBtn.setObjectName("startModusBtn")
        self.stopModusBtn = QtGui.QPushButton(self.centralWidget)
        self.stopModusBtn.setGeometry(QtCore.QRect(110, 20, 93, 28))
        self.stopModusBtn.setObjectName("stopModusBtn")
        self.previewModusBtn = QtGui.QPushButton(self.centralWidget)
        self.previewModusBtn.setGeometry(QtCore.QRect(210, 20, 93, 28))
        self.previewModusBtn.setObjectName("previewModusBtn")
        self.setKonstantTempBtn = QtGui.QPushButton(self.centralWidget)
        self.setKonstantTempBtn.setGeometry(QtCore.QRect(550, 20, 101, 28))
        self.setKonstantTempBtn.setObjectName("setKonstantTempBtn")
        self.EditModesBtn = QtGui.QPushButton(self.centralWidget)
        self.EditModesBtn.setGeometry(QtCore.QRect(660, 280, 171, 28))
        self.EditModesBtn.setObjectName("EditModeslbl")
        self.SettingsBtn = QtGui.QPushButton(self.centralWidget)
        self.SettingsBtn.setGeometry(QtCore.QRect(660, 310, 171, 28))
        self.SettingsBtn.setObjectName("Settingslbl")
        self.modusTagsLbl = QtGui.QLabel(self.centralWidget)
        self.modusTagsLbl.setGeometry(QtCore.QRect(10, 280, 300, 16))
        self.modusTagsLbl.setObjectName("modusTagsLbl")
        self.modusDescriptionlbl = QtGui.QLabel(self.centralWidget)
        self.modusDescriptionlbl.setGeometry(QtCore.QRect(10, 300, 500, 16))
        self.modusDescriptionlbl.setObjectName("modusDescriptionlbl")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 846, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionshow_log = QtGui.QAction(MainWindow)
        self.actionshow_log.setObjectName("actionshow_log")
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionshow_log)
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.Userlbl.setText(QtGui.QApplication.translate("MainWindow", "User:", None, QtGui.QApplication.UnicodeUTF8))
        self.TimeLbl.setText(QtGui.QApplication.translate("MainWindow", "TIME", None, QtGui.QApplication.UnicodeUTF8))
        self.Sunriselbl.setText(QtGui.QApplication.translate("MainWindow", "Sunrise:", None, QtGui.QApplication.UnicodeUTF8))
        self.Sunsetlbl.setText(QtGui.QApplication.translate("MainWindow", "Sunset:", None, QtGui.QApplication.UnicodeUTF8))
        self.Locationlbl.setText(QtGui.QApplication.translate("MainWindow", "Location:", None, QtGui.QApplication.UnicodeUTF8))
        self.ColoTemplbl.setText(QtGui.QApplication.translate("MainWindow", "Color Temperature:", None, QtGui.QApplication.UnicodeUTF8))
        self.startModusBtn.setText(QtGui.QApplication.translate("MainWindow", "start", None, QtGui.QApplication.UnicodeUTF8))
        self.stopModusBtn.setText(QtGui.QApplication.translate("MainWindow", "stop", None, QtGui.QApplication.UnicodeUTF8))
        self.previewModusBtn.setText(QtGui.QApplication.translate("MainWindow", "preview", None, QtGui.QApplication.UnicodeUTF8))
        self.setKonstantTempBtn.setText(QtGui.QApplication.translate("MainWindow", "set Konstant", None, QtGui.QApplication.UnicodeUTF8))
        self.EditModesBtn.setText(QtGui.QApplication.translate("MainWindow", "Edit Modes", None, QtGui.QApplication.UnicodeUTF8))
        self.SettingsBtn.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.modusTagsLbl.setText(QtGui.QApplication.translate("MainWindow", "tags:", None, QtGui.QApplication.UnicodeUTF8))
        self.modusDescriptionlbl.setText(QtGui.QApplication.translate("MainWindow", "description:", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionshow_log.setText(QtGui.QApplication.translate("MainWindow", "show log", None, QtGui.QApplication.UnicodeUTF8))

    def calculate_space_for_hour(self,view_width,count):
        return view_width / count

    def createBreakpointElement(self,rect,count,color,hour):
        tmp = BreakPointFrame(self.BreakpointsFrame,hour)
        tmp.setGeometry(rect)
        tmp.setStyleSheet("""background-color:rgb"""+ str(color) +""";""")
        tmp.setObjectName("Breakpoint"+str(count))
        tmp.show()
        self.breakpointElements.append(tmp)

    def deleteBreakpointElements(self):
        for pb in self.breakpointElements:
            pb.setParent(None)

    def visualizeBreakpoints(self,breakpoints):
        self.deleteBreakpointElements()
        count = len(breakpoints)
        view_width = self.BreakpointsFrame.width()
        view_height = self.BreakpointsFrame.height()
        spaceH = self.calculate_space_for_hour(view_width,count)
        for point in range(count):
            size = breakpoints[point].Farbtemperatur/40
            tmpR = QtCore.QRect(int(spaceH/2.0)+spaceH*point,view_height-size,35,size)
            print(tmpR)
            color = breakpoints[point].getTempInColor()
            print(color)
            self.createBreakpointElement(tmpR,point,color,breakpoints[point].Zeit)

    def hide_Breakpoints(self):
        for pb in self.BreakpointsFrame.children():
            try:
                pb.hide()
            except:
                None
                
    def show_Breakpoints(self):
        for pb in self.BreakpointsFrame.children():
            try:
                pb.show()
            except:
                None

    def show_Konstant_Controls(self,minimum,maximum,normal):
        self.hide_Breakpoints()
        self.konstantModeSlider.setGeometry(QtCore.QRect(20, 150, self.BreakpointsFrame.width()-40, 50))
        self.konstantModeSlider.setMaximum(int(maximum))
        self.konstantModeSlider.setMinimum(int(minimum))
        self.konstantModeSlider.setValue(int(normal))
        self.konstantModeSlider.show()
        

    def hide_Konstant_Controls(self):
        self.show_Breakpoints()
        self.konstantModeSlider.hide()
            
        
        

