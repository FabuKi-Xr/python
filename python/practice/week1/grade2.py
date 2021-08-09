grade = "FFFFFFDCBAA"
myInput = int(input())
if(myInput%10 >=5 and myInput<90):
    print(grade[myInput//10]+"+")
else :
    print(grade[myInput//10])