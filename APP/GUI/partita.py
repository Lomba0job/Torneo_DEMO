import sys
import typing
from PyQt6 import QtGui
from PyQt6.QtCore import QSize, Qt, QFile, QTextStream, QTimer, QRect, QEvent, QRectF, QFileInfo, QTime
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


import dialog_partita as add
import strutture as st

class Ogg_partita(QWidget):

    

    reti_sq1 = 0        #reti della partita  
    reti_sq2 = 0        #reti della partita 
    
    giocata = 0
    stato = 0 

    def __init__(self, main, s1, s2):
        super().__init__()
        self.main_page = main
        self.time_left = QTime(0, 0, 5)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)

        self.squadra1 = s1
        self.squadra2 = s2

        l_tempo = QHBoxLayout()
        label_tempo = QLabel("TEMPO: ")
        self.tempo = QLabel(self.time_left.toString())
        l_tempo.addWidget(label_tempo)
        l_tempo.addWidget(self.tempo)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(l_tempo)

        team = QHBoxLayout()

        l_sq1 = QVBoxLayout()
        label1  = QLabel(self.squadra1.get_nome_squadra())
        l_sq1.addWidget(label1)
        self.p1 = QLabel("0")
        l_sq1.addWidget(self.p1)

        l_sq2 = QVBoxLayout()
        label2  = QLabel(self.squadra2.get_nome_squadra())
        l_sq2.addWidget(label2)
        self.p2 = QLabel("0")
        l_sq2.addWidget(self.p2)

        team.addLayout(l_sq1)
        team.addLayout(l_sq2)

        self.main_layout.addLayout(team)

        self.setLayout(self.main_layout)

    def start_t(self):
        self.timer.start(1000)
        self.main_page.partita_incorso(self)

    def update(self):
        self.time_left = self.time_left.addSecs(-1)
        self.tempo.setText(self.time_left.toString())

        if self.time_left == QTime(0, 0, 0):
            print("Il timer è a zero!")
            self.end_partita()

    def get_nome_p(self):
        nome_p = self.squadra1.get_nome_squadra() +" vs " + self.squadra2.get_nome_squadra()
        return nome_p
    
    def segna_rete(self, n):
        print(n)
        if (n == 1): #squadra 1
            self.reti_sq1 += 1
            self.squadra1.add_rete_eff()
            self.squadra2.add_rete_sub()
            if (self.time_left > QTime(0, 0, 0)):
                self.p1.setText(str(self.reti_sq1))
            else:
                self.end_ui()
            self.main_page.aggiorna_classifica()
        elif(n == 2):
            self.reti_sq2 += 1
            self.squadra2.add_rete_eff()
            self.squadra1.add_rete_sub()
            if (self.time_left > QTime(0, 0, 0)):
                self.p2.setText(str(self.reti_sq2))
            else:
                self.end_ui()
            self.main_page.aggiorna_classifica()

    def desegna_rete(self, n):
        print(n)
        if (n == 1): #squadra 1
            self.reti_sq1 -= 1
            self.squadra1.rem_rete_eff()
            self.squadra2.rem_rete_sub()
            if (self.time_left > QTime(0, 0, 0)):
                self.p1.setText(str(self.reti_sq1))
            else:
                self.end_ui()
            self.main_page.aggiorna_classifica()

        elif(n == 2):
            self.reti_sq2 -= 1
            self.squadra2.rem_rete_eff()
            self.squadra1.rem_rete_sub()
            if (self.time_left > QTime(0, 0, 0)):
                self.p2.setText(str(self.reti_sq2))
            else:
                self.end_ui()
            self.main_page.aggiorna_classifica()


    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if(self.giocata == 0):
                if(st.n_p is self or st.stato == 0):
                    #print("premuto")            #TEST
                    self.dialog_1 = add.Connection_dialog(self)
                    self.dialog_1.exec()
            else:
                dialog = add.Connection_dialog_end(self)
                dialog.exec()

    def remove_items(self, layout):
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            if item.widget() is not None:
                item.widget().deleteLater()
            elif item.layout() is not None:
                self.remove_items(item.layout())
            layout.removeItem(item)

    def end_partita(self):
        self.timer.stop()

        self.end_ui()
        
        self.main_page.partita_finita()
        self.giocata=1
        
        
    def end_ui(self):
        self.remove_items(self.main_layout)
        self.main_layout.update()
        
        if (self.reti_sq1 > self.reti_sq2):
            vincitore = self.squadra1.get_nome_squadra()
            punteggio = str(self.reti_sq1) + " a " + str(self.reti_sq2)
            perdente = self.squadra2.get_nome_squadra()

        else:
            vincitore =  self.squadra2.get_nome_squadra()
            punteggio = str(self.reti_sq2) + " a " + str(self.reti_sq1)
            perdente = self.squadra1.get_nome_squadra()

        titolo = QLabel(vincitore)
        titolo.setObjectName("win")
        punt = QLabel(punteggio)
        punt.setObjectName("punt")
        sub = QLabel(perdente)
        sub.setObjectName("lose")
        
        self.main_layout.addWidget(titolo)
        self.main_layout.addWidget(punt)
        self.main_layout.addWidget(sub)

        #! ECCESSIVA
        self.squadra1.calcola_punti()
        self.squadra2.calcola_punti()
                