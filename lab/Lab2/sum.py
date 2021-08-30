def combinatoricSum(List):
    newList = []
    tempList = []
    if(len(List)<3):
        return "Array Input Length Must More Than 2"
    else:
        for i in List:
            tempList.append(i)
            for j in List[List.index(i)+1:len(List):]:
                tempList.append(j)
                for k in List[List.index(j)+1:len(List):]:
                    isSumList = tempList.copy()
                    #print("issumList : "+str(isSumList))
                    if(isSumList[0]+isSumList[1]+k == 5):
                        tempList.append(k)
                        tempList.sort()
                        if tempList not in newList:
                            newList.append(tempList.copy())
                        tempList.remove(k)
                tempList.remove(j)
            tempList.clear()
            
        return newList
            
            
myList = list(map(int,input("Enter Your List : ").split()))
print(combinatoricSum(myList))