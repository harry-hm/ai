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
