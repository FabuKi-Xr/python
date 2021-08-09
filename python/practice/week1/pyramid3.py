myInput = int(input())
for i in range (1,(2*myInput),1):
    for j in range (1,(2*myInput)) :
        if(i+j <=myInput or i+j>= (3*myInput) or i-j >= myInput or j-i >= myInput):
            print(" ",end="")
        else:
            print("*",end="")
    print("")
