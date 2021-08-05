import re
myInput = input()
print("".join(re.split("[aeiouAEIOU]*",myInput)))