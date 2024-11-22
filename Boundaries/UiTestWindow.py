# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TestWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_TestWindow(object):
    def setupUi(self, TestWindow):
        if not TestWindow.objectName():
            TestWindow.setObjectName(u"TestWindow")
        TestWindow.resize(1015, 773)
        self.centralwidget = QWidget(TestWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.exitButton = QPushButton(self.centralwidget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(10, 710, 141, 51))
        font = QFont()
        font.setPointSize(16)
        self.exitButton.setFont(font)
        TestWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(TestWindow)

        QMetaObject.connectSlotsByName(TestWindow)
    # setupUi

    def retranslateUi(self, TestWindow):
        TestWindow.setWindowTitle(QCoreApplication.translate("TestWindow", u"\u0422\u0435\u0441\u0442 \u0428\u0443\u043b\u044c\u0442\u0435", None))
        self.exitButton.setText(QCoreApplication.translate("TestWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
    # retranslateUi

