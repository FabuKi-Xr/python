myList = []
myList.append(int(input()))
myList.append(int(input()))
if(myList[0]>myList[1]):
    print("A")
elif(myList[0]==myList[1]):
    print("AB")
else:
    print("B")