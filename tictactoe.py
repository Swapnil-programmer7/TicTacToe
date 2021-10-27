

#printing the board
def disp_brd(current_board):
    print("\n"*2)
    print("   |   |   \n {} | {} | {} \n   |   |   ".format(current_board[6],current_board[7],current_board[8])) #prints first row
    print("------------")
    print("   |   |   \n {} | {} | {} \n   |   |   ".format(current_board[3],current_board[4],current_board[5])) #prints second row
    print("------------")
    print("   |   |   \n {} | {} | {} \n   |   |   ".format(current_board[0],current_board[1],current_board[2])) #prints third row
    return

#this function takes an user input and checks if it is proper and then only returns the value
def mark_pos(board):
    inp = 'wrong'
    while not inp.isdigit() or inp not in ['1','2','3','4','5','6','7','8','9']:
        inp = input('Enter a number (1-9) only: ')
        if inp.isdigit():
            if int(inp) in range(1,10):
                if board[int(inp)-1] == ' ':
                    return int(inp)-1
                else:
                    inp = 'wrong'
                    print('this place has already been filled! Please enter a position that is free')
            else:
                print("accepted value not in range (1-9)")
        else:
            print("enter a numeral only")

#to check if the tri seq exists in board
def check(board,mark):
    s = board[mark]
    if mark%3 == 0:
        if board[mark]+board[mark+1]+board[mark+2] == s*3:
            return True
        elif board[0]+board[3]+board[6] == s*3:
            return True
    elif mark%3 == 1:
        if board[mark-1]+board[mark]+board[mark+1] == s*3:
            return True
        elif board[1]+board[4]+board[7] == s*3:
            return True
    elif mark%3 == 2:
        if board[mark-2]+board[mark-1]+board[mark] == s*3:
            return True
        elif board[2]+board[5]+board[8] == s*3:
            return True
    
    if board[6]+ board[4] + board[2] == s*3:
        return True
    elif board[0] + board[4] + board[8] == s*3:
        return True
    return False

#this is where we play
def play(board,p1,p2):
    p=1 #a indicator to say which players turn this is
    c=0
    winner = 0
    while winner == 0 and c<9:
        c+=1
        mark = mark_pos(board)
        if p == 1:
            board[mark] = p1
        else:
            board[mark] = p2
        
        disp_brd(board)

        if check(board,mark):
            print('\n\nplayer {} wins!!'.format(p))
            winner = p
        elif c==9:
            print('\n\nNo player wins! Draw')
        p = p**2 - 4*p + 5

#instructions
def instruct():
    print('\n'*4 +"Welcome to TicTacToe")
    print('This program lets you have a two player TicTacToe duel with your friend')
    print('The first player gets to choose his sign, and then he will have to enter the position he wants to put the mark at.')
    print('The program is gonna ask you for a popsition. The number corresponding to each position is given here.')
    disp_brd(['1','2','3','4','5','6','7','8','9'])
    print('\n'*2 + 'In order to win, players need to create a series of three either horizontally or vertically or diagonally.\nhorizontally like:')
    disp_brd([' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', 'X'])
    print('\n'*2 + "Vertically like: ")
    disp_brd(['X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' '])
    print('\n'*2 + 'diagonally like:')
    disp_brd(['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X'])
    return
        

#this will be the starting function
def replay():
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    choice = 'wrong'
    while not (choice == 'X' or choice == 'O'):
        choice = input('Hi player 1, choose either X or O: ').upper()
        #print(choice)
        if not (choice == 'X' or choice == 'O'):
            print("Player 1, unrecognised input, Enter either X or O")
    
    p1 = choice
    if p1 == 'X':
        p2 = 'O'
    else:
        p2 = 'X'
    play(board,p1,p2)

ch = True
inp = 'wrong'
i = 'ft'
while ch:
    if i != 'ft':
        print('Do you want to see the instructions on how to play the game?')
        while i not in ['N', 'Y']:
            inp = input('Say either Y or N: ').upper()
            if inp not in ['N', 'Y']:
                print('The passed value is not recognized.')
    if i == 'Y' or i == 'ft':
        instruct()
    i = 'wrong'

    replay()

    print('Want to play again?')
    while inp not in ['T','F']:
        inp = input('Say either T or F: ').upper()
        if inp not in ['T', 'F']:
            print('The passed value is not recognized.')
    if inp == 'T':
        ch = True
        inp = 'wrong'

    else:
        ch = False
    
       
print('I hope that you enjoyed playing TicTacToe. Bonne soiree!!')
