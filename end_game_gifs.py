import sys
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*

class end_game_gifs(QWidget):
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setGeometry(450, 450, 600, 500)
        self.setWindowTitle('End Game Gifs')
        self.setPalette(QPalette(QColor("cyan")))
        self.setAutoFillBackground(True)  
        self.win_gif = QPushButton('WIN GIF')
        self.loss_gif = QPushButton('LOSE GIF')
        self.draw_gif = QPushButton('TIE GIF')
        
        a = QHBoxLayout()
        a.addWidget(self.win_gif)
        a.addWidget(self.draw_gif)
        a.addWidget(self.loss_gif)
        self.a = QWidget()
        self.setLayout(a)
        
        self.win_gif.clicked.connect(self.winClick)
        self.draw_gif.clicked.connect(self.drawClick)
        self.loss_gif.clicked.connect(self.loseClick)
        #self.close_app.clicked.connect(self.quit)
        #self.sale_made.clicked.connect(self.sale_recorded)
    
    def winClick(self):
        self.ap = win_gif()
        self.ap.show()
        
    def drawClick(self):
        self.ap = draw_gif()
        self.ap.show()
    
    def loseClick(self):
        self.ap = lose_gif()
        self.ap.show() 
        
class win_gif(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        
        self.setGeometry(1250, 450, 600, 500)
        self.setWindowTitle('Win Gif')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)       
                
        #self.setPalette(QPalette(QColor("orange")))
        #self.setAutoFillBackground(True)
        self.congrats=QLabel()
        self.congrats_movie=QMovie("source.gif")
        
        
        grid_1=QHBoxLayout()#creates grid layout
        grid_1.addWidget(self.congrats)  

        self.grid_1 = QWidget()
        self.setLayout(grid_1)        
        
        self.congrats.setMovie(self.congrats_movie)
        self.congrats_movie.start()        
        self.wait(500)
        self.congrats_movie.stop()
        #self.congrats.clear()  
        
    def wait(self,microsec):
        loop = QEventLoop()
        QTimer.singleShot(microsec, loop.quit)
        loop.exec_()         

class draw_gif(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        
        self.setGeometry(1250, 450, 600, 500)
        self.setWindowTitle('DRAW Gif')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)          
        self.congrats=QLabel()
        self.congrats_movie=QMovie("giphy.gif")
        
        
        grid_1=QHBoxLayout()#creates grid layout
        grid_1.addWidget(self.congrats)  

        self.grid_1 = QWidget()
        self.setLayout(grid_1)        
        
        self.congrats.setMovie(self.congrats_movie)
        self.congrats_movie.start()        
        self.wait(500)
        self.congrats_movie.stop()
       
        
    def wait(self,microsec):
        loop = QEventLoop()
        QTimer.singleShot(microsec, loop.quit)
        loop.exec_()  
        
class lose_gif(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        
        self.setGeometry(1250, 150, 600, 500)
        self.setWindowTitle('lose Gif')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)           
        
        self.congrats=QLabel()
        self.congrats_movie=QMovie("lose.GIF")
        
        
        grid_1=QHBoxLayout()#creates grid layout
        grid_1.addWidget(self.congrats)  

        self.grid_1 = QWidget()
        self.setLayout(grid_1)        
        
        self.congrats.setMovie(self.congrats_movie)
        self.congrats_movie.start()        
        self.wait(500)
        self.congrats_movie.stop()
        #self.congrats.clear()  
        
    def wait(self,microsec):
        loop = QEventLoop()
        QTimer.singleShot(microsec, loop.quit)
        loop.exec_()         

#class draw_gif(QWidget):
    #def __init__(self, parent=None):
        #QWidget.__init__(self, parent)
        
        #self.setGeometry(450, 450, 600, 500)
        #self.setWindowTitle('DRAW Gif')
        #self.setPalette(QPalette(QColor("orange")))
        #self.setAutoFillBackground(True)
        #self.congrats=QLabel()
        #self.congrats_movie=QMovie("giphy.gif")
        
        
        #grid_1=QHBoxLayout()#creates grid layout
        #grid_1.addWidget(self.congrats)  

        #self.grid_1 = QWidget()
        #self.setLayout(grid_1)        
        
        #self.congrats.setMovie(self.congrats_movie)
        #self.congrats_movie.start()        
        #self.wait(500)
        #self.congrats_movie.stop()
        ##self.congrats.clear()  
        
    def wait(self,microsec):
        loop = QEventLoop()
        QTimer.singleShot(microsec, loop.quit)
        loop.exec_()          


def main():
    app = QApplication(sys.argv)
    abs_widget = end_game_gifs()
    abs_widget.show()
    sys.exit(app.exec_())

main()