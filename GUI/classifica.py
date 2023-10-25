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

class Oggetto(QWidget):

    def __init__(self, ogg):
        super().__init__()
        
        self.sq = ogg
        
        l = QHBoxLayout()
        self.n = ogg.get_punti_squadra()
        self.nome = QLabel(ogg.get_nome_squadra())
        self.punti = QLabel(str(self.n))
        l.addWidget(self.nome)
        l.addWidget(self.punti)

        self.setLayout(l)
    
    def aggiorna(self):
        self.n = self.sq.get_punti_squadra()
        self.punti.setText(str(self.n))
        

        

class Crea_clas(QWidget):

    def __init__(self, main):
        super().__init__()
        self.mainpage = main

        self.lista_widg = []
        l = QVBoxLayout()

        self.layout_m = QVBoxLayout()
        title = QLabel("CLASSIFICA VIRTUALE")

        

        for ogg in st.lista_squadre:
            widg = Oggetto(ogg)
            self.layout_m.addWidget(widg)
            self.lista_widg.append(widg)

        l.addWidget(title)
        l.addLayout(self.layout_m)
        self.setLayout(l)
        

        
    def riaggiorna(self):
        for widg in self.lista_widg:
            print(widg)
            self.layout_m.removeWidget(widg)
            widg.aggiorna()

        lista_ordinata = sorted(self.lista_widg, key=lambda oggetto: oggetto.n, reverse=True)

        for widg in lista_ordinata:
            self.layout_m.addWidget(widg)

        self.lista_widg = lista_ordinata
        
        