def findMax(l:list):
    if l == []:
        return -9999999999999
    max = findMax(l[1:])
    if l[0] > max:
        max = l[0]
    return max

def selection(unorder:list,index):
    if index < 0:
        return 
    max = findMax(unorder[:index+1])
    if unorder[index] != max:
        maxindex = unorder.index(max)
        print(f"swap {unorder[index]} <-> {max} : ",end="")
        unorder[maxindex],unorder[index] = unorder[index],unorder[maxindex]
        print(unorder)
    selection(unorder,index-1)
    return unorder

unorder = list(map(int,input('Enter Input : ').split()))
print(selection(unorder,len(unorder)-1))
