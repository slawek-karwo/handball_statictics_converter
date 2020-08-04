# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stats_generator_gui.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(782, 283)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 10, 731, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_Input_File = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Input_File.setObjectName(u"pushButton_Input_File")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Input_File.sizePolicy().hasHeightForWidth())
        self.pushButton_Input_File.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Aharoni")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Input_File.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_Input_File)

        self.label_Input_File = QLabel(self.horizontalLayoutWidget)
        self.label_Input_File.setObjectName(u"label_Input_File")
        self.label_Input_File.setMinimumSize(QSize(600, 0))

        self.horizontalLayout.addWidget(self.label_Input_File)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(30, 50, 731, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_Output_Folder = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_Output_Folder.setObjectName(u"pushButton_Output_Folder")
        sizePolicy.setHeightForWidth(self.pushButton_Output_Folder.sizePolicy().hasHeightForWidth())
        self.pushButton_Output_Folder.setSizePolicy(sizePolicy)
        self.pushButton_Output_Folder.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton_Output_Folder)

        self.label_Output_Folder = QLabel(self.horizontalLayoutWidget_2)
        self.label_Output_Folder.setObjectName(u"label_Output_Folder")
        self.label_Output_Folder.setMinimumSize(QSize(600, 0))

        self.horizontalLayout_2.addWidget(self.label_Output_Folder)

        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(30, 90, 731, 61))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.textEdit_Output_File_Name = QTextEdit(self.horizontalLayoutWidget_3)
        self.textEdit_Output_File_Name.setObjectName(u"textEdit_Output_File_Name")
        self.textEdit_Output_File_Name.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(20)
        self.textEdit_Output_File_Name.setFont(font1)

        self.horizontalLayout_3.addWidget(self.textEdit_Output_File_Name)

        self.pushButton_generate = QPushButton(self.centralwidget)
        self.pushButton_generate.setObjectName(u"pushButton_generate")
        self.pushButton_generate.setGeometry(QRect(570, 170, 151, 51))
        font2 = QFont()
        font2.setFamily(u"Aharoni")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton_generate.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 782, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Handball Stats Generator", None))
        self.pushButton_Input_File.setText(QCoreApplication.translate("MainWindow", u"Select Input File", None))
        self.label_Input_File.setText("")
        self.pushButton_Output_Folder.setText(QCoreApplication.translate("MainWindow", u"Select Output Folder", None))
        self.label_Output_Folder.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Output File Name", None))
        self.pushButton_generate.setText(QCoreApplication.translate("MainWindow", u"Generate Report", None))
    # retranslateUi

