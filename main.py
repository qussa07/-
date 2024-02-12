import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QPixmap, QKeyEvent
import PyQt5.QtGui
from PyQt5.QtWidgets import QLineEdit
import requests
from PIL import Image
from PyQt5.QtCore import Qt
from PyQt5.uic.properties import QtGui

SIZE = [1300, 900]
SIZE_W = [300, 300]


class Maps_API(QWidget):
    def __init__(self):
        super().__init__()
        self.zero()
        self.map_file = "map.png"
        self.initUI()

    def zero(self):
        self.ll = '46.953431,55.490871'
        self.spn = 0.05
        self.z = '4'
        self.map = 'map'

    def initUI(self):
        self.setGeometry(100, 100, SIZE[0], SIZE[1])
        self.setWindowTitle('Maps API')
        self.label = QLabel(self)
        self.label.resize(*SIZE)
        self.label.move(0, 0)
        self.one_button = QPushButton('Поиск', self)
        self.one_button.resize(60, 30)
        self.one_button.move(10, 10)
        self.coord = QLineEdit(self.ll, self)
        self.coord.resize(100, 30)
        self.coord.move(230, 10)
        self.spn_win = QLineEdit(str(self.spn), self)
        self.spn_win.resize(100, 30)
        self.spn_win.move(120, 10)
        self.one_button.clicked.connect(self.get_image)

    def new_data(self):
        self.ll = self.coord.text()
        self.spn = float(self.spn_win.text())

    def draw_map(self):
        self.pixmap = QPixmap(self.map_file)
        self.label.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
        x, y = list(map(float, self.ll.split(',')))
        if event.key() == Qt.Key_PageUp:
            self.spn += float(self.spn) / 2
        elif event.key() == Qt.Key_PageDown:
            self.spn -= float(self.spn) / 2
        if event.key() == Qt.Key_Up:
            y += 0.01 * self.spn
        elif event.key() == Qt.Key_Down:
            y -= 0.01 * self.spn
        elif event.key() == Qt.Key_Left:
            x -= 0.01 * self.spn
        elif event.key() == Qt.Key_Right:
            x += 0.01 * self.spn
        self.spn_win.setText(f'{self.spn}')
        self.coord.setText(f'{x},{y}')
        self.get_image()
        print(self.spn)

    def get_image(self):
        self.new_data()
        map_params = {
            "ll": self.ll,
            "spn": f'{self.spn},{self.spn}',
            "l": self.map
        }
        print(map_params)
        map_api_server = "http://static-maps.yandex.ru/1.x/"
        response = requests.get(map_api_server, params=map_params)
        if not response:
            print("Ошибка выполнения запроса:")
            print(map_api_server)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        print("Http статус:", response.status_code, "(", response.reason, ")")
        # Запишем полученное изображение в файл.
        with open(self.map_file, "wb") as file:
            file.write(response.content)
        self.draw_map()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Maps_API()
    ex.show()
    sys.exit(app.exec())
