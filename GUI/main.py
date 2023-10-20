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

lista_squadre =  []

import creazioine_squadre
import strutture as st

st.struttura()

class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()

        current_monitor = get_monitors()[0]
        width = current_monitor.width
        height = current_monitor.height 

        self.resize(width, height)

        self.showMaximized()
        self.setWindowTitle("APPLICAZIONE TORNEO")

        self.layout = QStackedLayout()

        widgetCrea = creazioine_squadre.crea(self)
        self.layout.addWidget(widgetCrea)    #pagina crea Squadre

        widgetTorneo = QWidget()
        self.layout.addWidget(widgetTorneo)    #pagina crea Torneo

        self.layout.setCurrentIndex(0)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    


 



app = QApplication(sys.argv)
window = MainWindow()
window.show()

window.closeEvent = window.closeEvent

app.exec()
