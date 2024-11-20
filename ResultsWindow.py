# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ResultsWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_ResultsWindow(object):
    def setupUi(self, ResultsWindow):
        if not ResultsWindow.objectName():
            ResultsWindow.setObjectName(u"ResultsWindow")
        ResultsWindow.resize(1058, 600)
        self.centralwidget = QWidget(ResultsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.resultsTableWidget = QTableWidget(self.centralwidget)
        if (self.resultsTableWidget.columnCount() < 10):
            self.resultsTableWidget.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.resultsTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.resultsTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.resultsTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.resultsTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.resultsTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.resultsTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.resultsTableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.resultsTableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.resultsTableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.resultsTableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.resultsTableWidget.setObjectName(u"resultsTableWidget")
        self.resultsTableWidget.setGeometry(QRect(20, 100, 1011, 381))
        self.resultsTableWidget.setShowGrid(True)
        self.resultsTableWidget.setColumnCount(10)
        self.resultsTableWidget.horizontalHeader().setVisible(True)
        self.exitButton = QPushButton(self.centralwidget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(480, 520, 111, 41))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.exitButton.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(390, 30, 269, 32))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label.setFont(font1)
        ResultsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ResultsWindow)

        QMetaObject.connectSlotsByName(ResultsWindow)
    # setupUi

    def retranslateUi(self, ResultsWindow):
        ResultsWindow.setWindowTitle(QCoreApplication.translate("ResultsWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.resultsTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ResultsWindow", u"ID", None));
        ___qtablewidgetitem1 = self.resultsTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ResultsWindow", u"\u0412\u0440\u0435\u043c\u044f_1", None));
        ___qtablewidgetitem2 = self.resultsTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ResultsWindow", u"\u0412\u0440\u0435\u043c\u044f_2", None));
        ___qtablewidgetitem3 = self.resultsTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ResultsWindow", u"\u0412\u0440\u0435\u043c\u044f_3", None));
        ___qtablewidgetitem4 = self.resultsTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ResultsWindow", u"\u0412\u0440\u0435\u043c\u044f_4", None));
        ___qtablewidgetitem5 = self.resultsTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ResultsWindow", u"\u0412\u0440\u0435\u043c\u044f_5", None));
        ___qtablewidgetitem6 = self.resultsTableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ResultsWindow", u"\u0427\u0438\u0441\u043b\u043e_\u043e\u0448\u0438\u0431\u043e\u043a", None));
        ___qtablewidgetitem7 = self.resultsTableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("ResultsWindow", u"\u042d\u0420", None));
        ___qtablewidgetitem8 = self.resultsTableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("ResultsWindow", u"\u0412\u0420", None));
        ___qtablewidgetitem9 = self.resultsTableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("ResultsWindow", u"\u041f\u0423", None));
        self.exitButton.setText(QCoreApplication.translate("ResultsWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.label.setText(QCoreApplication.translate("ResultsWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432", None))
    # retranslateUi

