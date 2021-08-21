myInput = []
myInput = [int(e) for e in input("V1 : ").split()]
myInput2 = []
myInput2 = [int(e) for e in input("V2 : ").split()]
dotProduct = 0
for i in range(len(myInput)):
     dotProduct += myInput[i]*myInput2[i]
print(dotProduct)