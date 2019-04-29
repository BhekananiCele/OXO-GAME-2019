# OXO GAME 
# Bhekanani Cele
# 08 April 2019

import sys
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*

class oxo_game(QWidget): 
    def __init__(self,parent=None):  #constructor
        QWidget.__init__(self,parent) 
        self.setGeometry(700,200,400,80) 
        self.setWindowTitle("OXO GAME CLIENT") # window title
        
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
        self.connect.setStyleSheet('color: darkblue')
        self.connect.setFont(QFont("Arial",10,weight=QFont.Bold))
        self.connect.setMinimumHeight(25)
                             
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
        self.your_shape.setPixmap(self.X_Shape) #insert picture to the shape label 
        
        self.user_feedback=QTextEdit() # label to store users instructions
        #formating label
        #self.user_feedback.moveCursor(QTextCursor.End)
        self.user_feedback.setStyleSheet('color: darkblue')
        self.user_feedback.setFont(QFont("Arial",10,weight=QFont.Bold)) 
          
        self.position0=QPushButton()# creating QPushButton
        #formating QPushButton
        self.icon0 = QIcon(self.X_Shape)
        self.position0.setIcon(self.icon0)
        self.position0.setIconSize(QSize(80, 80))
        
        self.position1=QPushButton()# creating QPushButton
        #formating QPushButton
        self.icon1 = QIcon(self.blank_Shape)
        self.position1.setIcon(self.icon1)
        self.position1.setIconSize(QSize(80, 80))
        
        self.position2=QPushButton()# creating QPushButton
        #formating QPushButton
        self.icon2 = QIcon(self.O_Shape)
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
        self.icon7 = QIcon(self.O_Shape)
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
        
        #signals connected to slots
        self.button_group.buttonClicked.connect(self.position_clicked)       
        self.exit.clicked.connect(self.exit_clicked)
        self.connect.clicked.connect(self.connect_clicked)
        
    # a slots called when "button_group" push buttons are clicked    
    def position_clicked(self,button):
        position_button_clicked=self.button_group.id(button)
        self.user_feedback.insertPlainText("Button {} clicked\n".format(position_button_clicked+1))
        self.user_feedback.moveCursor(QTextCursor.End)
        
    # a slots called when "Exit Game" push button is clicked
    def exit_clicked(self):
        self.close()
    
    # a slots called when "Connect" push button is clicked
    def connect_clicked(self):
        self.user_feedback.insertPlainText("Connect button clicked\n")
        self.user_feedback.moveCursor(QTextCursor.End)
        
def main():
    app=QApplication(sys.argv)
    game=oxo_game() # instance of oxo_game class
    game.show() # show instance of oxo_game class
    sys.exit(app.exec_())
if __name__=="__main__":
    main()