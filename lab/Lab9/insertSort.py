def insertSort(main:list,temp:list=None):
    if temp == []:
        print("sorted")
        print(main)
        return   
    val = temp.pop(0)
    print(f"insert {val} at index {insert(main,val)} : ",end="")
    print(main,temp) if temp!= [] else print(main)
    insertSort(main,temp)
def insert(main:list,val,index=0):
    if index > len(main)-1:
        main.insert(index,val)
        return index
    if val > main[index]:
        index = insert(main,val,index+1)

    else:
        main.insert(index,val)
    return index

inp = list(map(int,input('Enter Input : ').split()))
insertSort([inp.pop(0)],inp)

