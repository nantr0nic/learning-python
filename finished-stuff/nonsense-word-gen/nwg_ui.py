# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nsw-gen-ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# This file is the "blueprint" for your GUI window.
# It was generated by Qt Designer and contains all the UI elements (buttons, checkboxes, etc.)
# and their properties (size, position, etc.)

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpinBox, QStatusBar, QWidget)

# This class is like a blueprint that defines how your window should look
# It doesn't handle any functionality - that's done in main.py
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # This method creates all the UI elements and sets their properties
        # It's called by main.py to set up the actual window
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(226, 514)
        MainWindow.setMaximumSize(QSize(226, 514))
        font = QFont()
        font.setFamilies([u"Arial"])
        MainWindow.setFont(font)
        MainWindow.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.generated_words = QScrollArea(self.centralwidget)
        self.generated_words.setObjectName(u"generated_words")
        self.generated_words.setGeometry(QRect(20, 160, 181, 291))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generated_words.sizePolicy().hasHeightForWidth())
        self.generated_words.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.generated_words.setFont(font1)
        self.generated_words.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 179, 329))
        self.generated_words.setWidget(self.scrollAreaWidgetContents)
        self.soundsBox = QComboBox(self.centralwidget)
        self.soundsBox.addItem("")
        self.soundsBox.addItem("")
        self.soundsBox.addItem("")
        self.soundsBox.addItem("")
        self.soundsBox.addItem("")
        self.soundsBox.addItem("")
        self.soundsBox.setObjectName(u"soundsBox")
        self.soundsBox.setGeometry(QRect(50, 10, 121, 22))
        self.include_qpk = QCheckBox(self.centralwidget)
        self.include_qpk.setObjectName(u"include_qpk")
        self.include_qpk.setGeometry(QRect(20, 100, 181, 20))
        self.include_digs = QCheckBox(self.centralwidget)
        self.include_digs.setObjectName(u"include_digs")
        self.include_digs.setGeometry(QRect(20, 80, 181, 20))
        self.include_dips = QCheckBox(self.centralwidget)
        self.include_dips.setObjectName(u"include_dips")
        self.include_dips.setGeometry(QRect(20, 40, 181, 20))
        self.generate_button = QPushButton(self.centralwidget)
        self.generate_button.setObjectName(u"generate_button")
        self.generate_button.setGeometry(QRect(40, 460, 131, 24))
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(20, 60, 181, 20))
        self.words_number = QSpinBox(self.centralwidget)
        self.words_number.setObjectName(u"words_number")
        self.words_number.setGeometry(QRect(100, 130, 101, 22))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 130, 71, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NWG", None))
        self.soundsBox.setItemText(0, QCoreApplication.translate("MainWindow", u"CV", None))
        self.soundsBox.setItemText(1, QCoreApplication.translate("MainWindow", u"VC", None))
        self.soundsBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CVC", None))
        self.soundsBox.setItemText(3, QCoreApplication.translate("MainWindow", u"CCVC", None))
        self.soundsBox.setItemText(4, QCoreApplication.translate("MainWindow", u"CVCC", None))
        self.soundsBox.setItemText(5, QCoreApplication.translate("MainWindow", u"CCVCC", None))
        self.soundsBox.setItemText(6, QCoreApplication.translate("MainWindow", u"CCVCC (Common)", None))

#if QT_CONFIG(tooltip)
        self.soundsBox.setToolTip(QCoreApplication.translate("MainWindow", u"Select sound combinations. C = consonant sound, V = vowel sound. (e.g. \"BAT\" is a CVC. \"STOP\" is a CCVC. etc.)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.include_qpk.setToolTip(QCoreApplication.translate("MainWindow", u"Include \"qu\", \"ph\", and \"kn\" at the beginning of the word.", None))
#endif // QT_CONFIG(tooltip)
        self.include_qpk.setText(QCoreApplication.translate("MainWindow", u"Include \"qu\", \"ph\", \"kn\"", None))
#if QT_CONFIG(tooltip)
        self.include_digs.setToolTip(QCoreApplication.translate("MainWindow", u"Include \"th\", \"ch\", and \"sh\"", None))
#endif // QT_CONFIG(tooltip)
        self.include_digs.setText(QCoreApplication.translate("MainWindow", u"Include digraphs", None))
#if QT_CONFIG(tooltip)
        self.include_dips.setToolTip(QCoreApplication.translate("MainWindow", u"Include diphthongs like \"oi\", \"aw\", and \"ou\"", None))
#endif // QT_CONFIG(tooltip)
        self.include_dips.setText(QCoreApplication.translate("MainWindow", u"Include dipthongs", None))
        self.generate_button.setText(QCoreApplication.translate("MainWindow", u"Generate!", None))
#if QT_CONFIG(tooltip)
        self.checkBox.setToolTip(QCoreApplication.translate("MainWindow", u"Include vowel teams like \"ai\", \"ea\", and \"ui\"", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Include vowel teams", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"How many:", None))
    # retranslateUi
