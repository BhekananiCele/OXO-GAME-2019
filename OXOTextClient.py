from GameClient import *
# Just added this
class OXOTextClient(GameClient):

    def __init__(self):
        GameClient.__init__(self)
        self.board = [' '] * BOARD_SIZE
        self.shape = None
        self.position= None
        self.results=None
    def clear_board(self):
        self.board = [' '] * BOARD_SIZE
        
    def input_server(self):
        return input('enter server:')
     
    def input_move(self):
        return input('enter move(0-8):')
     
    def input_play_again(self):
        return input('play again(y/n):')

    def display_board(self):
        # display the board of the game
        for col in range(9):
            if col==3 or col==6:
                print()
            if col<3:
                print(self.board[col],end="|")
            elif 2<col<6:
                print(self.board[col],end="|")
            elif 5<col<9:
                print(self.board[col],end="|") 
        print()
    def handle_message(self,msg):
        #conditions that will match the messages from  the sever and perform necessary steps
        if msg[:msg.find(",")]=="new game":
            self.shape=msg[-1]
            print("New game is about to start, your character is "+self.shape)
            display_board()
            #some code missing 
        elif msg=="your move":
            print("It's your turn to move")
            self.input_move()     
        elif msg=="opponents move":
            print("It's the opponent turn to move") #self.send_message(self.input_move())  
        elif msg[:msg.find(",")]=="valid move":
            self.shape=msg[-3]
            self.position=msg[-1]
            self.board[self.position]= self.shape
            self.display_board()
        elif msg=="invalid move":
            print("You have entered an invalid move")
            self.input_move()
        elif msg[:msg.find(",")]=="game over":
            self.results=msg[-1]
            if self.result=="X" or self.result=="O" :print("Game over the winner is "+self.results) 
            else: print("Game over it is a Tie")
        elif msg=="play again":
            self.input_play_again()
            self.clear_board()
        elif msg=="exit game":
            print("Game exited")    
    
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