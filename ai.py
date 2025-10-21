# 1. BFS
def bfs(graph,start):
    visited=[]
    queue=[start]
    while queue:
        node=queue.pop(0)
        if node not in visited:
            print(node,end=" ")
            visited.append(node)
            queue.extend(graph[node])
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'B', 'C'],
    'C': ['W', 'G', 'E'],
    'D': [],
    'E': ['V'],
    'W': [],
    'G': [],
    'V': []
}
bfs(graph,'A')

# 2. DFS
def dfs(graph,node,visited=None):
    if visited is None:
        visited=[]
    if node not in visited:
        print(node,end=" ")
        visited.append(node)
        for i in graph[node]:
            dfs(graph,i,visited)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
dfs(graph,'A')

# 3. Tic-Tac-Toe
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]  
player = "X"  
for turn in range(9):  
    print(board[0], "|", board[1], "|", board[2])  
    print(board[3], "|", board[4], "|", board[5])  
    print(board[6], "|", board[7], "|", board[8])    
    choice = int(input("Player " + player + " enter 1-9: "))  
    board[choice - 1] = player       
    if board[0] == board[1] == board[2]:  
        print("Player", player, "wins!")  
        break  
    if board[3] == board[4] == board[5]:  
        print("Player", player, "wins!")  
        break  
    if board[6] == board[7] == board[8]:  
        print("Player", player, "wins!")  
        break  
    if board[0] == board[3] == board[6]:  
        print("Player", player, "wins!")  
        break  
    if board[1] == board[4] == board[7]:  
        print("Player", player, "wins!")  
        break  
    if board[2] == board[5] == board[8]:  
        print("Player", player, "wins!")  
        break  
    if board[0] == board[4] == board[8]:  
        print("Player", player, "wins!")  
        break  
    if board[2] == board[4] == board[6]:  
        print("Player", player, "wins!")  
        break  
    if player == "X":  
        player = "O"  
    else:  
        player = "X"  
else:  
    print("It's a tie!") 
    
# 4. 8-Puzzles
from collections import deque   
def solve(b):  
    s = sum(b, [])  
    if s == list(range(9)): return 0  
    m = [[1,3], [0,2,4], [1,5], [0,4,6], [1,3,5,7], [2,4,8], [3,7], 
[4,6,8], [5,7]]  
    q = deque([(s, 0)])  
    v = set()       
    while q:  
        t, c = q.popleft()  
        if str(t) in v: continue  
        v.add(str(t))  
        z = t.index(0)           
        for i in m[z]:  
            n = t[:]  
            n[z], n[i] = n[i], n[z]  
            if n == list(range(9)): return c + 1  
            q.append((n, c + 1))     
    return -1   
print(solve([[3,1,2], [4,7,5], [6,8,0]]))

# 5. Water Jug Problem 
print("Water jug Problem")
x=int(input("Enter X:"))
y=int(input("Enter Y:"))
while True:
    r=int(input("Rule no.:"))
    if r==1:
        x=4
    elif r==2:
        y=3
    elif r==5:
        x=0
    elif r==6:
        y=0
    elif r==7 and y>0:
        y-=max(0,4-x)
        x=4
    elif r==8 and x>0:
        x-=max(0,3-y)
        y=3
    elif r==9 and y>0:
        x=min(4,x+y)
        y=0
    elif r==10 and x>0:
        y=min(3,y+x)
        x=0
    print("x:",x)
    print("y:",y)
    if x==2:
        print("goal stat achived")
        break

# 6. TSP
from itertools import permutations  
d = [[0,10,15,20], [10,0,35,25], [15,35,0,30], [20,25,30,0]]  
best = 999  
path = []  
for trip in permutations([1,2,3]):  
a, b, c = trip  
cost = d[0][a] + d[a][b] + d[b][c] + d[c][0]  
if cost < best:  
best = cost  
path = trip  
print("Cost:", best, "Path:", path)  

#7. Tower of Hanoi
def honnai(n,source,aux,dest):
    if n==0:
        return
    honnai(n-1,source,dest,aux)
    print(f"Move disk {n} from source {source} to destination {dest}")
    honnai(n-1,aux,source,dest)
n=3
honnai(n,'A','B','C')

#8. Monkey
def monkey(n):
    climb=0
    banana=0
    hungry=True
    for i in range(n):
        if hungry:
            climb+=1
            banana+=1
            hungry=False
        else:
            climb+=1
            return climb ,banana
n=10
climb, banana=monkey(n)
print(f"The Monkey made {climb} climbs and get {banana} Bananas")

#9. Alpha Beta Purning
MIN,MAX=-1000,1000
def minimax(depth,nodeindex,maximizingPlayer,values,alpha,beta):
    if depth==3:
        return values[nodeindex]
    if maximizingPlayer:
        best=MIN
        for i in range(0,2):
            val=minimax(depth+1,nodeindex*2+i,False,values,alpha,beta)
            best=max(best,val)
            alpha=max(alpha,best)
            if beta<=alpha:
                break
        return best
    else:
        best=MAX
        for i in range(0,2):
            val=minimax(depth+1,nodeindex*2+i,True,values,alpha,beta)
            best=min(best,val)
            beta=min(beta,best)
            if beta<=alpha:
                break
        return best
values=[3, 5, 6, 9, 1, 2, 0, -1]
print("The optimal value is:",minimax(0,0,True,values,MIN,MAX))

# 10. 8-Queens
global N
N=4
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j],end=" ")
        print()
def isSafe(board,row,col):
    for i in range(col):
        if board[row][i]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    for i,j in zip(range(row,N,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    return True
def solveNQUtil(board,col):
    if col>=N:
        return True
    for i in range(N):
        if isSafe(board,i,col):
            board[i][col]=1
            if solveNQUtil(board,col+1)==True:
                return True
            board[i][col]=0
    return False
def solveNQ():
    board=[
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
    if solveNQUtil(board,0)==False:
        print("Solution Does not exist")
        return False
    printSolution(board)
    return True
solveNQ()

# 11. Chatbot
import random
responses=["Hello,how can I help you?",
           "What do you want to talk about?",
           "I'm not sure what you mean.",
           "Can you repeat that?",
           "I'm sorry,I don't understand.",
           "Goodbye!"]
def get_response():
    return random.choice(responses)
def start_chatbot():
    print("Hello,I'm a chatbot.What do you want to talk about?")
    while True:
        user_input=input()
        response=get_response()
        print(response)
start_chatbot()

#12. Hangman
import random
import string
def choose_word():
    words = ["python", "hangman", "programming", "developer", "artificial", "intelligence"]
    return random.choice(words)
def get_available_letters(letters_guessed):
    return ''.join([ch for ch in string.ascii_lowercase if ch not in letters_guessed])
def get_guessed_word(secret_word, letters_guessed):
    return ''.join([ch if ch in letters_guessed else '_' for ch in secret_word])
def is_word_guessed(secret_word, letters_guessed):
    return all(ch in letters_guessed for ch in secret_word)
def hangman(secret_word):
    guesses_left = 8
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print("-------------")
    while guesses_left > 0:
        print(f"You have {guesses_left} guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ").lower()

        if guess in letters_guessed:
            print("Oops! You've already guessed that letter:", get_guessed_word(secret_word, letters_guessed))
        elif guess in secret_word:
            letters_guessed.append(guess)
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed.append(guess)
            guesses_left -= 1
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))

        print("-------------")

        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            break
    else:
        print(f"Sorry, you ran out of guesses. The word was '{secret_word}'.")
if __name__ == "__main__":
    word = choose_word()
    hangman(word)

# 13. Stopwords
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

text="This ia a simple example to remove the stop words wsing NLTK."
words=word_tokenize(text)
fil=[w for w in words if w.lower() not in stopwords.words('english')]
print(fil)
