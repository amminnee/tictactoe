from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize

class mainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.h_space1 = QSpacerItem(1, 1, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.space = QSpacerItem(1, 10)
        self.v_space1 = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(50, 50, 50, 50)
        h_layout = QHBoxLayout()
        self.main_layout.addLayout(h_layout)
        v_layout = QVBoxLayout()
        h_layout.addLayout(v_layout)

        self.players = []
        for i in range(2):
            player = {
                "fill": self.smallLabel(),
                "name": self.largeLabel(),
                "score": self.smallLabel()
            }
            line_layout = QHBoxLayout()
            v_layout.addLayout(line_layout)
            line_layout.addWidget(player["fill"])
            line_layout.addWidget(player["name"])
            line_layout.addWidget(player["score"])
            self.players.append(player)

        h_layout.addSpacerItem(self.h_space1)

        right_layout = QVBoxLayout()
        self.settings = QPushButton("", self)
        self.settings.setToolTip("edit")
        self.settings.setObjectName("small_button")
        self.settings.setFixedSize(65, 65)
        self.settings.setIcon(QIcon("assets/edit.png"))
        self.settings.setIconSize(QSize(50, 50))
        self.settings.setCursor(Qt.PointingHandCursor)
        right_layout.addWidget(self.settings)

        right_layout.addSpacerItem(QSpacerItem(0, 5))

        self.reset_score = QPushButton("", self)
        self.reset_score.setToolTip("reset score")
        self.reset_score.setObjectName("small_button")
        self.reset_score.setFixedSize(65, 65)
        self.reset_score.setIcon(QIcon("assets/reset.png"))
        self.reset_score.setIconSize(QSize(45, 45))
        self.reset_score.setCursor(Qt.PointingHandCursor)

        right_layout.addWidget(self.reset_score)
        h_layout.addLayout(right_layout)

        self.main_layout.addSpacerItem(self.v_space1)

        self.grid = []
        for i in range(3):
            line = self.addLine()
            self.grid.append(line)
            self.main_layout.addLayout(self.h_layout)
        
        self.main_layout.addSpacerItem(self.space)

        self.reset = QPushButton("reset", self)
        self.reset.setCursor(Qt.PointingHandCursor)
        self.reset.setObjectName("button")
        self.reset.setFixedSize(250, 80)
        self.main_layout.addWidget(self.reset, alignment=Qt.AlignCenter)

        with open('style.css', 'r') as style:
            self.setStyleSheet(style.read())

    def smallLabel(self):
        label = QLabel("", self)
        label.setAlignment(Qt.AlignCenter)
        label.setFixedSize(50, 50)
        return label
    
    def largeLabel(self):
        label = QLabel("", self)
        label.setAlignment(Qt.AlignCenter)
        label.setFixedSize(170, 50)
        return label

    def addCell(self):
        cell = QPushButton("", self)
        cell.setObjectName("cell")
        return cell
    
    def addLine(self):
        self.h_layout = QHBoxLayout()
        self.h_layout.addSpacerItem(self.h_space1)
        line = []
        for i in range(3):
            cell = self.addCell()
            line.append(cell)
            self.h_layout.addWidget(cell)
        self.h_layout.addSpacerItem(self.h_space1)

        return line
    