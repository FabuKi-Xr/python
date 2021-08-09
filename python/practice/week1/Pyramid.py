myInput = int(input())
for i in range(1,myInput+1):
    if(myInput >= 1) :
        for j in range (i):
            print("*",end="")
        i+=1
        print("")