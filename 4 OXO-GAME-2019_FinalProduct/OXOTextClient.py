from GameClient import *
import time

class OXOTextClient(GameClient):

    def __init__(self):
        GameClient.__init__(self)
        self.board = [' '] * BOARD_SIZE
        self.shape = None
        self.position= None
        self.results=None
        self.answer=None
    def clear_board(self):
        self.board = [' '] * BOARD_SIZE

    def input_server(self):
        return input('enter server:')

    def input_move(self):
        return input('enter move(0-8):')

    def input_play_again(self):
        return input('play again(y/n):')

    def display_board(self):
        if self.board[0]==" "and self.board[1]==" "and self.board[2]==" " and self.board[3]==" "and self.board[4]==" "and self.board[5]==" "and self.board[6]==" "and self.board[7]==" "and self.board[8]==" ":
            a='0'
            b='1'
            c='2'
            d='3'
            e='4'
            f='5'
            g='6'
            h='7'
            i='8'                
            print('+-----+-----+-----+')
            print('|'+'  '+a+'  '+'|'+'  '+b+'  '+'|'+'  '+c+'  '+'|')
            print('+-----+-----+-----+')
            print('|'+'  '+d+'  '+'|'+'  '+e+'  '+'|'+'  '+f+'  '+'|')  
            print('+-----+-----+-----+')        
            print('|'+'  '+g+'  '+'|'+'  '+h+'  '+'|'+'  '+i+'  '+'|')
            print('+-----+-----+-----+')  
        else:
            a='0'
            b='1'
            c='2'
            d='3'
            e='4'
            f='5'
            g='6'
            h='7'
            i='8'             
            for element in range(9):
                if element==0:
                    a=self.board[element]
                elif element==1:
                    b=self.board[element]                    
                elif element==2:
                    c=self.board[element]   
                elif element==3:
                    d=self.board[element]
                elif element==4:
                    e=self.board[element]
                elif element==5:
                    f=self.board[element]
                elif element==6:
                    g=self.board[element]
                elif element==7:
                    h=self.board[element]
                elif element==8:
                    i=self.board[element]                
            print('+-----+-----+-----+')
            print('|'+'  '+a+'  '+'|'+'  '+b+'  '+'|'+'  '+c+'  '+'|')
            print('+-----+-----+-----+')
            print('|'+'  '+d+'  '+'|'+'  '+e+'  '+'|'+'  '+f+'  '+'|')  
            print('+-----+-----+-----+')        
            print('|'+'  '+g+'  '+'|'+'  '+h+'  '+'|'+'  '+i+'  '+'|')
            print('+-----+-----+-----+')    
            
    def handle_message(self,msg):
        #conditions that will match the messages from  the sever and perform necessary steps
        if msg[:msg.find(",")]=="new game":
            self.shape=msg[-1] #index shape
            print("New game is about to start, your character is "+self.shape) #lets the players know their shape
            self.display_board() #display_board method called to display the board
        elif msg=="your move":
            print("It's your turn to move") #lets the players know their turn to move
            self.send_message(self.input_move())  #lets the players input their move and sends message to the server
        elif msg=="opponents move":
            print("It's the opponent turn to move") #lets the players know it their opponent turn to move
        elif msg[:msg.find(",")]=="valid move":
            self.shape=msg[-3] #index shape
            self.position=int(msg[-1]) #index position
            self.board[self.position]= self.shape #insert shape to the board
            self.display_board() #display_board method called to display the board
        elif msg=="invalid move":
            print("You have entered an invalid move") #lets the player know that an invalid move was made
        elif msg[:msg.find(",")]=="game over":
            self.results=msg[-1] #index shape
            if self.results=="X" or self.results=="O" :print("Game Over, the winner is "+self.results) #lets the players know who is the winner
            else: print("Game Over, it is a Tie") #lets the players know that no one won, it is a tie
        elif msg=="play again":
            self.answer=self.input_play_again() #Ask the players whether they want to play again
            self.send_message(self.answer) #lets the players input their answer and sends message to the server
            if self.answer.lower()=="y":self.clear_board() # clear board if the answer from the player is "y"
        elif msg=="exit game":
            print("Game Closed, One of the players doesn't want to play again.") #lets the players know that the game has been closed
            time.sleep(4)

    def play_loop(self):
        while True:
            msg = self.receive_message()
            if len(msg): self.handle_message(msg)
            else: break

def main():
    otc = OXOTextClient()
    while True:
        try:
            otc.connect_to_server(otc.input_server())
            break
        except:
            print('Error connecting to server!')
    otc.play_loop()
    input('Press click to exit.')

main()