import re
sum = 0
myList = re.findall(r'\d+',input())
myList = list(map(int,myList))
for i in range (len(myList)) :
     sum += myList[i]
sum = [char for char in str(sum) ]
for j in range (4-len(sum)):
    sum.insert(0,"0")
print("".join(map(str,sum)))