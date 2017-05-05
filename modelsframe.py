# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modelsview.ui'
#
# Created: Sun Mar 05 15:30:58 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Models_View(object):
    def setupUi(self, ModelsView):
        ModelsView.setObjectName("ModelsView")
        ModelsView.resize(805, 355)
        self.centralWidget = QtGui.QWidget(ModelsView)
        self.centralWidget.setObjectName("centralWidget")
        self.ModesList = QtGui.QListWidget(self.centralWidget)
        self.ModesList.setGeometry(QtCore.QRect(20, 40, 751, 201))
        self.ModesList.setObjectName("ModesList")
        self.addModeBtn = QtGui.QPushButton(self.centralWidget)
        self.addModeBtn.setGeometry(QtCore.QRect(480, 250, 93, 28))
        self.addModeBtn.setObjectName("addModeBtn")
        self.RemoveModeBtn = QtGui.QPushButton(self.centralWidget)
        self.RemoveModeBtn.setGeometry(QtCore.QRect(580, 250, 93, 28))
        self.RemoveModeBtn.setObjectName("RemoveModeBtn")
        self.EditModeBtn = QtGui.QPushButton(self.centralWidget)
        self.EditModeBtn.setGeometry(QtCore.QRect(680, 250, 93, 28))
        self.EditModeBtn.setObjectName("EditModeBtn")
        self.InheritBtn = QtGui.QPushButton(self.centralWidget)
        self.InheritBtn.setGeometry(QtCore.QRect(380,250,93,28))
        self.InheritBtn.setObjectName("InheritBtn")
        self.SearchModeTxt = QtGui.QLineEdit(self.centralWidget)
        self.SearchModeTxt.setGeometry(QtCore.QRect(20, 10, 571, 22))
        self.SearchModeTxt.setObjectName("SearchModeBtn")
        self.TagsComboBox = QtGui.QComboBox(self.centralWidget)
        self.TagsComboBox.setGeometry(QtCore.QRect(600, 10, 171, 22))
        self.TagsComboBox.setObjectName("TagsComboBox")
        self.BackBtn = QtGui.QPushButton(self.centralWidget)
        self.BackBtn.setGeometry(QtCore.QRect(20, 250, 41, 28))
        self.BackBtn.setObjectName("BackBtn")
        #Ui_Models_View.setCentralWidget(self.centralWidget)
        self.retranslateUi(ModelsView)
        QtCore.QMetaObject.connectSlotsByName(ModelsView)

    def retranslateUi(self, ModelsView):
        ModelsView.setWindowTitle(QtGui.QApplication.translate("ModelsView", "ModelsView", None, QtGui.QApplication.UnicodeUTF8))
        self.addModeBtn.setText(QtGui.QApplication.translate("ModelsView", "Add Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.RemoveModeBtn.setText(QtGui.QApplication.translate("ModelsView", "Remove Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.EditModeBtn.setText(QtGui.QApplication.translate("ModelsView", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.InheritBtn.setText(QtGui.QApplication.translate("ModelsView","Inherit",None, QtGui.QApplication.UnicodeUTF8))
        self.BackBtn.setText(QtGui.QApplication.translate("ModelsView", "<-", None, QtGui.QApplication.UnicodeUTF8))

