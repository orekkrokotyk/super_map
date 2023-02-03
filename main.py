import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
import requests


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.zoom = 18
        delta = 0.2
        self.map_l = 'map'
        self.map_ll = [37.620431, 55.753789]
        self.render_map()

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_PageUp and self.zoom < 17:
            self.zoom += 1
        if key == Qt.Key_PageDown and 0 < self.zoom:
            self.zoom -= 1


        self.render_map()

    def render_map(self):
        params = {
            "ll": f'{self.map_ll[0]},{self.map_ll[1]}',
            "l": self.map_l,
            'z': self.zoom

        }
        resspons = requests.get('https://static-maps.yandex.ru/1.x/', params=params)
        with open('tmp.png', 'wb') as tmp:
            tmp.write(resspons.content)

        pixmap = QPixmap()
        pixmap.load('tmp.png')

        self.label.setPixmap(pixmap)


app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())