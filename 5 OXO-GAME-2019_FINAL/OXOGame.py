# OXO GAME 
# Bhekanani Cele & Matthew Weppenaar
# 08 April 2019

import os
import sys
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from GameClient import *
from Game_Over import*  #"enhancement" - Game Over windows
from check_running_program import*

class Instruction_Window(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setGeometry(300, 40, 1280, 720) 
        self.setFixedSize(1280, 720)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint) #"enhancement"- disabling maximise window flag
        self.setWindowIcon(QIcon('icon.jpg')) #window  icon
        self.setWindowTitle('Instructions')  # window title    

        self.setPalette(QPalette(QColor("darkgray"))) #setting game window colour
        
        self.instructions_label=QLabel() #creating label 
        self.instructions_picture=QPixmap("Instructions.png")
        self.instructions_label.setPixmap(self.instructions_picture)
        
        vbox=QVBoxLayout() #creates horizontal box layout
        vbox.addWidget(self.instructions_label) #adding widget to the hozintal box layout
        self.setLayout(vbox)  
    
    # a slots called when "Instructions" push button is clicked
    def instructions_clicked(self):
        self.show()
        
class OXO_game(QWidget,GameClient): 
    def __init__(self,parent=None):  #constructor
        QWidget.__init__(self,parent)
        GameClient.__init__(self)
        self.setGeometry(500,40,420,820)
        self.setFixedSize(420,840)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint) #"enhancement"- disabling maximise window flag
        self.setWindowTitle("OXO GAME CLIENT") # window title
        self.setWindowIcon(QIcon('icon.jpg')) #window  icon
        self.server=QLabel("Enter Server:")#creating label
        #formating label
        self.server.setFont(QFont("Arial",10,weight=QFont.Bold))   
        
        self.server_input=QLineEdit()#creating QLine edit for entering server to connect to
        self.server_input.setToolTip("Enter Server IP Address") #"enhancement"- set tool tip
        #formating QLine edit
        self.server_input.setStyleSheet('color: red')
        self.server_input.setFont(QFont("Arial",10,weight=QFont.Bold))        
        
        self.connect=QPushButton("Connect")#creating QPushButton
        #formating button
        self.connect.setFont(QFont("Arial",10,weight=QFont.Bold))
        self.connect.setMinimumHeight(25)
        self.connect.setStyleSheet("color: darkblue") 
        self.connect.setMinimumHeight(30)
        self.connect.setMaximumWidth(200) 
        self.connect.setToolTip("Connect To The Server") #"enhancement"- set tool tip
        
        self.start_server=QPushButton("Start Server")#creating QPushButton
        #formating button
        self.start_server.setToolTip("Start Server To Connect To")
        self.start_server.setFont(QFont("Arial",10,weight=QFont.Bold))
        self.start_server.setMinimumHeight(25)
        self.start_server.setStyleSheet("color: darkblue") 
        self.start_server.setMinimumHeight(30)
        self.start_server.setMaximumWidth(200)         
        
        self.mute=QPixmap("mute.png") #mute image
        self.un_mute=QPixmap("un_mute.png") #mute image    
        
        self.your_shape_label=QLabel("Your Shape:")#creating label
        #formating label
        self.your_shape_label.setFont(QFont("Arial",10,weight=QFont.Bold))
        
        self.exit=QPushButton("Exit Game")#creating QPushButton
        #formating button
        self.exit.setStyleSheet('color: darkblue')
        self.exit.setFont(QFont("Arial",10,weight=QFont.Bold))        
        self.exit.setMinimumHeight(35)
        self.exit.setMaximumWidth(110)
        self.exit.setToolTip("Close Game") #"enhancement"- set tool tip
        
        self.instructions=QPushButton("Instructions")#creating QPushButton
        #formating button
        self.instructions.setStyleSheet('color: darkblue')
        self.instructions.setFont(QFont("Arial",10,weight=QFont.Bold))        
        self.instructions.setMinimumHeight(35)
        self.instructions.setMaximumWidth(110)
        self.instructions.setToolTip("Game Instructions") #"enhancement"- set tool tip        
        
        self.O_Shape=QPixmap("nought.png") # O_Shape picture
        self.X_Shape=QPixmap("cross.png") # X_Shape picture
        self.blank_Shape= QPixmap("blank.png") # blank picture
        self.OXO=QPixmap("OXO.png") #OXO picture
        
        self.OXO_label=QLabel() # creating label to store OXO picture
        #formating label
        self.OXO_label.setPixmap(self.OXO) #insert picture to the OXO label 
        self.OXO_label.setAlignment(Qt.AlignCenter)
        
        self.your_shape=QLabel() # label to store players shape picture
        self.your_shape.setPixmap(self.blank_Shape) #insert picture to the shape label 
        
        self.effect=QLabel() # creating label to store effects
        
        #Creating Effects - "enhancement" 
        self.please_wait_movie=QMovie("PleaseWait.gif")
        
        self.user_feedback=QTextEdit() # Text edit to display users instructions
        #formating Text edit
        self.user_feedback.setReadOnly(True) #"enhancement" - make Text edit to read only
        self.user_feedback.setStyleSheet('color: darkblue;background-color: lightgray')
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
        
        #players scores
        self.X_Shape_Score=0 
        self.O_Shape_Score=0 
        
        self.score=QLabel("Score:") #creating label
        #formating label
        self.score.setFont(QFont("Arial",10,weight=QFont.Bold)) 
        
        self.O_Shape_Score_label=QLabel("Nought Shape: "+str(self.O_Shape_Score)) #creating label
        #formating label
        self.O_Shape_Score_label.setFont(QFont("Arial",10,weight=QFont.Bold))
        
        self.X_Shape_Score_label=QLabel("Cross Shape: "+str(self.X_Shape_Score)) #creating label
        #formating label
        self.X_Shape_Score_label.setFont(QFont("Arial",10,weight=QFont.Bold))
        
        #"enhancement" - setting tool tips for all move buttons
        self.position0.setToolTip("Place Move")
        self.position1.setToolTip("Place Move")
        self.position2.setToolTip("Place Move")
        self.position3.setToolTip("Place Move")
        self.position4.setToolTip("Place Move")
        self.position5.setToolTip("Place Move")
        self.position6.setToolTip("Place Move")
        self.position7.setToolTip("Place Move")
        self.position8.setToolTip("Place Move")
        
        self.colour=QLabel("Game Colour:") #creating label
        #formating label
        self.colour.setFont(QFont("Arial",10,weight=QFont.Bold))
        
        #create colour Combo box
        self.colour_combo=QComboBox()
        # formating combo box 
        self.colour_combo.setToolTip("Change Theme") #"enhancement"- set tool tip
        self.colour_combo.setStyleSheet('color: darkblue')  
        self.colour_combo.setFont(QFont("Arial",10,weight=QFont.Bold))   
        #add items to the colour combo
        self.colour_combo.addItem("Dark Cyan")
        self.colour_combo.addItem("Dark Mode")
        self.colour_combo.addItem("Dark Magenta")
        self.colour_combo.addItem("Dark Red")
        self.colour_combo.addItem("Dark Blue")
        self.colour_combo.addItem("Dark Orange")     
        
        self.game_server_msg=QLabel(">>>>>>>>>>>> User FeedBack <<<<<<<<<<<<<") #create label
        #formating label
        self.game_server_msg.setAlignment(Qt.AlignCenter)
        
        self.game_board=QLabel(">>>>>>>>>>>>>> Game Board <<<<<<<<<<<<<<") #create label
        #formating label
        self.game_board.setAlignment(Qt.AlignCenter)        
        
        grid_1=QGridLayout()#creates grid layout
        #adding widgets to the grid layout 
        grid_1.addWidget(self.server,0,0)
        grid_1.addWidget(self.server_input,0,1,1,2)
        grid_1.addWidget(self.connect,1,1)
        grid_1.addWidget(self.start_server,1,2)
        grid_1.addWidget(self.score,4,0)
        grid_1.addWidget(self.X_Shape_Score_label,4,1)
        grid_1.addWidget(self.O_Shape_Score_label,4,2)
        grid_1.addWidget(self.your_shape_label,2,0)
        grid_1.addWidget(self.your_shape,2,1)
        grid_1.addWidget(self.effect,2,2)
        grid_1.addWidget(self.colour,3,0)
        grid_1.addWidget(self.colour_combo,3,1)        
        grid_1.addWidget(self.game_server_msg,5,0,1,3)
        grid_1.addWidget(self.user_feedback,6,0,1,3)
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
        
        self.grid_widget=QGroupBox() #creating group box
        #formating group box
        self.grid_widget.setObjectName("board")
        self.grid_widget.setStyleSheet("QGroupBox#board {font-weight: bold;font-size:14px;border: 2px solid orange}")
        self.grid_widget.setLayout(grid) #setting layout
        
        hbox=QHBoxLayout()#creates horizontal box layout
        #adding widgets to the hozintal box layout
        hbox.addWidget(self.instructions)
        hbox.addWidget(self.exit)
        hbox_widget=QWidget()
        hbox_widget.setLayout(hbox)

        vbox=QVBoxLayout()#creates vertical box layout
        #adding widgets to the vertical box layout 
        vbox.addWidget(self.OXO_label)
        vbox.addWidget(grid_1_widget)
        vbox.addWidget(self.game_board)
        vbox.addWidget(self.grid_widget)
        vbox.addWidget(hbox_widget)
        self.setLayout(vbox)        
        
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

        self.board = [' '] * BOARD_SIZE #Board list
        self.shape = None 
        self.mute_status=False #mute status
        self.disable_buttons() #"enhancement" - disabling buttons for placing moves since it a not yet any player turn to move 
        
        self.text_colour("orange") #setting game text colour
        self.setPalette(QPalette(QColor(self.colour_combo.currentText()))) #setting game window colour
       
        #signals connected to slots
        self.button_group.buttonClicked.connect(self.position_clicked)       
        self.exit.clicked.connect(self.exit_clicked)
        self.connect.clicked.connect(self.connect_clicked)
        self.colour_combo.currentTextChanged.connect(self.combo_changed)
        self.start_server.clicked.connect(self.start_server_clicked)
        
    
    # a slots called when "Start Server" push button is clicked
    def start_server_clicked(self):
        if checkIfProcessRunning("OXOGameServer.exe")!=True:
            try:
                os.startfile("OXOGameServer.exe")
                self.user_feedback.insertPlainText('\n>>Server started successfuly!')
                self.user_feedback.moveCursor(QTextCursor.End)
            except:
                self.user_feedback.insertPlainText('\n>>"OXOGameServer.exe" could not be found!')
                self.user_feedback.moveCursor(QTextCursor.End)
        else:
            self.user_feedback.insertPlainText('\n>>Server has already started!')
            self.user_feedback.moveCursor(QTextCursor.End)
    #text colour change method
    def text_colour(self,colour): #"enhancement" - method
        self.O_Shape_Score_label.setStyleSheet('color: '+str(colour))
        self.X_Shape_Score_label.setStyleSheet('color: '+str(colour))
        self.score.setStyleSheet('color: '+str(colour))
        self.your_shape_label.setStyleSheet('color: '+str(colour))
        self.server.setStyleSheet('color: '+str(colour))
        self.colour.setStyleSheet('color: '+str(colour))       
        self.game_board.setStyleSheet("color: "+str(colour)+";font-weight: bold;font-size:13px")
        self.game_server_msg.setStyleSheet("color: "+str(colour)+";font-weight: bold;font-size:13px")
        self.grid_widget.setStyleSheet("QGroupBox#board {font-weight: bold;font-size:14px;border: 2px solid "+str(colour)+"}")
        
    # a slots called when "combo box" text is Changed  
    def combo_changed(self): #"enhancement" - method
        if self.colour_combo.currentText()=="Dark Mode":
            self.text_colour("Lightgreen") #setting game text colour
        elif self.colour_combo.currentText()=="Dark Magenta":
            self.text_colour("Cyan") #setting game text colour
        elif self.colour_combo.currentText()=="Dark Cyan":
            self.text_colour("Orange")  #setting game text colour
        elif self.colour_combo.currentText()=="Dark Orange":
            self.text_colour("LightGray")  #setting game text colour
        elif self.colour_combo.currentText()=="Dark Blue":
            self.text_colour("White")   #setting game text colour           
        elif self.colour_combo.currentText()=="Dark Red":
            self.text_colour("Green") #setting game text colour
            
        self.setPalette(QPalette(QColor(self.colour_combo.currentText()))) #setting game window colour

    #clear board method   
    def clear_board(self):
        self.board = [' '] * BOARD_SIZE    
        
    # a slots called when "button_group" push buttons are clicked    
    def position_clicked(self,button):
        clicked_position=self.button_group.id(button)
        try:
            self.send_message(str(clicked_position))  #sends message to the server
        except:
            self.server_disconnected() # alert the player that the sever has been disconnected
        else:
            try:
                self.play_loop() #Get message from the server
            except:
                self.server_disconnected() # alert the player that the sever has been disconnected
  
    # a slots called when "Exit Game" push button is clicked
    def exit_clicked(self):
        self.close()    

    # a slots called when "Connect" push button is clicked
    def connect_clicked(self):
            try:
                self.connect_to_server(self.server_input.text()) #connect to the server
                self.user_feedback.insertPlainText("\n>>Connected to the server successfuly!") #lets the players know they have connected to the server successfuly
                self.connect.setText("Connected")
                self.user_feedback.moveCursor(QTextCursor.End) #"enhancement" - autoscroll text eqit
                self.connect.setEnabled(False) # "enhancement" - disable connect button
                self.connect.setStyleSheet('color: darkgray')             
            except:
                self.user_feedback.insertPlainText("\n>>Error connecting to server!") #lets the players know they have not connected to the server successfuly
                self.user_feedback.moveCursor(QTextCursor.End) #"enhancement" - autoscroll text eqit
            else:
                #"enhancement" - start please wait movie effect 
                self.effect.setMovie(self.please_wait_movie) 
                self.please_wait_movie.start()   
                #wait for 5 seconds
                self.wait(5000)
                #"enhancement" - stop please wait movie effect
                self.please_wait_movie.stop()
                self.effect.clear()#clear effect label   
                try:
                    self.play_loop() #Get message from the server
                except:
                    self.server_disconnected() # alert the player that the sever has been disconnected
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
            self.user_feedback.insertPlainText("\n>>New game is about to start, your character is a "+shape_name+" shape.") #lets the players know their shape
            self.user_feedback.moveCursor(QTextCursor.End) #"enhancement" - autoscroll text eqit
                
        elif msg=="your move":
            self.display_board() # display Board
            self.user_feedback.insertPlainText("\n>>It's your turn to move.") #lets the players know it their turn to move
            self.user_feedback.moveCursor(QTextCursor.End) #"enhancement" - autoscroll text eqit
            self.enable_buttons() #"enhancement" - enabling buttons for placing moves since it player turn to move 
            
        elif msg=="opponents move": 
            self.user_feedback.insertPlainText("\n>>It's the opponent turn to move.") #lets the players know it their opponent turn to move 
            self.user_feedback.moveCursor(QTextCursor.End) #"enhancement" - autoscroll text eqit
            self.disable_buttons() #"enhancement" - disabling buttons for placing moves since it a not yet any player turn to move    
            #"enhancement" - start please wait movie effect 
            self.effect.setMovie(self.please_wait_movie) 
            self.please_wait_movie.start()   
            #wait for 250 micro seconds
            self.wait(250)
            #"enhancement" - stop please wait movie effect
            self.please_wait_movie.stop()
            self.effect.clear()#clear effect label
                
        elif msg[:msg.find(",")]=="valid move":
            shape=msg[-3] #index shape
            position=int(msg[-1]) #index position
            self.board[position]= shape #insert shape to the board         
            self.display_board() #display the game board
            
        elif msg=="invalid move":
            self.user_feedback.insertPlainText("\n>>Invalid move.") #lets the player know that an invalid move was made
            self.user_feedback.moveCursor(QTextCursor.End) #"enhancement" - autoscroll text eqit
            
        elif msg[:msg.find(",")]=="game over":
            #"enhancement"
            #get window x and y geometry
            x_geo=self.geometry().x()+27
            y_geo=self.geometry().y()+160
            
            results=msg[-1] #index shape
            if results=="X":self.X_Shape_Score+=1
            elif results=="O":self.O_Shape_Score+=1
            
            if results=="X" and self.shape=="X":
                self.O_Shape_Score_label.setText("Nought Shape: "+str(self.O_Shape_Score))
                self.X_Shape_Score_label.setText("Cross Shape: "+str(self.X_Shape_Score))
                win=Win_Window()
                win.setGeometry(x_geo,y_geo,340, 380) #set window geometry
                win.show()
                win.win_play_movie() #play Movie Effect for Winning -"enhancement"
            elif results=="O" and self.shape=="O":
                self.O_Shape_Score_label.setText("Nought Shape: "+str(self.O_Shape_Score))
                self.X_Shape_Score_label.setText("Cross Shape: "+str(self.X_Shape_Score))              
                win=Win_Window() # instance of Win_Window class
                win.setGeometry(x_geo,y_geo,340, 380) #set window geometry
                win.show()  
                win.win_play_movie() #play Movie Effect for Winning -"enhancement"
            elif results=="X" and self.shape=="O":
                self.O_Shape_Score_label.setText("Nought Shape: "+str(self.O_Shape_Score))
                self.X_Shape_Score_label.setText("Cross Shape: "+str(self.X_Shape_Score))                 
                win=Lose_Window() # instance of Lose_Window class
                win.setGeometry(x_geo,y_geo,340, 380) #set window geometry
                win.show()
                win.lose_play_movie() #play Movie Effect for Losing -"enhancement"
            elif results=="O" and self.shape=="X":
                self.O_Shape_Score_label.setText("Nought Shape: "+str(self.O_Shape_Score))
                self.X_Shape_Score_label.setText("Cross Shape: "+str(self.X_Shape_Score))                 
                win=Lose_Window() # instance of Lose_Window class
                win.setGeometry(x_geo,y_geo,340, 380) #set window geometry
                win.show() 
                win.lose_play_movie() #play Movie Effect for Losing -"enhancement"
            else:
                win=Draw_Window() # instance of Draw_Window class
                win.setGeometry(x_geo,y_geo,344, 428) #set window geometry
                win.show()
                win.draw_play_movie() #play Movie Effect for a Tie -"enhancement"
                
        elif msg=="play again":           
            answer=QMessageBox.question(self,"Game Over", "Do you want to play again?",QMessageBox.Yes | QMessageBox.No) #Pop up Dialog to Ask the players whether they want to play again 
            if answer==QMessageBox.Yes:
                answer="y"
                try:
                    self.send_message(answer) #send message to the server
                except:
                    self.server_disconnected() # alert the player that the sever has been disconnected                       
                else:               
                    self.clear_board() # clear board if the answer from the player is "yes"
                    self.display_board() #display the game board
            else:
                answer="n"
                try:
                    self.send_message(answer) #send message to the server
                except:
                    self.server_disconnected() # alert the player that the sever has been disconnected
        elif msg=="exit game":
            self.user_feedback.insertPlainText("\n>>Game is about to close, one or both of the players doesn't want to play again.") #lets the players know that the game is about to close
            self.user_feedback.moveCursor(QTextCursor.End) #"enhancement" - autoscroll text eqit
            if checkIfProcessRunning("OXOGameServer.exe"): #check if the program is running
                try:
                    os.system("TASKKILL /F /IM OXOGameServer.exe") #close the program
                except:
                    pass
            self.wait(2000) #wait for 2 second
            self.close() #close window
            
    #method to alert the user when the server has been disconnected       
    def server_disconnected(self) :
        self.user_feedback.insertPlainText("\n>>Server Disconnected. An existing connection was forcibly closed by the remote host!")
        self.socket.close()
        self.user_feedback.moveCursor(QTextCursor.End)
        self.connect.setEnabled(True)
        self.connect.setText("Connect")
        self.connect.setStyleSheet("color: darkblue")
        self.your_shape.setPixmap(self.blank_Shape)
        self.clear_board()
        self.display_board()
        self.disable_buttons()
        self.socket = socket(AF_INET, SOCK_STREAM)    
        
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
                
    #method to wait for number of micro seconds
    def wait(self,microsec):
        loop = QEventLoop()
        QTimer.singleShot(microsec, loop.quit)
        loop.exec_()  
    # method to get message from the server
    def play_loop(self):
        while True:
            msg = self.receive_message()
            if len(msg): 
                self.handle_message(msg)
                if msg=="your move":break
            else: 
                self.opponent_disconnected() # alert the player that their opponent has  disconnected from the server
                break 
    #method to alert the user when the opponent has disconnected from the server     
    def opponent_disconnected(self):
        self.user_feedback.insertPlainText("\n>>Your opponnent has disconnected from the server!")
        self.socket.close()
        self.user_feedback.moveCursor(QTextCursor.End)
        self.connect.setEnabled(True)
        self.connect.setText("Connect")
        self.connect.setStyleSheet("color: darkblue")
        self.your_shape.setPixmap(self.blank_Shape)
        self.clear_board()
        self.display_board()
        self.disable_buttons()
        self.socket = socket(AF_INET, SOCK_STREAM)  
        
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

#main function      
def main():
    app=QApplication(sys.argv)
    game=OXO_game() # instance of OXO_game class
    game.show() # show instance of OXO_game class
    game.user_feedback.insertPlainText(">>Enter server to connect to and click the connect button to connect to that server.") # Player instructions
    game.user_feedback.moveCursor(QTextCursor.End)
    instruc=Instruction_Window() # instance of Instruction_Window class
    game.instructions.clicked.connect(instruc.instructions_clicked) #connect signal to slot
    sys.exit(app.exec_())
if __name__=="__main__":
    main()