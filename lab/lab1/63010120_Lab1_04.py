print("*** Fun with Drawing ***")
myInput = int(input("Enter input : "))

### upper
for i in range (1,myInput+1):
    for j in range(1,(myInput*4)-2):
        if(j== i+myInput-1 or j== (myInput)+1-i or j==i-3+(3*myInput) or j==(3*myInput)-1-i):
            print("*",end="")
        elif((j < i+myInput-1 and j > (myInput)+1-i )and j<=((myInput*4)-2)//2):
            print("+",end="")
        elif(j< i-3+(3*myInput) and j > (3*myInput)-1-i and j>=((myInput*4)-2)//2):
            print("+",end="")
        else:
            print(".",end="")
    print("")
for i in range (myInput+1,(3*myInput)-1):
    for j in range(1,(myInput*4)-2):
        if(j == i-myInput+1 or j == -i+(5*myInput)-3):
            print("*",end="")
        elif(j > i-myInput+1 and j < -i+(5*myInput)-3):
            print("+",end="")
        else:
            print(".",end="")
    print("")
