def GCD(num1,num2):
    if num2 == 0:
        return abs(num1)
    return GCD(num2,num1%num2)
inp = list(map(int,(input('Enter Input : ').split())))

if inp[0] == inp[1] == 0:

    print("Error! must be not all zero.")

else:
    gcd = GCD(inp[0],inp[1])
    if inp[0] < 0 and inp[1] < 0:
        print(f"The gcd of {min(inp)} and {max(inp)} is : {gcd}")
    else:
        print(f"The gcd of {max(inp)} and {min(inp)} is : {gcd}")