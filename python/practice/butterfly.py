def butterfly(n):
    for i in range(1,2*n,1):
        # subtractor = 0
        for j in range(1,2*n,1):
            # if j>n:
            #     subtractor +=1
            if(abs(j-n) >= -i +n and abs(j-n) >= i-n):
                if j>n:
                    print(n-(j-n),end="")
                else:
                    print(j,end="")
            else:
                print(" ",end="")
        print()
# n = int(input("Enter number : "))
butterfly(9)