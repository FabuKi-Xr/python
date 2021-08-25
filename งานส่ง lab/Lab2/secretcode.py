myInput = input("Enter secret code : ")
myList = [(ord(e)-96)*2 for e in myInput]
print(max(set(myList),key=myList.count)*2)