myInput = int(input())
sum = 0
while(myInput!=0):
    sum += myInput%10
    myInput = int(myInput//10)
    if(myInput==0 and sum>=10):
        myInput = sum
        sum = 0
print(sum)