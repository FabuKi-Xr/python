myInput = int(input())
if(myInput%4 == 0):
    if((myInput%100)==0 and (myInput/100)%4 != 0) :
        print("Not a Leap Year")
    else :
        print("Leap Year")
else :
    print("Not a Leap Year")