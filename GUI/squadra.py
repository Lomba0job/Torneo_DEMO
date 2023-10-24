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

import add 
import strutture as st



class Ogg_quadra(QWidget):

    nome_squadra = ""
    nome_giocatore1 = ""
    nome_giocatore2 = ""

    reti_eff = 0
    reti_sub = 0
    punti = 0

    def __init__(self):
        super().__init__()
        
        main_layout = QVBoxLayout()  # Layout principale della finestra
        self.nomeSquadra = QLabel(" NOME SQUADRA ")

        main_layout.addWidget(self.nomeSquadra)

        self.setLayout(main_layout)

    def set_data(self, nome_SQ, nome_G1, nome_G2):

        self.nome_squadra = nome_SQ
        self.nome_giocatore1 = nome_G1
        self.nome_giocatore2 = nome_G2

        self.nomeSquadra.setText(self.nome_squadra)

    def add_rete_eff(self):
        self.reti_eff += 1

    def add_rete_sub(self):
        self.reti_sub += 1

    def rem_rete_eff(self):
        self.reti_eff -= 1

    def rem_rete_sub(self):
        self.reti_sub -= 1

    def get_nome_squadra(self):
        return self.nome_squadra
    

    def calcola_punti(self):
        self.punti = self.reti_eff - self.reti_sub

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            dialog_1 = add.Connection_dialog(self, self.nome_squadra, self.nome_giocatore1, self.nome_giocatore2)
            dialog_1.exec()
    