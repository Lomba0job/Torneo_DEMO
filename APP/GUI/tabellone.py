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

import itertools


class Crea_tab(QWidget):

    def __init__(self, main):
        super().__init__()
        self.mainpage = main
        main_layout = QHBoxLayout()

        layout = QVBoxLayout()
        layout.addStretch(1)

        def split_and_shuffle(lst): 
            random.shuffle(lst)
            half = len(lst) // 2
            print(half)
            return lst[:half], lst[half:]

        random.shuffle(st.lista_squadre)
        list1, list2 = split_and_shuffle(st.lista_squadre)
 

        n = 0
        for n in range(len(list1)):
            p1 = partita.Ogg_partita(self, list1[n], list2[n])
            layout.addWidget(p1)
       

        self.classi = classifica.Crea_clas(self)

        main_layout.addLayout(layout)
        main_layout.addWidget(self.classi)

        self.setLayout(main_layout)


    def aggiorna_classifica(self):
        self.classi.riaggiorna()

    def partita_incorso(self, p):
        st.stato = 1
        st.n_p = p

    def partita_finita(self):
        st.stato = 0
        st.n_p = 0 
        