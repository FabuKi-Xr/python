import math
def binary(n,digit):
    if n>=0:
        temp = format(binary(n-1,digit),"0"+digit+"b")
        print(temp)
    return n+1

n = int(input("Enter Number : "))
if n<0:
    print("Only Positive & Zero Number ! ! !")
else:
    binary((2**n)-1,str(n))