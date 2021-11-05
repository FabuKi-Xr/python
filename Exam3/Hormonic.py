def harmonic_sum(n):
    if n > 1:
        sum = harmonic_sum(n-1)
        print(f"+ 1/{n}",end=" ")
        return sum+float(1/n)
    else:
        print("1",end=" ")
        return 1.0
print(" *** Harmonic sum ***")
num = int(input("Enter number of terms : ")) 
print("= %.8f" %(harmonic_sum(num)))