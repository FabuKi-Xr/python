def reverseSort(l:list,item): 
    if l == [] or item < l[-1]:
        l.append(item)
        return
    else:
        temp = l.pop()
        reverseSort(l,item)
        l.append(temp)
        
def stack(l:list):
    if l != []:
        temp = l.pop()
        stack(l)
        reverseSort(l,temp)
    return l

inp = list(map(int,(input("Enter your List : ").split(','))))
print("List after Sorted : "+str(stack(inp)))


