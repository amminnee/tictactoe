from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QSpacerItem
from PyQt5.QtCore import Qt


class settings(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setAlignment(Qt.AlignCenter)
        self.players = []
        for i in range(2):
            player = {}
            player["label"] = QLabel("Player {} name".format(i+1), self)
            label = player["label"]
            label.setFixedSize(500, 30)
            label.setObjectName("line_label")
            self.main_layout.addWidget(label)

            player["line edit"] = QLineEdit(self)
            line = player["line edit"]
            line.setFixedSize(600, 80)
            line.setObjectName("line")
            self.main_layout.addWidget(line)

            player["error"] = QLabel("", self)
            error = player["error"]
            error.setFixedSize(500, 18)
            error.setObjectName("error")
            self.main_layout.addWidget(error)
            
            self.players.append(player)
            self.main_layout.addSpacerItem(QSpacerItem(0, 30))

        self.main_layout.addSpacerItem(QSpacerItem(0, 20))

        self.save = QPushButton("Save",self)
        self.save.setCursor(Qt.PointingHandCursor)
        self.save.setFixedSize(250, 80)
        self.save.setObjectName("button")
        self.main_layout.addWidget(self.save, alignment=Qt.AlignCenter)

        with open("style.css", "r") as style:
            self.setStyleSheet(style.read())
