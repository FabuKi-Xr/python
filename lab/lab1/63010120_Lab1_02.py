print("*** multiplication or sum ***")
x,y = map(int,input("Enter num1 num2 : ").split())
if(x*y > 1000):
    print("The result is "+str(x+y))
else:
    print("The result is "+str(x*y))