# OXO GAME 
# Bhekanani Cele
# 08 April 2019

import sys
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from text_to_speech import*
from GameClient import *
    
class oxo_game(QWidget,GameClient): 
    def __init__(self,parent=None):  #constructor
        QWidget.__init__(self,parent)
        GameClient.__init__(self)
        #GameServer.accept_clients(self)
        self.setGeometry(700,200,400,80) 
        self.setWindowTitle("OXO GAME CLIENT") # window title
        self.setWindowIcon(QIcon('icon.jpg')) #window  icon
        server=QLabel("Enter Server:")#creating label
        #formating label
        server.setStyleSheet('color: black')
        server.setFont(QFont("Arial",10,weight=QFont.Bold))   
        
        self.server_input=QLineEdit()#creating QLine edit for entering server to connect to
        #formating QLine edit
        self.server_input.setStyleSheet('color: red')
        self.server_input.setFont(QFont("Arial",10,weight=QFont.Bold))        
        
        self.connect=QPushButton("Connect")#creating label
        #formating label
        self.connect.setFont(QFont("Arial",10,weight=QFont.Bold))
        self.connect.setMinimumHeight(25)
        self.connect.setStyleSheet("color: darkblue")    
        
        your_shape_label=QLabel("Your Shape:")#creating label
        #formating label
        your_shape_label.setStyleSheet('color: black')
        your_shape_label.setFont(QFont("Arial",10,weight=QFont.Bold))
        
        self.exit=QPushButton("Exit Game")#creating label
        #formating label
        self.exit.setStyleSheet('color: darkblue')
        self.exit.setFont(QFont("Arial",10,weight=QFont.Bold))        
        self.exit.setMinimumHeight(35)        
        
        self.O_Shape=QPixmap("nought.png") # O_Shape picture
        self.X_Shape=QPixmap("cross.png") # X_Shape picture
        self.blank_Shape=QPixmap("blank.png") # blank picture
        
        self.your_shape=QLabel() # label to store players shape picture
        self.your_shape.setPixmap(self.blank_Shape) #insert picture to the shape label 
        
        self.please_wait=QLabel()
        self.please_wait_movie=QMovie("PleaseWait.gif")
        
        
        self.user_feedback=QTextEdit() # Text edit to display users instructions
        #formating label
        self.user_feedback.setStyleSheet('background-color: gray')
        self.user_feedback.setStyleSheet('color: darkblue')
        self.user_feedback.setFont(QFont("Arial",10,weight=QFont.Bold)) 
        
        self.position0=QPushButton()# creating QPushButton
        #formating QPushButton
        self.icon0 = QIcon(self.blank_Shape)
        self.position0.setIcon(self.icon0)
        self.position0.setIconSize(QSize(80, 80))
        
        self.position1=QPushButton()# creating QPushButton
        #formating QPushButton
        self.icon1 = QIcon(self.blank_Shape)
        self.position1.setIcon(self.icon1)
        self.position1.setIconSize(QSize(80, 80))        
        
        self.position2=QPushButton()# creating QPushButton
        #formating QPushButton
        self.icon2 = QIcon(self.blank_Shape)
        self.position2.setIcon(self.icon2)
        self.position2.setIconSize(QSize(80, 80))       
        
        self.position3=QPushButton()# creating QPushButton
        #formating QPushButton
        self.icon3 = QIcon(self.blank_Shape)
        self.position3.setIcon(self.icon3)
        self.position3.setIconSize(QSize(80, 80))      
        
        self.position4=QPushButton()# creating QPushButton
        #formating QPushButton
        self.icon4 = QIcon(self.blank_Shape)
        self.position4.setIcon(self.icon4)
        self.position4.setIconSize(QSize(80, 80))         
        
        self.position5=QPushButton()# creating QPushButton
        #formating QPushButton
        self.icon5 = QIcon(self.blank_Shape)
        self.position5.setIcon(self.icon5)
        self.position5.setIconSize(QSize(80, 80))       
        
        self.position6=QPushButton()# creating QPushButton
        #formating QPushButton
        self.icon6 = QIcon(self.blank_Shape)
        self.position6.setIcon(self.icon6)
        self.position6.setIconSize(QSize(80, 80))
        
        self.position7=QPushButton()# creating QPushButton
        #formating QPushButton
        self.icon7 = QIcon(self.blank_Shape)
        self.position7.setIcon(self.icon7) 
        self.position7.setIconSize(QSize(80, 80))        
        
        self.position8=QPushButton()# creating QPushButton
        #formating QPushButton
        self.icon8 = QIcon(self.blank_Shape)
        self.position8.setIcon(self.icon8)
        self.position8.setIconSize(QSize(80, 80))      
        
        grid_1=QGridLayout()#creates grid layout
        #adding widgets to the grid layout 
        grid_1.addWidget(server,0,0)
        grid_1.addWidget(self.server_input,0,1,1,2)
        grid_1.addWidget(self.connect,1,1)
        grid_1.addWidget(your_shape_label,2,0)
        grid_1.addWidget(self.your_shape,2,1)
        grid_1.addWidget(self.please_wait,2,2)
        grid_1.addWidget(self.user_feedback,3,0,1,3)
        grid_1_widget=QWidget()
        grid_1_widget.setLayout(grid_1)
        
        grid=QGridLayout()#creates grid layout
        #adding widgets to the grid layout 
        grid.addWidget(self.position0,0,0)
        grid.addWidget(self.position1,0,1)
        grid.addWidget(self.position2,0,2)
        grid.addWidget(self.position3,1,0)
        grid.addWidget(self.position4,1,1)
        grid.addWidget(self.position5,1,2)
        grid.addWidget(self.position6,2,0)
        grid.addWidget(self.position7,2,1)
        grid.addWidget(self.position8,2,2)
        grid.addWidget(self.exit,3,1)
        grid_widget=QWidget()
        grid_widget.setLayout(grid)
        
        vbox=QVBoxLayout()#creates vertical box layout
        #adding widgets to the vertical box layout 
        vbox.addWidget(grid_1_widget)
        vbox.addWidget(grid_widget)
        self.setLayout(vbox)        
        self.setPalette(QPalette(QColor("Dark Cyan")))
        
        self.button_group=QButtonGroup() #creating group buttons
        #adding buttons to the group buttons
        self.button_group.addButton(self.position0,0)
        self.button_group.addButton(self.position1,1)
        self.button_group.addButton(self.position2,2)
        self.button_group.addButton(self.position3,3)
        self.button_group.addButton(self.position4,4)
        self.button_group.addButton(self.position5,5)
        self.button_group.addButton(self.position6,6)
        self.button_group.addButton(self.position7,7)
        self.button_group.addButton(self.position8,8)
        
        self.board = [' '] * BOARD_SIZE
        self.shape = None
        
        self.disable_buttons()
        
        #signals connected to slots
        self.button_group.buttonClicked.connect(self.position_clicked)       
        self.exit.clicked.connect(self.exit_clicked)
        self.connect.clicked.connect(self.connect_clicked)
        
     #clear board method   
    def clear_board(self):
        self.board = [' '] * BOARD_SIZE    
        
    # a slots called when "button_group" push buttons are clicked    
    def position_clicked(self,button):
        clicked_position=self.button_group.id(button)
        self.send_message(str(clicked_position))  #sends message to the server       
        self.play_loop()
        
    # a slots called when "Exit Game" push button is clicked
    def exit_clicked(self):
        try:
            text_to_speech("Game Exitting")
        except:
            pass
        else:
            self.close()
            
    # a slots called when "Connect" push button is clicked
    def connect_clicked(self):
            try:
                self.connect_to_server(self.server_input.text())
                self.user_feedback.insertPlainText(">>Connected to the server successfuly!\n")
                self.user_feedback.moveCursor(QTextCursor.End)
                self.connect.setEnabled(False) # disable connect button
                self.please_wait.setMovie(self.please_wait_movie) 
                self.please_wait_movie.start()
                self.connect.setStyleSheet('background color: darkgray')
                try:
                    text_to_speech("Connected to the server successfuly!")
                except:
                    pass               
            except:
                self.user_feedback.insertPlainText(">>Error connecting to server!\n")
                self.user_feedback.moveCursor(QTextCursor.End)
                try:
                    text_to_speech("Error connecting to server!")
                except:
                    pass
            else:
                self.wait(5000)
                self.please_wait_movie.stop()
                self.please_wait.clear()
                self.play_loop()                
    # a slots called when LoopThread emit a signal push button is clicked
    def handle_message(self,msg):
        if msg[:msg.find(",")]=="new game":
            self.shape=msg[-1] #index shape
            if self.shape=="X":
                shape_name="cross"
                self.your_shape.setPixmap(self.X_Shape)
            else:
                shape_name="nought"
                self.your_shape.setPixmap(self.O_Shape)
            self.user_feedback.insertPlainText(">>New game is about to start, your character is a "+shape_name+" shape.\n") #lets the players know their shape
            self.user_feedback.moveCursor(QTextCursor.End)
            try:
                text_to_speech("New game is about to start, your character is a "+shape_name+" shape.") #lets the players know their shape
            except:
                pass
        elif msg=="your move":
            self.display_board()
            self.user_feedback.insertPlainText(">>It's your turn to move.\n")
            self.user_feedback.moveCursor(QTextCursor.End)
            self.enable_buttons()
            self.enable_buttons_color()
            try:
                text_to_speech("It's your turn to move.") #lets the players know their turn to move
            except:
                pass
        elif msg=="opponents move": 
            self.user_feedback.insertPlainText(">>It's the opponent turn to move.\n") #lets the players know it their opponent turn to move 
            self.user_feedback.moveCursor(QTextCursor.End)
            self.please_wait.setMovie(self.please_wait_movie)
            self.please_wait_movie.start()
            self.disable_buttons()
            try:
                text_to_speech("It's the opponent turn to move") #lets the players know their turn to move
            except:
                pass
            self.wait(500)
            self.please_wait_movie.stop()
            self.please_wait.clear()            
            self.play_loop()
            self.display_board()
        elif msg[:msg.find(",")]=="valid move":
            self.shape=msg[-3] #index shape
            position=int(msg[-1]) #index position
            self.board[position]= self.shape #insert shape to the board         
            self.display_board()
        elif msg=="invalid move":
            self.user_feedback.insertPlainText(">>Invalid move.\n") #lets the player know that an invalid move was made
            self.user_feedback.moveCursor(QTextCursor.End)
            try:
                text_to_speech("Invalid move.") #lets the player know that an invalid move was made
            except:
                pass                        
        elif msg[:msg.find(",")]=="game over":
            results=msg[-1] #index shape
            if results=="X":
                _shape_name_="cross"
                self.user_feedback.insertPlainText(">>Game Over, the winner is the player with the "+_shape_name_+" shape.\n")   #lets the players know who is the winner
                self.user_feedback.moveCursor(QTextCursor.End)
                try:
                    text_to_speech("Game Over, the winner is the player with the "+_shape_name_+" shape.")   #lets the players know who is the winner
                except:
                    pass                                    
            elif results=="O":
                _shape_name_="nought"
                self.user_feedback.insertPlainText(">>Game Over, the winner is the player with the "+_shape_name_+" shape.\n")   #lets the players know who is the winner
                self.user_feedback.moveCursor(QTextCursor.End)
                try:
                    text_to_speech("Game Over, the winner is the player with the "+_shape_name_+" shape.")   #lets the players know who is the winner
                except:
                    pass                    
            else: 
                self.user_feedback.insertPlainText(">>Game Over, no one won. It is a Tie.\n") #lets the players know that no one won, it is a tie
                self.user_feedback.moveCursor(QTextCursor.End)
                try:
                    text_to_speech("Game Over, no one won. It is a Tie") #lets the players know that no one won, it is a tie
                except:
                    pass                
        elif msg=="play again":
            try:
                text_to_speech("Do you want to play again?") #Ask the players whether they want to play again
            except:
                pass             
            answer=QMessageBox.question(self,"Game Over", "Do you want to play again?",QMessageBox.Yes | QMessageBox.No) #Ask the players whether they want to play again 
            if answer==QMessageBox.Yes:
                answer="y"
                self.send_message(answer) #lets the players input their answer and sends message to the server
                self.clear_board() # clear board if the answer from the player is "yes"
                self.display_board()
            else:
                answer="n"
                self.send_message(answer)
        elif msg=="exit game":
            self.user_feedback.insertPlainText(">>Game is about to be closed, one or both of the players doesn't want to play again.\n") #lets the players know that the game has been closed
            self.user_feedback.moveCursor(QTextCursor.End)
            try:
                text_to_speech("Game is about to be closed, one or both of the players doesn't want to play again.") #lets the players know that the game has been closed
            except:
                pass
            self.close()
            
    # display board method      
    def display_board(self):
        for move in range(9):
            if self.board[move]=="X" and move==0:
                self.icon0 = QIcon(self.X_Shape)
                self.position0.setIcon(self.icon0)                    
            elif self.board[move]=="O" and move==0:
                self.icon0 = QIcon(self.O_Shape)
                self.position0.setIcon(self.icon0)
            elif self.board[move]==" " and move==0:
                self.icon0 = QIcon(self.blank_Shape)
                self.position0.setIcon(self.icon0)   
            elif self.board[move]=="X" and move==1:
                self.icon1 = QIcon(self.X_Shape)
                self.position1.setIcon(self.icon1)                    
            elif self.board[move]=="O" and move==1:
                self.icon1 = QIcon(self.O_Shape)
                self.position1.setIcon(self.icon1)
            elif self.board[move]==" " and move==1:
                self.icon1 = QIcon(self.blank_Shape)
                self.position1.setIcon(self.icon1)
            elif self.board[move]=="X" and move==2:
                self.icon2 = QIcon(self.X_Shape)
                self.position2.setIcon(self.icon2)                    
            elif self.board[move]=="O" and move==2:
                self.icon2 = QIcon(self.O_Shape)
                self.position2.setIcon(self.icon2)
            elif self.board[move]==" " and move==2:
                self.icon2 = QIcon(self.blank_Shape)
                self.position2.setIcon(self.icon2) 
            elif self.board[move]=="X" and move==3:
                self.icon3 = QIcon(self.X_Shape)
                self.position3.setIcon(self.icon3)                    
            elif self.board[move]=="O" and move==3:
                self.icon3 = QIcon(self.O_Shape)
                self.position3.setIcon(self.icon3)
            elif self.board[move]==" " and move==3:
                self.icon3 = QIcon(self.blank_Shape)
                self.position3.setIcon(self.icon3) 
            elif self.board[move]=="X" and move==4:
                self.icon4 = QIcon(self.X_Shape)
                self.position4.setIcon(self.icon4)                    
            elif self.board[move]=="O" and move==4:
                self.icon4 = QIcon(self.O_Shape)
                self.position4.setIcon(self.icon4)
            elif self.board[move]==" " and move==4:
                self.icon4 = QIcon(self.blank_Shape)
                self.position4.setIcon(self.icon4)   
            elif self.board[move]=="X" and move==5:
                self.icon5 = QIcon(self.X_Shape)
                self.position5.setIcon(self.icon5)                    
            elif self.board[move]=="O" and move==5:
                self.icon5 = QIcon(self.O_Shape)
                self.position5.setIcon(self.icon5)
            elif self.board[move]==" " and move==5:
                self.icon5 = QIcon(self.blank_Shape)
                self.position5.setIcon(self.icon5)   
            elif self.board[move]=="X" and move==6:
                self.icon6 = QIcon(self.X_Shape)
                self.position6.setIcon(self.icon6)                    
            elif self.board[move]=="O" and move==6:
                self.icon6 = QIcon(self.O_Shape)
                self.position6.setIcon(self.icon6)
            elif self.board[move]==" " and move==6:
                self.icon6 = QIcon(self.blank_Shape)
                self.position6.setIcon(self.icon6) 
            elif self.board[move]=="X" and move==7:
                self.icon7 = QIcon(self.X_Shape)
                self.position7.setIcon(self.icon7)                    
            elif self.board[move]=="O" and move==7:
                self.icon7 = QIcon(self.O_Shape)
                self.position7.setIcon(self.icon7)
            elif self.board[move]==" " and move==7:
                self.icon7 = QIcon(self.blank_Shape)
                self.position7.setIcon(self.icon7)  
            elif self.board[move]=="X" and move==8:
                self.icon8 = QIcon(self.X_Shape)
                self.position8.setIcon(self.icon8)                    
            elif self.board[move]=="O" and move==8:
                self.icon8 = QIcon(self.O_Shape)
                self.position8.setIcon(self.icon8)
            elif self.board[move]==" " and move==8:
                self.icon8 = QIcon(self.blank_Shape)
                self.position8.setIcon(self.icon8)                
    def wait(self,microsec):
        loop = QEventLoop()
        QTimer.singleShot(microsec, loop.quit)
        loop.exec_()          
    def play_loop(self):
        while True:
            msg = self.receive_message()
            if len(msg): 
                self.handle_message(msg)
                if msg=="your move" or msg=="opponents move":break
            else: break    
            
    #disable grid buttons method
    def disable_buttons(self):
        self.position0.setEnabled(False)
        self.position1.setEnabled(False)
        self.position2.setEnabled(False)
        self.position3.setEnabled(False)
        self.position4.setEnabled(False)
        self.position5.setEnabled(False)
        self.position6.setEnabled(False)
        self.position7.setEnabled(False)
        self.position8.setEnabled(False)
        
    #enable grid buttons method    
    def enable_buttons(self):
        self.position0.setDisabled(False)
        self.position1.setDisabled(False)
        self.position2.setDisabled(False)
        self.position3.setDisabled(False)
        self.position4.setDisabled(False)                   
        self.position5.setDisabled(False)             
        self.position6.setDisabled(False)
        self.position7.setDisabled(False)
        self.position8.setDisabled(False)
        
    #enable grid buttons colour method     
    def enable_buttons_color(self):
        self.position0.setStyleSheet('color: darkblue;background-color: None')
        self.position0.setStyleSheet('color: darkblue;background-color: None') 
        self.position2.setStyleSheet('color: darkblue;background-color: None')  
        self.position3.setStyleSheet('color: darkblue;background-color: None') 
        self.position4.setStyleSheet('color: darkblue;background-color: None')  
        self.position5.setStyleSheet('color: darkblue;background-color: None')
        self.position6.setStyleSheet('color: darkblue;background-color: None')
        self.position7.setStyleSheet('color: darkblue;background-color: None')  
        self.position8.setStyleSheet('color: darkblue;background-color: None') 
        
def main():
    app=QApplication(sys.argv)
    game=oxo_game() # instance of oxo_game class
    game.show() # show instance of oxo_game class
    game.user_feedback.insertPlainText(">>Enter server to connect to and click the connect button to connect to that server.\n")
    try:
        text_to_speech("Enter server to connect to and click the connect button to connect to that server.")
    except:
        pass
    sys.exit(app.exec_())
if __name__=="__main__":
    main()