from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt


class overPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(50, 50, 50, 50)

        self.label = QLabel("", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFixedSize(1200, 500)
        self.label.setObjectName("text")
        layout.addWidget(self.label, alignment=Qt.AlignCenter)

        self.again = QPushButton("Play again", self)
        self.again.setCursor(Qt.PointingHandCursor)
        self.again.setObjectName("button")
        self.again.setFixedSize(250, 80)
        layout.addWidget(self.again, alignment=Qt.AlignHCenter)

        with open("style.css", 'r') as style:
            self.setStyleSheet(style.read())