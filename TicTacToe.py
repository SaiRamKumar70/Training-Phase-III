import random
def printboard(board):
    print("*" * 20)
    for row in board:
        print("  "," ".join(row))
        print("-" * 15)
    print("*" * 20)
def isfull(board):
    for row in board:
        for col in row:
            if col == "":
                return False
    return True
def check(board, p):
    for row in board:
        if row[0] == p and row[1] == p and row[2] == p:
            return True
        for i in range(3):
            if board[0][i] == p and board[1][i] == p and board[2][i] == p:
                return True
        if board[1][1] == p and board[2][2] == p and board[0][0] == p:
            return True
        if board[0][2] == p and board[1][1] == p and board[2][0] == p:
            return True
board=[[""]*3 for _ in range(3)]
print("Welcome To The Tic-Tac-Toe GAME!")
printboard(board)
print("Players X And O")
curr=random.choice(['X', 'O'])
while True:
    print("Current Player Is", curr)
    print("Enter The Dimensions (Row and Column) : ")
    x,y=map(int,input().split())
    if -1<x<3 or -1<y<3:
        if board[x][y] == "":
            board[x][y] = curr
            printboard(board)
            if check(board, curr):
                print("Congratulations!",curr,"Wins The Game!")
                break
            if isfull(board):
                print("Game is a Tie")
                break
            if curr == 'X':
                curr = 'O'
            else: 
                curr = 'X'
        else:
            print("That cell is already occupied. Try again.")
    else:
        print("Invalid coordinates. Please enter valid values (0, 1, or 2).")