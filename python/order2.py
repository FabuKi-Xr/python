myInput = int(input())
myList = []
for i in range (myInput):
    myList.append(int(input()))
myList.sort(reverse=True)
for i in range(len(myList)):
    print(myList[i])