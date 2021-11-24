def bubble_sort(inp:list):
    count = 0
    for i in range(len(inp)):
        isSwap = False
        for j in range(len(inp)-i-1):
            count += 1
            if inp[j] > inp[j+1]:

                inp[j],inp[j+1] = inp[j+1],inp[j]
                isSwap = True
        if not isSwap:
            break 
    return count


print(" *** Bubble sort ***")    
input_string = input("Enter some numbers : ")
A=[]
for n in input_string.split():
	A.append(int(n))
count = bubble_sort(A)
print()
print(A)
print("Data comparison =", count)