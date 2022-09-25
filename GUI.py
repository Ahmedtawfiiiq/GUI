# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from json import encoder
from operator import index
from unicodedata import name
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 100))
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 345, 324))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setMinimumSize(QtCore.QSize(0, 50))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 367, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Siemens"))
        self.pushButton_2.setText(_translate("MainWindow", "Next"))
        self.pushButton.setText(_translate("MainWindow", "Previous"))
        self.label.setText(_translate("MainWindow", "Press Next"))
        self.label_2.setWordWrap(True)
        self.pushButton_2.clicked.connect(self.nextEvent)
        self.pushButton.clicked.connect(self.prevEvent)

    def nextEvent(self):
        global index
        global dataDict
        global nameDict
        index += 1
        if index <= (len(dataDict) - 1):
            self.label.setText(nameDict[index + 1])
            self.label_2.setText(dataDict[index])
        else:
            index = len(dataDict)
            self.label.setText(nameDict[index + 1])
            self.label_2.setText("")
        self.updateDimensions()

    def prevEvent(self):
        global index
        global dataDict
        global nameDict
        index -= 1
        if index >= 0:
            self.label.setText(nameDict[index + 1])
            self.label_2.setText(dataDict[index])
        else:
            index = -1
            self.label.setText(nameDict[index + 1])
            self.label_2.setText("")
        self.updateDimensions()

    def updateDimensions(self):
        self.label.adjustSize()


class FileHandler:
    def __init__(self, path):
        self.path = path

    def openFile(self):
        with open(self.path, 'r', encoding='utf-8') as self.f:
            self.data = self.f.readlines()

    def readFile(self):
        self.sList = []
        
        for line in self.data:
            self.sList.append(str(line.split('\n')[0]))


if __name__ == "__main__":
    #######################################################
    index = -1
    fileObject = FileHandler("output.txt")
    fileObject.openFile()
    fileObject.readFile()
    data = fileObject.sList
    #######################################################
    mapperData = ""
    for line in data[2:10]:
        mapperData = mapperData + line + "\n" 
    #######################################################
    scramblerData = ""
    for line in data[11:19]:
        scramblerData = scramblerData + line + "\n" 
    #######################################################
    modulatorData = ""
    for line in data[21:52]:
        modulatorData = modulatorData + line + "\n" 
    #######################################################
    withCP = ""
    for line in data[53:93]:
        withCP = withCP + line + "\n" 
    #######################################################
    withNoise = ""
    for line in data[94:134]:
        withNoise = withNoise + line + "\n" 
    #######################################################
    withoutCP = ""
    for line in data[135:167]:
        withoutCP = withoutCP + line + "\n" 
    #######################################################
    demodulatorData = ""
    for line in data[168:176]:
        demodulatorData = demodulatorData + line + "\n" 
    #######################################################
    demodulatorData = ""
    for line in data[168:176]:
        demodulatorData = demodulatorData + line + "\n" 
    #######################################################
    descramblerData = ""
    for line in data[177:185]:
        descramblerData = descramblerData + line + "\n" 
    #######################################################
    dataDict = {
        0  : data[0],
        1  : mapperData,
        2  : scramblerData,
        3  : modulatorData,
        4  : withCP,
        5  : withNoise,
        6  : withoutCP,
        7  : demodulatorData,
        8  : descramblerData,
        9  : data[186],
        10 : data[188]
    }
    #######################################################
    nameDict = {
        0 :"Press next",
        1 :"Encoder",     
        2 :"Mapper",      
        3 :"Scrambler",   
        4 :"Modulator",   
        5 :"With Cyclic Prefix",       
        6 :"AWGN Channel",        
        7 :"Without Cyclic Prefix",    
        8 :"Demodulator", 
        9 :"Descrambler", 
        10:"Demapper",    
        11:"Decoder",
        12:"Press previous"     
    }
    #######################################################
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
