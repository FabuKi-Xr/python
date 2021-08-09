myInput = int(input())
#row
for i in range (1,myInput+1,1) :
    #spaces
    for j in range (0,myInput-i,1 ):
        print(" ",end="")
    #symbols
    for k in range (0,(2*i)-1,1) :
        print("*",end="")
    print("")
        
        