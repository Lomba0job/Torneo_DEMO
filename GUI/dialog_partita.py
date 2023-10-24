import sys
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


class Connection_dialog(QDialog):



    def __init__(self, main_widget):
        super().__init__()

        self.widg = self.sender()

        self.main = main_widget
        main_layout = QVBoxLayout()  # Layout principale della finestra

        titolo = QLabel(self.main.get_nome_p())

        avvia = QPushButton("AVVIA PARTITA")
        avvia.clicked.connect(self.start)

        l = QVBoxLayout()
        l1 = QHBoxLayout()
        l2 = QHBoxLayout()
        p1 = QPushButton("+1")
        p1.clicked.connect(self.segna1)
        p2 = QPushButton("+1")
        p2.clicked.connect(self.segna2)

        m1 = QPushButton("-1")
        m1.clicked.connect(self.desegna1)
        m2 = QPushButton("-1")
        m2.clicked.connect(self.desegna2)

        l1.addWidget(p1)
        l1.addWidget(p2)
        l2.addWidget(m1)
        l2.addWidget(m2)

        l.addLayout(l1)
        l.addLayout(l2)

        main_layout.addWidget(titolo)
        main_layout.addWidget(avvia)
        main_layout.addLayout(l)

        self.setLayout(main_layout)
        
    def start(self):
        self.main.start_t()

    def segna1(self):
        self.main.segna_rete(1)

    def segna2(self):
        self.main.segna_rete(2)

    def desegna1(self):
        self.main.desegna_rete(1)

    def desegna2(self):
        self.main.desegna_rete(2)
