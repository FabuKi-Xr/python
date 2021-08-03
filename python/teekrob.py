myInput = int(input())
for i in range(0,myInput,1) : 
    for j in range (0,myInput,1) :
        if(i == 0 or i == myInput-1) :
            print("#",end="")
        else :
            if(j == 0 or j == myInput-1):
                print("#",end="")
            else :
                print(" ",end="")
    print("")
