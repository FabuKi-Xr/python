print("*** Fun with countdown ***")
myList = list(map(int,input("Enter List : ").split()))
newList = []
size = len(myList)
idx_list = [idx + 1 for idx, val in
            enumerate(myList) if val == 1]
count = 0
res = [myList[i: j] for i, j in
        zip([0] + idx_list, idx_list + 
        ([size] if idx_list[0] == size else []))]
for i in res :
    count = 0
    for k in range(len(i)-1,0,-1) :
        if(i[k-1] - i[k] != 1):
            for j in range (len(i)-count-1):
                i.remove(i[0])
        else:
            count += 1
print("[{},".format(len(res)),str(res)+"]")