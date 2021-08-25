class game():
    def __init__(self,List):

        self.gameList = List.copy()
        self.seperate_InList = [word for line in self.gameList for word in line.split() ]
        self.wordList = []

        self.gameState()

    def play(self,i):
        buffer = self.seperate_InList[self.seperate_InList.index(i)+1]
        self.seperate_InList.remove(i)

        if(len(self.wordList) == 0):
            self.wordList.append(buffer)
            print("""'{}' -> {}""".format(self.wordList[len(self.wordList)-1],self.wordList))
        elif(self.wordList[-1][(len(self.wordList[-1])-2):len(self.wordList[-1])].upper() == buffer[0:2].upper()):
            self.wordList.append(buffer)
            print("""'{}' -> {}""".format(self.wordList[len(self.wordList)-1],self.wordList))
        else:
            print("""'{}' -> game over""".format(buffer))
        
    def restart(self):
        print("game restarted")
        self.wordList.clear()
    
    def end(self):
        exit()

    def gameState(self):

        for i in self.seperate_InList:

            if(i[0] == 'P'):
                self.play(i)
            
            elif(i[0] == 'R'):
                self.restart()

            elif(i[0] == 'X'):
                self.end()

            else:
                print("""'{}' is Invalid Input !!!""".format(self.gameList[self.seperate_InList.index(i)]))
                break

myInput = input().split(',')
game = game(myInput)


