from datetime import date
today = date.today()
name = input()
year = int(input())
if(today.year-year >= 18):
    print("Welcome ",end="")
    print(name,end="") 
    print(" to NongGipsy Pub")
else :
    print("You shall not pass!")