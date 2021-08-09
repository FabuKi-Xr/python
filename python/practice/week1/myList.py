myList = []
for i in range (0,1000,1) :
    myList.append(int(input())) 
    if(myList[-1]== 0):
        myList.remove(0)
        break
command = input()
if(command.upper() == "MAX"):
    myList.sort(reverse=True)
else:
    myList.sort()
print(' '.join(map(str,myList)))
