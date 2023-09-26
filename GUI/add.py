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



    def __init__(self, main_widget1, nome_sq, nome_g1, nome_g2):
        super().__init__()

        self.widg = self.sender()

        self.main = main_widget1
        main_layout = QVBoxLayout()  # Layout principale della finestra

        
        titolo = QLabel("NOME SQUADRA")
        self.nome_squadra = QLineEdit()
        self.nome_squadra.setText(nome_sq)
        gio1 = QLabel("GIOCATORE 1")
        self.nome_giocatore1 = QLineEdit()
        self.nome_giocatore1.setText(nome_g1)
        gio2 = QLabel("GIOCATORE 2")
        self.nome_giocatore2 = QLineEdit()
        self.nome_giocatore2.setText(nome_g2)
        save = QPushButton()
        save.setText("SALVA")
        save.clicked.connect(self.salva)

        main_layout.addWidget(titolo)
        main_layout.addWidget(self.nome_squadra)
        main_layout.addStretch(1)
        main_layout.addWidget(gio1)
        main_layout.addWidget(self.nome_giocatore1)
        main_layout.addWidget(gio2)
        main_layout.addWidget(self.nome_giocatore2)
        main_layout.addWidget(save)
        self.setLayout(main_layout)

    def salva(self):
        vn = self.nome_squadra.text()
        vg1 = self.nome_giocatore1.text()
        vg2 = self.nome_giocatore2.text()

        print("sq: " +str(vn) +" g1: " + str(vg1) + " g2: " + str(vg2))
        self.main.set_data(vn, vg1, vg2)
        self.accept()


   