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

import squadra 
import strutture as st




class crea(QWidget):

    def __init__(self, main):
        super().__init__()

        self.mainpage = main
        l = QVBoxLayout()
        grid_layout = QGridLayout()
        # Creazione 
        for row in range(3):
            for col in range(5):
                widget = squadra.Ogg_quadra()
                grid_layout.addWidget(widget, row, col)
                st.lista_squadre.append(widget)

        save = QPushButton()
        save.setText("SALVA")
        save.clicked.connect(self.save_f)

        l.addLayout(grid_layout)
        l.addWidget(save)

        self.setLayout(l)

    def save_f(self):
        self.mainpage.layout.setCurrentIndex(1)