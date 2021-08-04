mylist=[]
for i in range(5):
    mylist.append(int(input()))
mylist.sort(reverse=True)
for i in range(5):
    print(mylist[i])