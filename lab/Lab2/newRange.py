print("*** New Range ***")
def addition(var,myList): #var[0-2] is a,b,c orderly. var[3] is list
    starter = 0.0
    if(len(var) == 3):
        while(len(myList) == 0 or myList[-1]+var[2]<var[1]):
            myList.append(round(var[0]+starter,3))
            starter += var[2]
    else:
        if(len(var)== 1):
            while(len(myList) == 0 or myList[-1]+1< var[0]):
                myList.append(round(starter,3))
                starter+=1.0
        else:
            while(len(myList) == 0  or myList[len(myList)-1]+1 < var[1]):
                myList.append(round(var[0]+starter,3))
                starter+=1.0
myInput = list(map(float,(input("Enter Input : ").split())))
myList = []
addition(myInput,myList)
print(tuple(myList))