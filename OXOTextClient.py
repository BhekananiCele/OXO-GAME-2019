from GameClient import *

class OXOTextClient(GameClient):

    def __init__(self):
        GameClient.__init__(self)
        self.board = [' '] * BOARD_SIZE
        self.shape = None
        self.position= None
        self.winner=None
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
        elif msg=="your move":
            pass #code missing     
        elif msg=="opponents move":
            pass #code missing 
        elif msg[:msg.find(",")]=="valid move":
            self.shape=msg[-3]
            self.position=msg[-1]
        elif msg=="invalid move":
            pass #code missing 
        elif msg[:msg.find(",")]=="game over":
            self.winner=msg[-1]
        elif msg=="play again":
            pass #code missing 
        elif msg=="exit game":
            pass #code missing     
    
    def play_loop(self):
        while True:
            msg = self.receive_message()
            if len(msg): self.handle_message(msg)
            else: break
            
def main():
    otc = OXOTextClient()
    #otc.display_board()
    while True:
        try:
            otc.connect_to_server(otc.input_server())
            break
        except:
            print('Error connecting to server!')
    otc.play_loop()
    
    input('Press click to exit.')
        
main()