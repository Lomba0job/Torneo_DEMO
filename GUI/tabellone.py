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

import partita
import strutture as st




class Crea_tab(QWidget):

    def __init__(self, main):
        super().__init__()
        self.mainpage = main
        layout = QVBoxLayout()

        

        p1 = partita.Ogg_partita(st.lista_squadre[0], st.lista_squadre[1])
        p2 = partita.Ogg_partita(st.lista_squadre[2], st.lista_squadre[3])

        layout.addStretch(1)
        layout.addWidget(p1)
        layout.addWidget(p2)
        layout.addStretch(1)


        self.setLayout(layout)
