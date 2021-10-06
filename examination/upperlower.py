txt = input(" *** String count ***\nEnter message : ")
list = [[],[]]
noUP = 0
noLow = 0 
for i in txt:
    if ord(i) >= ord('A') and ord(i) <= ord('Z'):
        noUP += 1
        if i not in list[0]:
            list[0].append(i)
    if ord(i) >= ord('a') and ord(i) <= ord('z'):
        noLow +=1
        if i not in list[1]:
            list[1].append(i)
list[0].sort()
list[1].sort()
print("No. of Upper case characters :",noUP)
print("Unique Upper case characters :",end=" ")
print(*list[0],sep="  ")
print("No. of Lower case Characters :",noLow)
print("Unique Lower case characters :",end=" ")
print(*list[1],sep="  ")
