import sys
from screeninfo import get_monitors
import re
from PyQt6 import QtGui
from PyQt6.QtCore import QSize, Qt, QFile, QTextStream, QTimer, QRect, QEvent, QRectF, QFileInfo, QCoreApplication
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
    QColorDialog,
    QDialogButtonBox,
    
)
import glob
#import serial
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot, InfiniteLine
from pyqtgraph.GraphicsScene import exportDialog
import random
import math
#from modbus_IMA import ModBus
import numpy as np
import time
from pyModbusTCP.client import ModbusClient
import os 

project_dir = os.path.dirname(os.path.abspath(os.getcwd()))
sys.path.append(project_dir)


import squadra

class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()
        # init modbus client

        current_monitor = get_monitors()[0]
        width = current_monitor.width
        height = current_monitor.height 

        self.resize(width, height)

        self.showMaximized()
        self.setWindowTitle("APPLICAZIONE TORNEO")

        layout = QVBoxLayout()

        lh = QHBoxLayout()
        widg1 = squadra.Ogg_quadra()
        widg2 = squadra.Ogg_quadra()
        widg3 = squadra.Ogg_quadra()
        widg4 = squadra.Ogg_quadra()
        lh.addWidget(widg1)
        lh.addWidget(widg2)
        lh.addWidget(widg3)
        lh.addWidget(widg4)

        lh1 = QHBoxLayout()
        widg11 = squadra.Ogg_quadra()
        widg12 = squadra.Ogg_quadra()
        widg13 = squadra.Ogg_quadra()
        widg14 = squadra.Ogg_quadra()
        lh1.addWidget(widg11)
        lh1.addWidget(widg12)
        lh1.addWidget(widg13)
        lh1.addWidget(widg14)    

        lh2 = QHBoxLayout()
        widg21 = squadra.Ogg_quadra()
        widg22 = squadra.Ogg_quadra()
        widg23 = squadra.Ogg_quadra()
        widg24 = squadra.Ogg_quadra()
        lh2.addWidget(widg21)
        lh2.addWidget(widg22)
        lh2.addWidget(widg23)
        lh2.addWidget(widg24)      

        layout.addLayout(lh)
        layout.addLayout(lh1)
        layout.addLayout(lh2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    


 



app = QApplication(sys.argv)
window = MainWindow()
window.show()

window.closeEvent = window.closeEvent

app.exec()
