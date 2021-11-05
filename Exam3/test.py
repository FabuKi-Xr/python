# def GCD(l:list,gcd):
#     if gcd > 0:
#         if abs(l[0]) % gcd == abs(l[1]) % gcd == 0:
#             return abs(gcd)
#         temp = GCD(l,gcd)
#         return temp
#     else:
#         return 1 
# inp = list(map(int,(input('Enter Input : ').split())))
# if inp[0] == inp[1] == 0:
#     print("Error! must be not all zero.")
# else:
#     if abs(inp[0]) > abs(inp[1]):
#         mul = abs(inp[0]//inp[1])
#         gcd = GCD(inp,abs(inp[0])//mul)
#     else:
#         mul = abs(inp[1]//inp[0])
#         gcd = GCD(inp,abs(inp[1])//mul)

#     if inp[0] < 0 and inp[1] < 0:
#         temp = inp.pop(inp.index(max(inp)))
#         print(f"The gcd of {inp[0]} and {temp} is : {gcd}")
#     else:
#         print(f"The gcd of {inp.pop(inp.index(max(inp)))} and {inp[0]} is : {gcd}")