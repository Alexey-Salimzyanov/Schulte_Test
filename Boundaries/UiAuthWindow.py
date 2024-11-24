# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AuthWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QLabel, QLineEdit, QPushButton, QWidget)

class Ui_AuthWindow(object):
    def setupUi(self, AuthWindow):
        if not AuthWindow.objectName():
            AuthWindow.setObjectName(u"AuthWindow")
        AuthWindow.resize(466, 383)
        self.centralwidget = QWidget(AuthWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.passwordEdit = QLineEdit(self.centralwidget)
        self.passwordEdit.setObjectName(u"passwordEdit")
        self.passwordEdit.setGeometry(QRect(80, 150, 211, 41))
        font = QFont()
        font.setPointSize(11)
        self.passwordEdit.setFont(font)
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.enterButton = QPushButton(self.centralwidget)
        self.enterButton.setObjectName(u"enterButton")
        self.enterButton.setGeometry(QRect(310, 150, 71, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.enterButton.setFont(font1)
        self.authLabel = QLabel(self.centralwidget)
        self.authLabel.setObjectName(u"authLabel")
        self.authLabel.setGeometry(QRect(150, 80, 157, 32))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.authLabel.setFont(font2)
        self.authLabel.setLayoutDirection(Qt.LeftToRight)
        self.toMainButton = QPushButton(self.centralwidget)
        self.toMainButton.setObjectName(u"toMainButton")
        self.toMainButton.setGeometry(QRect(170, 270, 121, 41))
        self.toMainButton.setFont(font1)
        AuthWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AuthWindow)

        QMetaObject.connectSlotsByName(AuthWindow)
    # setupUi

    def retranslateUi(self, AuthWindow):
        AuthWindow.setWindowTitle(QCoreApplication.translate("AuthWindow", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.passwordEdit.setPlaceholderText(QCoreApplication.translate("AuthWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.enterButton.setText(QCoreApplication.translate("AuthWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.authLabel.setText(QCoreApplication.translate("AuthWindow", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.toMainButton.setText(QCoreApplication.translate("AuthWindow", u"\u041d\u0430 \u0433\u043b\u0430\u0432\u043d\u0443\u044e", None))
    # retranslateUi
