def Max(l:list):
    if l != []:
        temp = Max(l[1:])
        if int(l[0]) > temp:
            return int(l[0])
        else:
            return temp
    else:
        return -99999999999999

inp = input('Enter Input : ').split()
print("Max :",Max(inp))