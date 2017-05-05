# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modenewedit.ui'
#
# Created: Mon Mar 06 11:50:29 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class MySlider(QtGui.QSlider):
    time = None
    def __init__(self,parent,time):
        super(MySlider,self).__init__(parent)
        self.time = time

class Ui_ModeNewEdit(object):
    breakpointElements = []
    currentBreakpoint = None
    def setupUi(self, ModeNewEdit):
        ModeNewEdit.setObjectName("ModeNewEdit")
        ModeNewEdit.resize(715, 399)
        self.centralWidget = QtGui.QWidget(ModeNewEdit)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(350, 40, 55, 16))
        self.label_2.setObjectName("label_2")
        self.TagsTxt = QtGui.QTextEdit(self.centralWidget)
        self.TagsTxt.setGeometry(QtCore.QRect(390, 50, 261, 51))
        self.TagsTxt.setObjectName("DescriptionTxt")
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(350, 10, 55, 16))
        self.label_4.setObjectName("label_4")
        self.changTypeBox = QtGui.QComboBox(self.centralWidget)
        self.changTypeBox.setGeometry(QtCore.QRect(400, 10, 131, 22))
        self.changTypeBox.setObjectName("changTypeBox")
        self.changTypeBox.addItem("")
        self.changTypeBox.addItem("")
        self.changTypeBox.addItem("")
        self.NameTxt = QtGui.QLineEdit(self.centralWidget)
        self.NameTxt.setGeometry(QtCore.QRect(70, 10, 261, 22))
        self.NameTxt.setObjectName("NameTxt")
        self.DescriptionTxt = QtGui.QTextEdit(self.centralWidget)
        self.DescriptionTxt.setGeometry(QtCore.QRect(70, 50, 261, 51))
        self.DescriptionTxt.setObjectName("DescriptionTxt")
        self.BreakpointsFrame = QtGui.QFrame(self.centralWidget)
        self.BreakpointsFrame.setGeometry(QtCore.QRect(10, 160, 501, 140))
        self.BreakpointsFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.BreakpointsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.BreakpointsFrame.setObjectName("BreakpointsView")
        self.BreakpointsFrame.setStyleSheet("Background-Color:rgb(40,40,40);")
        self.ApplyBtn = QtGui.QPushButton(self.centralWidget)
        self.ApplyBtn.setGeometry(QtCore.QRect(10, 310, 131, 28))
        self.ApplyBtn.setObjectName("CreateBtn")
        self.CancelBtn = QtGui.QPushButton(self.centralWidget)
        self.CancelBtn.setGeometry(QtCore.QRect(150, 310, 131, 28))
        self.CancelBtn.setObjectName("CancelBtn")
        self.ClearAllBtn = QtGui.QPushButton(self.centralWidget)
        self.ClearAllBtn.setGeometry(QtCore.QRect(10, 130, 93, 28))
        self.ClearAllBtn.setObjectName("ClearAllBtn")
        self.RemoveBreakpointBtn = QtGui.QPushButton(self.centralWidget)
        self.RemoveBreakpointBtn.setGeometry(QtCore.QRect(110,130,93,28))
        self.RemoveBreakpointBtn.setObjectName("RemoveBtn")
        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(520, 150, 181, 161))
        self.groupBox.setObjectName("groupBox")
        self.BreakpointTime = QtGui.QTimeEdit(self.groupBox)
        self.BreakpointTime.setGeometry(QtCore.QRect(97, 20, 81, 22))
        self.BreakpointTime.setObjectName("BreakpointTime")
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 55, 16))
        self.label_5.setObjectName("label_5")
        self.addBreakpointBtn = QtGui.QPushButton(self.groupBox)
        self.addBreakpointBtn.setGeometry(QtCore.QRect(0, 130, 181, 28))
        self.addBreakpointBtn.setObjectName("addBreakpointBtn")
        #ModeNewEdit.setCentralWidget(self.centralWidget)
        #self.menuBar = QtGui.QMenuBar(ModeNewEdit)
        #self.menuBar.setGeometry(QtCore.QRect(0, 0, 715, 21))
        #self.menuBar.setObjectName("menuBar")
        #ModeNewEdit.setMenuBar(self.menuBar)
        #self.mainToolBar = QtGui.QToolBar(ModeNewEdit)
        #self.mainToolBar.setObjectName("mainToolBar")
        #ModeNewEdit.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        #self.statusBar = QtGui.QStatusBar(ModeNewEdit)
        #self.statusBar.setObjectName("statusBar")
        #ModeNewEdit.setStatusBar(self.statusBar)

        self.retranslateUi(ModeNewEdit)
        QtCore.QMetaObject.connectSlotsByName(ModeNewEdit)

    def retranslateUi(self, ModeNewEdit):
        #ModeNewEdit.setWindowTitle(QtGui.QApplication.translate("ModeNewEdit", "ModeNewEdit", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ModeNewEdit", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ModeNewEdit", "Tags", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ModeNewEdit", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ModeNewEdit", "Change", None, QtGui.QApplication.UnicodeUTF8))
        self.changTypeBox.setItemText(0, QtGui.QApplication.translate("ModeNewEdit", "smooth", None, QtGui.QApplication.UnicodeUTF8))
        self.changTypeBox.setItemText(1, QtGui.QApplication.translate("ModeNewEdit", "ultra smooth", None, QtGui.QApplication.UnicodeUTF8))
        self.changTypeBox.setItemText(2, QtGui.QApplication.translate("ModeNewEdit", "abbrupt", None, QtGui.QApplication.UnicodeUTF8))
        self.ApplyBtn.setText(QtGui.QApplication.translate("ModeNewEdit", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.CancelBtn.setText(QtGui.QApplication.translate("ModeNewEdit", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.ClearAllBtn.setText(QtGui.QApplication.translate("ModeNewEdit", "Clear All", None, QtGui.QApplication.UnicodeUTF8))
        self.RemoveBreakpointBtn.setText(QtGui.QApplication.translate("ModeNewEdit","Remove",None,QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ModeNewEdit", "Breakpoints", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ModeNewEdit", "Time", None, QtGui.QApplication.UnicodeUTF8))
        self.addBreakpointBtn.setText(QtGui.QApplication.translate("ModeNewEdit", "Add", None, QtGui.QApplication.UnicodeUTF8))


    def showColorTemp(self,tmp):
        print(tmp.rect().left())
        self.one_breakpoint.Farbtemperatur = tmp.value()
        rgb = self.one_breakpoint.getTempInColor()
        self.BreakpointsFrame.setStyleSheet("Background-Color:rgb"+str(rgb)+";")
        self.setCurrentBreakpoint(tmp)

    def restore_Normal_color_Temp_view(self):
        self.BreakpointsFrame.setStyleSheet("Background-Color:rgb(40,40,40);")

    def calculate_space_for_hour(self,view_width,count):
        return view_width / count

    def deleteCurrentBreakpoint(self):
        if(self.currentBreakpoint != None):
            self.currentBreakpoint.setParent(None)
            print("LENGE",len(self.breakpointElements))
            self.breakpointElements.remove(self.currentBreakpoint)
            print("LENGE",len(self.breakpointElements))
            self.currentBreakpoint=None
            self.reorganaizeBreakpoints()

    def reorganaizeBreakpoints(self):
        space = self.calculate_space_for_hour(self.BreakpointsFrame.width(),len(self.breakpointElements))
        for Belement in range(len(self.breakpointElements)):
            self.breakpointElements[Belement].hide()
            self.breakpointElements[Belement].move(space*Belement,self.BreakpointsFrame.height()-self.breakpointElements[Belement].height())
            self.breakpointElements[Belement].show()

    def setCurrentBreakpoint(self,bp):
        if(self.currentBreakpoint!=None):
            self.currentBreakpoint.setStyleSheet("QSlider::handle {Background-Color:gray;border-radius: 4px;}")
        self.currentBreakpoint = bp
        self.currentBreakpoint.setStyleSheet("QSlider::handle {Background-Color:red;border-radius: 4px;}")

    def signalize_current_Breakpoint(self,tmp):
        tmp.setStyleSheet("Background-Color:rgb(255,0,0);")

    def createBreakpointElement(self,rect,count,color,Zeit):
        tmp = MySlider(self.BreakpointsFrame,Zeit)
        tmp.setMinimum(1000)
        tmp.setMaximum(9000)
        tmp.setGeometry(rect)
        tmp.setOrientation(QtCore.Qt.Vertical)
        tmp.setValue(color)
        tmp.Zeit = Zeit
        tmp.setSingleStep(100)
        tmp.setPageStep(100)
        tmp.setObjectName("Breakpoint"+str(count))
        tmp.setTickPosition(QtGui.QSlider.TicksAbove)
        tmp.valueChanged.connect(lambda: self.showColorTemp(tmp))
        tmp.setStyleSheet("QSlider::handle {Background-Color:gray;border-radius: 4px;}")
        tmp.show()
        self.breakpointElements.append(tmp)

    def deleteBreakpointElements(self):
        for pb in self.breakpointElements:
            try:
                pb.setParent(None)
            except:
                None
        self.breakpointElements = []

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

    def visualizeBreakpoints(self,breakpoints):
        if(breakpoints != []):
            self.one_breakpoint = breakpoints[0]
            self.deleteBreakpointElements()
            count = len(breakpoints)
            view_width = self.BreakpointsFrame.width()
            view_height = self.BreakpointsFrame.height()
            spaceH = self.calculate_space_for_hour(view_width,count)
            for point in range(count):
                size = 101
                tmpR = QtCore.QRect(spaceH*point,view_height-size,20,100)
                print(tmpR)
                color = breakpoints[point].Farbtemperatur
                print(color)
                self.createBreakpointElement(tmpR,point,color,breakpoints[point].Zeit)
        else:
            self.deleteBreakpointElements()
        

