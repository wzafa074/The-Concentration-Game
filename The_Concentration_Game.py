import random

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    # YOUR CODE GOES HERE
    random.shuffle(deck)
    print("Shuffling the deck...\n")

def create_board(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    return board

def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')


def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nPress enter to continue. ")
    print()

def changing_board(size): # Extra Added Function
    ''' (int)-> list of str
    Given the size of the board, function returns a list of "*" corresponding
    to the size.
    Precondition: size is even positive integer.
    '''

    board = []
    for i in range(size):
        board.append("*")
    return board
    

def print_revealed(discovered, p1, p2, original_board):
    '''(list of str, int, int, list of str)->None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''
    # YOUR CODE GOES HERE
    
    discovered[p1]=original_board[p1]
    discovered[p2]=original_board[p2]
    print_board(discovered)
    print()
    wait_for_player()
    print(35*"\n")
    if original_board[p1]!=original_board[p2]:
        discovered[p1]="*"
        discovered[p2]="*"
        
        
        
        
    

#############################################################################
#   FUNCTIONS FOR OPTION 1 (with the board being read from a given file)    #
#############################################################################

def read_raw_board(file):
    '''str->list of str
    Returns a list of strings represeniting a deck of cards that was stored in a file. 
    The deck may not necessarifly be playable
    '''
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i]=raw_board[i].strip()
    return raw_board


def clean_up_board(l):
    '''list of str->list of str

    The functions takes as input a list of strings representing a deck of cards. 
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''
    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")
    pb=[]
    # YOUR CODE GOES HERE
    for x in l:
        if x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&()~_+':
            pb+=x
    for t in l:
        while pb.count(t)%2!=0:
            if pb.count(t)%2!=0:
                pb.remove(t)
    return pb

def board_check(l): #Extra added function
    ''' (list) -> True/False
    Returns True if the list of strings entered by a file is empty, else False
    '''
    b=[]
    if l==b:
        print("The resulting board is empty.\nPlaying Concentration game with an empty board is impossible.\nGood bye")
        return True
    else:
        return False

def is_rigorous(l):
    '''list of str->True or None
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: Every element in the list appears even number of times
    '''

    # YOUR CODE GOES HERE
    for i in l:
        if l.count(i)!=2:
            return False
    return True
 
                
        

####################################################################3              

def play_game(board):
    '''(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''
    
    print("Ready to play ...\n")

    # this is the funciton that plays the game
    # YOUR CODE GOES HERE

    guess_count=0
    x=0
    y=1
    for i in range(len(board)):
        
        while board2[i]=="*":

                if x!=y and board2[x]==board2[y]:
                    print_board(board2)
                    print("\n\n\nEnter two distinct positions on the board that you want revealed.\ni.e two integers in the range [1, " + str(len(board))+"]")
                    x = int(input("Enter position 1: "))-1
                    y = int(input("Enter position 2: "))-1
                
                while (board2[x]!="*" or board2[y]!="*") and board2[x]!=board2[y]:
                    print("One or both of your chosen positions has already been paired.")
                    print("Please try again. This guess did not count. You current number of guesses is "+ str(guess_count)+".")
                    print("\nEnter two distinct positions on the board that you want revealed.\ni.e two integers in the range [1, " + str(len(board))+"]")
                    x = int(input("Enter position 1: "))-1
                    y = int(input("Enter position 2: "))-1
                        
                while x==y:
                    if board2[x]!="*" and board2[y]!="*" and board2[x]==board2[y]:
                        print("One or both of your chosen positions has already been paired.")
                    print("You chose the same positions.\nPlease try again. This guess did not count. You current number of guesses is " +str(guess_count)+".")
                    print("\nEnter two distinct positions on the board that you want revealed.\ni.e two integers in the range [1, " + str(len(board))+"]")
                    x = int(input("Enter position 1: "))-1
                    y = int(input("Enter position 2: "))-1
                    
                if x!=y and board2[x]=="*" and board2[y]=="*" :
                    guess_count+=1        
                    print_revealed(board2, x, y, board)

    print("Congratulations! You completed the game with "+ str(guess_count) + " guesses. That is "+str(guess_count-((len(board))//2)) +" more than the best possible.")
          
#main    
# YOUR CODE TO GET A CHOICE 1 or CHOCE 2 from a player GOES HERE

s="Welcome to my Concentration game"
print((10+len(s))*"*")
print("*" + (8+len(s))*" " + "*")
print("*"+2*" " + "__" + s + "__"+ 2*" "+"*")
print("*" + (8+len(s))*" " + "*")
print((10+len(s))*"*")

q=int(input('\nWould you like to (enter 1 or 2 to indicate your choice):\n(1) me to generate a rigorous deck of cards for you\n(2) or,'+
            ' would you like me to read a deck from a file?\n'))
while q!=1 and q!=2:
    q=int(input(str(q)+" is not a existing option. Please try again. Enter 1 or 2 to indicate your choice\n"))
    

# YOUR CODE FOR OPTION 1 GOES HERE
if q==1:
    print("You chose to have a rigorous deck generated for you\n")
    j= int(input("How many cards do you want to play with?\nEnter an even number between 0 and 52 "))
    print()
    while j<0 or j>52 or j%2!=0:
        j= int(input("How many cards do you want to play with?\nEnter an even number between 0 and 52 "))
        print()
    board = create_board(j)
    shuffle_deck(board)
    wait_for_player()
    print(35*"\n")
    board2 = changing_board(j)
    play_game(board)
    
        
# In option 1 somewhere you need to and MUST have a call like this:
# board=create_board(size)

# YOUR CODE FOR OPTION 2 GOES HERE
else:
    
# In option 2 somewhere you need to and MUST have the following 4 lines of code one after another
    print("You chose to load a deck of cards from a file")
    file=input("Enter the name of the file: ")
    file=file.strip()
    board=read_raw_board(file)
    board=clean_up_board(board)

    if is_rigorous(board)==True:
        w="This deck is now playable and rigorous and it has "+ str(len(board)) +" cards."
        print((10+len(w))*"*")
        print("*" + (8+len(w))*" " + "*")
        print("*"+2*" " + "__" + w + "__"+ 2*" "+"*")
        print("*" + (8+len(w))*" " + "*")
        print((10+len(w))*"*")
    else:
        w="This deck is now playable but not rigorous and it has "+ str(len(board)) +" cards."
        print((10+len(w))*"*")
        print("*" + (8+len(w))*" " + "*")
        print("*"+2*" " + "__" + w + "__"+ 2*" "+"*")
        print("*" + (8+len(w))*" " + "*")
        print((10+len(w))*"*")

    wait_for_player()
    print(35*"\n")
    shuffle_deck(board)
    wait_for_player()
    print(35*"\n")
    board2= changing_board(len(board))
    if board_check(board)==False:
        play_game(board)

