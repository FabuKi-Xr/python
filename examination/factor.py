num = int(input(" *** Divisible number ***\nEnter a positive number : "))
count = 0

if (num > 0):
    
    print("Output ==> ",end="")

    for i in range(1,num+1):
        if (num % i == 0):
            print(i,end=" ")
            count += 1
    print("\nTotal ==> "+str(count))

else:
    print("0 is OUT of range !!!")
