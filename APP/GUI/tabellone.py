import sys
import typing
from PyQt6 import QtGui
from PyQt6.QtCore import QSize, Qt, QFile, QTextStream, QTimer, QRect, QEvent, QRectF, QFileInfo
from PyQt6.QtGui import QIcon, QAction, QKeySequence, QPalette, QColor, QPainter, QPixmap, QPen, QPaintDevice
from PyQt6.QtWidgets import (
    QApplication,
    QMenu,
    QCheckBox,
    QPushButton,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLayout,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QWidget,
    QToolBar,
    QStatusBar,
    QBoxLayout,
    QHBoxLayout,
    QVBoxLayout,
    QStackedLayout,
    QGridLayout,
    QFileDialog,
    QMessageBox,
    QDialog,
)
import glob
import random
import math
import numpy as np
import time

import partita
import strutture as st
import classifica




class Crea_tab(QWidget):

    def __init__(self, main):
        super().__init__()
        self.mainpage = main
        main_layout = QHBoxLayout()

        layout = QVBoxLayout()

        p1 = partita.Ogg_partita(self, st.lista_squadre[0], st.lista_squadre[1])
        p2 = partita.Ogg_partita(self, st.lista_squadre[2], st.lista_squadre[3])

        layout.addStretch(1)
        layout.addWidget(p1)
        layout.addWidget(p2)
        layout.addStretch(1)

        self.classi = classifica.Crea_clas(self)

        main_layout.addLayout(layout)
        main_layout.addWidget(self.classi)

        self.setLayout(main_layout)


    def aggiorna_classifica(self):
        self.classi.riaggiorna()

    def partita_incorso(self):
        print("DIOCANE")
        print(st.stato)
        st.stato = 1

    def partita_finita(self):
        st.stato = 0