def findsubset(l:list,val,returnee:list=[],temp=[],index=0):
    if index >= len(l):
        return returnee
    
    temp.append(l[index])
    if sum(temp) == val:
        returnee.append(temp.copy())
    returnee = findsubset(l,val,returnee,temp,index+1)
    temp.pop()
    returnee = findsubset(l,val,returnee,temp,index+1)
    return returnee

def bbsort(inp):
    for i in range(len(inp)):
        for j in range(len(inp)-i-1):
            if inp[j] > inp[j+1]:
                inp[j],inp[j+1] = inp[j+1],inp[j]
def sort(l):
    for i in range(len(l)-1):
        swapped = False
        for j in range(len(l)-i-1):
            if len(l[j]) > len(l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]
                swapped = True
        if not swapped:
            break
inp = input('Enter Input : ').split('/')
inp[1] = list(map(int,inp[1].split()))
bbsort(inp[1])
subset = findsubset(inp[1],int(inp[0]))
if subset == []:
    print("No Subset")
else:
    sort(subset)
    print(*subset,sep="\n")
