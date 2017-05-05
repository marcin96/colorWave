# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helpwindow.ui'
#
# Created: Sat Mar 11 15:39:31 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import xml.etree.ElementTree as ET
from xml.dom import minidom
import sys

class Ui_HelpWindow(object):
    def setupUi(self, HelpWindow):
        HelpWindow.setObjectName("HelpWindow")
        HelpWindow.resize(652, 400)
        self.centralWidget = QtGui.QWidget(HelpWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 210, 631, 181))
        self.groupBox.setObjectName("groupBox")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 621, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 611, 121))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtGui.QComboBox(self.centralWidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 631, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.listWidget = QtGui.QListWidget(self.centralWidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 631, 161))
        self.listWidget.setObjectName("listWidget")
        HelpWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(HelpWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 652, 26))
        self.menuBar.setObjectName("menuBar")
        HelpWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(HelpWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        HelpWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(HelpWindow)
        self.statusBar.setObjectName("statusBar")
        HelpWindow.setStatusBar(self.statusBar)

        self.retranslateUi(HelpWindow)
        QtCore.QMetaObject.connectSlotsByName(HelpWindow)

    def retranslateUi(self, HelpWindow):
        HelpWindow.setWindowTitle(QtGui.QApplication.translate("HelpWindow", "HelpWindow - colorWave", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("HelpWindow", "Problem", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("HelpWindow", "Title:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("HelpWindow", "Solution:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("HelpWindow", "Frequently asked questions", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("HelpWindow", "Known problems and their solutions", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("HelpWindow", "internal Bugs", None, QtGui.QApplication.UnicodeUTF8))

class HelpItem(object):
    title = None
    solution = None
    def __init__(self,title,solution):
        self.title = title
        self.solution = solution

class HelpReader():
    def __init__(self,helpfile):
        self.helpfile = helpfile

    def readHelpItems(self,sectionNode):
        items = []
        for item in sectionNode.findall("helpitem"):
            items.append(HelpItem(item.get("name"),item.text))
        return items

    def loadSections(self):
        sections = []
        tree = ET.parse(self.helpfile)
        root = tree.getroot()
        for section in root.findall('section'):
            sections.append(self.readHelpItems(section))
        print(len(sections))
        return sections
            

class HelpView(QtGui.QMainWindow):
    help_sections = []

    def getSoluctionFromText(self,text):
        for item in self.help_sections[self.ui.comboBox.currentIndex()]:
            if(item.title == text):
                return item.solution
        return None

    def change_section(self):
        self.show_section(self.ui.comboBox.currentIndex())

    def show_item(self):
        try:
            self.ui.label.setText("Title: "+str(self.ui.listWidget.currentItem().text()))
            self.ui.label_2.setText("Solution: "+str(self.getSoluctionFromText(self.ui.listWidget.currentItem().text())))
        except AttributeError:
            None

    def show_section(self,index):
        self.ui.listWidget.clear()
        for i in self.help_sections[index]:
            self.ui.listWidget.addItem(i.title)
        
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.ui = Ui_HelpWindow()
        self.ui.setupUi(self)
        self.help_sections.extend(HelpReader("help.xml").loadSections())
        self.ui.comboBox.currentIndexChanged.connect(self.change_section)
        self.ui.listWidget.currentTextChanged.connect(self.show_item)
        self.show_section(0)
        
def show():
    mySW = HelpView()
    mySW.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    app = QtGui.QApplication(None)
    show()
