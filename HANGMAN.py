import random
class Template:
    def __init__(self,size):
        self.dashes = ["_"]*size


    def isFull(self):
    
        if "_" in self.dashes: return False
        else: return True
        
    def update(self, word, character):
        found=False
        for i in range(len(word)):
            if character == word[i]:
                self.dashes[i]=character
                found=True
                 
        return found
    def existIn(self,char):
        if char in self.dashes: return True
        else: return False
    def show(self):
        line = ""
        for i in range(len(self.dashes)):
            line += self.dashes[i] + " "
        print (line)
    
### class Gallows
class Gallows:
    def __init__(self):
        self.step = 0
        
    def increment(self):
        self.step +=1
        
    def get(self):
        return self.step     
    def show(self):
            l1=l2=l3=l4=l5=l6=""
            if self.step>0:
              l2=l3=l4=l5=l6=" |"
            if self.step>1 :     
              l1="  ____"
            if self.step>2:
              l6="/|\\"
            if self.step>3:
              l2=" |/  |"
            if self.step==5:
              l3=" |   o"
              l4=" |  /|\\"
              l5=" |  / \\"
            print (l1,l2,l3,l4,l5,l6,sep="\n")

### hangman word game
myfile = open('wordshint.txt', 'r')
myLines=myfile.readlines()
myfile.close()

playingGame=True
while playingGame:
    wrongGuesses = []
    gameOver = False
    i=random.randrange(0,len(myLines))
    myLine = myLines[i].rstrip()
    [myWord,myHint]=myLine.split(",",1)
    myTemplate = Template(len(myWord))
    hangman = Gallows()

    while not gameOver :
        hangman.show()
        myTemplate.show()
        print ("Hint:",myHint)
        out=""
        for i in range(len(wrongGuesses)):
            out += wrongGuesses[i] + ", "        
        print (out)
        accept=False
        while not accept:
            theInput=input("Guess a letter: ")         
            myChar=theInput[0]
            if myChar not in wrongGuesses and not myTemplate.existIn(myChar) and myChar.isalpha(): accept = True
        if not myTemplate.update(myWord,myChar):
            hangman.increment()
            wrongGuesses.append(myChar)
            wrongGuesses=sorted(wrongGuesses)
        gameOver = myTemplate.isFull() or hangman.get()==5 
    if myTemplate.isFull():
        print ("Well Done! The word is indeed: ", myWord) 
    else:
        hangman.show()
        myTemplate.show()
        print ("R.I.P.! The Word was [", myWord,"]")
    while True:
        response=input("Do you want to play again? (Y/N)")
        play=response[0]
        if play.upper()=="Y" or play.upper()=="N": break
    if play.upper()=="N": playingGame=False
print("Thank you for playing Hangman")