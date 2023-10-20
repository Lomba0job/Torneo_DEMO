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
import serial
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot, InfiniteLine
import random
import math
import numpy as np
import time




class Ogg_partita(QWidget):


    reti_sq1 = 0 
    reti_sq2 = 0

    def __init__(self, s1, s2):
        super().__init__()

        self.squadra1 = s1
        self.squadra2 = s2

        l_tempo = QHBoxLayout()
        label_tempo = QLabel("TEMPO: ")
        self.tempo = QLabel("10:00")
        l_tempo.addWidget(label_tempo)
        l_tempo.addWidget(self.tempo)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(l_tempo)

        team = QHBoxLayout()

        l_sq1 = QVBoxLayout()
        l_sq1.addWidget(self.squadra1)
        self.p1 = QLabel("0")
        l_sq1.addWidget(self.p1)

        l_sq2 = QVBoxLayout()
        l_sq2.addWidget(self.squadra2)
        self.p2 = QLabel("0")
        l_sq2.addWidget(self.p2)

        team.addLayout(l_sq1)
        team.addLayout(l_sq2)

        self.main_layout.addLayout(team)

        self.setLayout(self.main_layout)

    #def avvia(self):
