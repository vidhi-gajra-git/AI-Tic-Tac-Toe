# just input taken here

board = [[' ' for _ in range(3)] for _ in range(3)]
import math
import copy

INT_MIN = -math.inf
INT_MAX = math.inf

class game():

  count=0
  def __init__(self):

    count=self.count
  def incCount(self):
   count+=1

  def calVal(self,graph):
    # calculates the heuristic
    final_sum=0
    for r in graph:
      r_sum=0

      for i in r:
        if i=='X':

          r_sum=r_sum+1
        elif i=='O':

          r_sum=r_sum-1
      if r_sum==3:
        # print('X wins here')
       return 100
      if r_sum==-3:
        # print('O wins here')
       return  -100

      final_sum=final_sum+r_sum
    for i in range (0,3):
      col_sum=0

      for j in range (0,3):

         if graph[j][i]=='X':

          col_sum=col_sum+1
         elif graph[j][i]=='O':
          col_sum=col_sum-1
      if col_sum==-3:
        # print('O wins here')
       return -100
      if col_sum==3:
        # print('X wins here')
        return 100
    #   final_sum=final_sum+col_sum

    d1_sum=0
    d2_sum=0
    for k in range (0,3):

        #  print(f"{k} {2-k}")

         if graph[k][k]=='X':
          #
          d1_sum=d1_sum+1
         elif graph[k][k]=='O':
          # count_o+=1
          d1_sum=d1_sum-1
         if graph[k][(2-k)]=='X':
          d2_sum=d2_sum+1
         elif graph[k][(2-k)]=='O':
             d2_sum=d2_sum-1
    if d2_sum==3:
           return 100
    if d2_sum==-3:
            return -100
    if d1_sum==3:

          return 100
    if d1_sum==-3:

          return -100


    final_sum=final_sum+d1_sum+d2_sum
    # print(f"final_sum={final_sum}")
    return 0


  def minmax (self,graph, depth, isMax ,a,b ):

    if  depth==9 or abs(self.calVal(graph))==100:
     
      val=self.calVal(graph)
  
      return val
    if isMax:
      local_max=INT_MIN
      best_children=None
      temp=[]
      for i in range(0,3):
        for j in range(0,3):

          if graph[i][j]==' ':
            temp=copy.deepcopy(graph)

            temp[i][j]='X'

            val=self.minmax(temp,depth+1,False , a,b)
            
            if val>local_max :
              local_max=val
              best_children=temp

            a=max(local_max,a)
            if a>=b :
              break
      if depth==0:
        return best_children
      return local_max

    else:
      local_min=INT_MAX
      # temp=[]
        # best_children=None
      for i in range(0,3):
          for j in range(0,3):
            if graph[i][j]==' ':
              temp=copy.deepcopy(graph)

              temp[i][j]='O'
              val=self.minmax(temp,depth+1,True , a,b)
           
              if val<local_min :
                local_min=val


              b=min(local_min,b)
              if a>=b :
                break

      return local_min

# print(minmax(root,0,True,INT_MIN,INT_MAX))


# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to take player input for row and column
def get_player_input():
    while True:
        try:
            row, col = map(int, input("Enter your move (row and column [1,2,3]): ").split())
            if 1 <= row < 4 and 1 <= col < 4 and board[row-1][col-1] == ' ':
                return row-1, col-1
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Main game loop
current_player = 'X'
board=[['X',' ',' '],[' ',' ',' '],[' ',' ',' ']]
g=game()
flag=True
count=0
while flag:
    count+=1
    print("player X's turn ")
    print_board(board)
    print(f"Player O's turn.")

    # Get player input for row and column
    row, col = get_player_input()

    # Place the player's symbol on the board
    board[row][col] = 'O'
    print_board(board)
    # Switch to the other player
    # node=Node(board)

    board=g.minmax(board,0,True,INT_MIN,INT_MAX)
    val=g.calVal(board)
    if val==100 :
       print_board(board)

       print("You loose💔!🥺 !")
       flag=False
    elif val==-100:
      print_board(board)

      print("You win🥳🥳❤️!")
      flag=False
    if count==8:
      print("Tie 🤡")



# dfs(node)
# for c in node.child:
#   print(c.val)

# board=node.path.graph
