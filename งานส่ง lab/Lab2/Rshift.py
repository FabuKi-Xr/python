def Rshift(num,shift):
    return str(num>>shift)
n,s = input("Enter number and shiftcount : ").split()
print(Rshift(int(n),int(s)))