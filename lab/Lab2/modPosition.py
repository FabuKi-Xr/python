print("*** Mod Position ***")
def mod_position(arr,s):
    myList = []
    for i in range(s-1,len(arr),s):
        myList.append(arr[i])
    return myList
myInput,s = input("Enter Input: ").split(',')
s = int(s) 
print(mod_position(myInput,s))
