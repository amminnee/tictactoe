from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QApplication
from MainPage import mainPage
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from Player import player
from OverPage import overPage
from Settings import settings


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.initGrid()

    def initUi(self):
        self.setObjectName("window")
        self.setGeometry(400, 50, 800, 950)
        self.setWindowTitle("tic tac toe")
        with open("style.css", 'r') as s:
            self.setStyleSheet(s.read())
        self.setWindowIcon(QIcon("assets/icon.png"))
        self.app = QStackedWidget(self)
        self.setCentralWidget(self.app)        
        self.fill = 0

        self.main_page = mainPage()
        self.setTurn()
        self.app.addWidget(self.main_page)
        self.main_page.reset.clicked.connect(lambda: self.resetGrid())
        self.main_page.reset_score.clicked.connect(self.resetScore)
        self.main_page.settings.clicked.connect(self.edit)
        self.whenClicked()

        self.p_instances = []
        for i in range(2):
            p_instance = player(i)
            self.p_instances.append(p_instance)

        self.over = overPage()
        self.app.addWidget(self.over)
        for i in range(2):
            self.updatePlayer(i)
        self.over.again.clicked.connect(lambda: self.changeIndex(0))

        self.settings = settings()
        self.app.addWidget(self.settings)
        self.settings.save.clicked.connect(self.save)

    def changeIndex(self, i):
        self.app.setCurrentIndex(i)

    def setTurn(self):
        for i, player in enumerate(self.main_page.players):
            if i == self.fill % 2:
                player['fill'].setObjectName("label_turn")
                player['name'].setObjectName("label_turn")
                player['score'].setObjectName("score")
            else:
                player['fill'].setObjectName("label")
                player['name'].setObjectName("label")
                player['score'].setObjectName("score")
        
        with open('style.css', 'r') as style:
            self.main_page.setStyleSheet(style.read())

    def save(self):
        flag = 1
        for i in range(2):
            name = self.settings.players[i]["line edit"].text().strip()
            if len(name) < 13:
                self.p_instances[i].updateName(name)
                self.settings.players[i]["error"].setText("")
                self.updatePlayer(i)    
            else:
                flag = 0
                self.settings.players[i]["error"].setText("Too many characters!")
        if flag:
            self.changeIndex(0)

    def edit(self):
        for i, player in enumerate(self.settings.players):
            player["line edit"].setText(self.p_instances[i].name)
        self.changeIndex(2)

    def resetScore(self):
        self.resetGrid()
        for i, player in enumerate(self.p_instances):
            player.resetScore()
            self.updatePlayer(i)

    def updatePlayer(self, i):
        self.main_page.players[i]["name"].setText(self.p_instances[i].name)
        self.main_page.players[i]["score"].setText(str(self.p_instances[i].score))
        self.main_page.players[i]["fill"].setText(self.p_instances[i].fill)

    def initGrid(self):
        self.grid = [[0 for j in range(3)] for i in range(3)]

    def resizeEvent(self, event):
        size = event.size().height()
        cell_size = round(size*0.19)
        for line in self.main_page.grid:
            for cell in line:
                cell.setFixedSize(cell_size, cell_size)

    def whenClicked(self):
        def create_callback(cell, i, j):
            def callback():
                self.updateCell(self.fill, cell, i, j)
            return callback

        for i, line in enumerate(self.main_page.grid):
            for j, cell in enumerate(line):
                cell.clicked.connect(create_callback(cell, i, j))

    def updateCell(self, fill, cell, x, y):
        if self.grid[x][y] == 0:
            if fill % 2 == 0:
                self.grid[x][y] = 1
                cell.setText("X")
            else:
                cell.setText("O")
                self.grid[x][y] = 2
        
            cell.setObjectName("full_cell")
            with open('style.css', 'r') as style:
                self.main_page.setStyleSheet(style.read())
            self.fill += 1
            self.setTurn()
            self.checkEnd(x, y)

    def resetGrid(self):
        self.initGrid()
        for line in self.main_page.grid:
            for cell in line:
                cell.setText("")
                cell.setObjectName("cell")
        with open("style.css", "r") as s:
            self.main_page.setStyleSheet(s.read())

    def checkFull(self):
        cnt = 0
        for line in self.grid:
            for cell in line:
                if cell == 0:
                    cnt = 1
        if cnt == 0:
            QTimer.singleShot(100, self.full)

    def checkEnd(self, x, y):
        self.checkH(x, y)
        self.checkV(x, y)
        self.checkD1()
        self.checkD2()
        self.checkFull()

    def checkD1(self):
        value = self.grid[0][0]
        for i in range(1,3):
            if self.grid[i][i] == value and value != 0:
                value = self.grid[i][i]
            else:
                return
        QTimer.singleShot(100, self.win)

    def checkD2(self):
        value = self.grid[0][2]
        for i, j in zip(range(1, 3), reversed(range(2))):
            if value == self.grid[i][j] and value != 0:
                value = self.grid[i][j]
            else:
                return
        QTimer.singleShot(100, self.win)

    def checkH(self, x, y):
        value = self.grid[x][y]
        for cell in self.grid[x]:
            if cell == value:
                value = cell
            else:
                return
            
        QTimer.singleShot(100, self.win)
        
    def checkV(self, x, y):
        value = self.grid[x][y]
        for line in self.grid:
            if line[y] == value:
                value = line[y]
            else:
                return
            
        QTimer.singleShot(100, self.win)

    def win(self):
        self.resetGrid()
        self.changeIndex(1)
        winner = (self.fill+1)%2
        win_text = "Game Over\n{} won!".format(self.p_instances[winner].name)
        self.over.label.setText(win_text)
        self.p_instances[winner].updateScore()
        for i in range(2):
            self.updatePlayer(i)

    def full(self):
        self.resetGrid()
        self.changeIndex(1)
        full_text = "Game Over\nTie!"
        self.over.label.setText(full_text)

if __name__ == "__main__":
    application = QApplication([])
    window = Main()
    window.showMaximized()
    application.exec_()