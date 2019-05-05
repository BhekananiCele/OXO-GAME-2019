# OXO GAME- Game Over Windows
# Bhekanani Cele & Matthew Weppenaar
# 03 May 2019
# Added "enhancement" to the game

import sys
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtMultimedia import *
  
class Win_Window(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setGeometry(527, 180, 340, 380) 
        self.setWindowIcon(QIcon('icon.jpg')) #window  icon
        self.setWindowTitle('Game Over')  # window title    

        self.setPalette(QPalette(QColor("darkgray"))) #setting game window colour
        
        self.win=QLabel() #creating label 
        self.win_movie=QMovie("win.gif") #Creating Winning Effect - "enhancement" 
        
        vbox=QVBoxLayout() #creates horizontal box layout
        vbox.addWidget(self.win) #adding widget to the hozintal box layout
        self.setLayout(vbox)  
        
    #Method to play Movie Effect for winning -"enhancement" 
    def win_play_movie(self):
        self.play_mp3("GameOver_YouWin.mp3") #play mp3 -"enhancement"
        self.win.setMovie(self.win_movie)
        self.win_movie.start()  #"enhancement" - start win movie effect
        self.wait(10000) # wait for 10 seconds
        self.win_movie.stop() #"enhancement" - stop win movie effect
        self.close()  #close window 
        
    #method to wait for number of micro seconds   
    def wait(self,microsec):
        loop = QEventLoop()
        QTimer.singleShot(microsec, loop.quit)
        loop.exec_()
        
    #method to play mp3 files -"enhancement"
    def play_mp3(self,mp3_file):
        self.playlist = QMediaPlaylist()
        self.player = QMediaPlayer()        
        url = QUrl.fromLocalFile("./"+mp3_file)
        self.playlist.addMedia(QMediaContent(url))
        self.player.setPlaylist(self.playlist)
        self.player.play()  
        
class Draw_Window(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setGeometry(527, 180, 344, 428)
        self.setWindowTitle('Game Over')  # window title
        self.setWindowIcon(QIcon('icon.jpg')) #window  icon
        
        self.setPalette(QPalette(QColor("darkgray"))) #setting game window colour
        
        self.draw=QLabel() #creating label
        self.draw_movie=QMovie("tie.gif") #Creating Tie Effect - "enhancement" 
        
        vbox=QVBoxLayout() #creates horizontal box layout
        vbox.addWidget(self.draw) #adding widget to the hozintal box layout
        self.setLayout(vbox) 
        
    #Method to play Movie Effect for a Tie -"enhancement"
    def draw_play_movie(self): 
        win= Win_Window() # instance of Win_Window class
        win.play_mp3("GameOver.mp3")  #play mp3 -"enhancement"
        self.draw.setMovie(self.draw_movie)
        self.draw_movie.start() #"enhancement" - start Tie movie effect
        win.wait(10000) # wait for 10 seconds
        self.draw_movie.stop() #"enhancement" - stop Tie movie effect
        self.close() #close window 
        
class Lose_Window(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setGeometry(527, 180, 340, 380)
        self.setWindowTitle('Game Over')  # window title  
        self.setWindowIcon(QIcon('icon.jpg')) #window  icon
        
        self.setPalette(QPalette(QColor("darkgray"))) #setting game window colour
        
        self.lose=QLabel() #creating label
        self.lose_movie=QMovie("lose.gif") #Creating Losing Effect - "enhancement" 
        
        vbox=QHBoxLayout() #creates horizontal box layout
        vbox.addWidget(self.lose) #adding widget to the hozintal box layout
        self.setLayout(vbox)   
        
    #Method to play Movie Effect for Losing -"enhancement"
    def lose_play_movie(self): 
        win=Win_Window() # instance of Win_Window class
        win.play_mp3("GameOver_YouLose.mp3") #play mp3 -"enhancement"      
        self.lose.setMovie(self.lose_movie) 
        self.lose_movie.start()  #"enhancement" - start lose movie effect        
        win.wait(10000) # wait for 10 seconds
        self.lose_movie.stop() #"enhancement" - stop lose movie effect
        self.close()  #close window           