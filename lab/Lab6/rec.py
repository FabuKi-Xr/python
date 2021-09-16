n = int(input("E : "))

for i in range(n,0,-1):
    if (n == 0):
        print("Not Draw!")
        break
    s =""
    s += "_"*(i-1)
    s += "#"*(n-len(s))
    print(s)