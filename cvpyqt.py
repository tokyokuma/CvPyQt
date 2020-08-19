#!python3
# -*- coding: utf-8 -*-

import sys
import os.path
import numpy as np
import cv2
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from cvpyqtUi import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.scene = QGraphicsScene()
        self.set()
        self.ui.processingButton.clicked.connect(self.push_processing)

    def set(self):
        cv_img = cv2.imread("sample.jpg")
        cv_img = cv2.cvtColor(cv_img,cv2.COLOR_BGR2RGB)
        height, width, dim = cv_img.shape
        bytesPerLine = dim * width
        self.image = QImage(cv_img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.item = QGraphicsPixmapItem(QPixmap.fromImage(self.image))
        self.scene.addItem(self.item)
        self.ui.graphicsView.setScene(self.scene)

    def push_processing(self):
        print("processing")

 #   def show(self):
 #       self.ui.graphicsView.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())