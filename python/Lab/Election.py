print("*** Election ***")
voter = int(input("Enter a number of voter(s) : "))
if(voter<=0):
    print("*** No Candidate Wins ***")
    exit()
myList = [int(e) for e in input().split()]
false = 0
for i in myList:
    if(  i <= 0 or i >20 ):
        myList.remove(i)
newList = []
newList = myList.copy()

newList.remove(max(set(myList),key=myList.count)) #ใช้ max หาค่าซ้ำสูงสุดของ mylist
if (myList == [] or newList == []):
    print("*** No Candidate Wins ***")
elif(newList.count(max(set(newList),key=newList.count)) == myList.count(max(set(myList),key=myList.count))):
        print("*** No Candidate Wins ***")
else:
    print(max(set(myList),key=myList.count))
        
             