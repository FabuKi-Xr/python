inp = list(map(int,(input('Enter Input : ').split())))

count = 1
for i in range(len(inp)):
    move = None
    isSorted = False
    for j in range(len(inp)-i-1):
        if inp[j] > inp[j+1]:
            inp[j],inp[j+1] = inp[j+1],inp[j]
            move = inp[j+1]
            isSorted = True
    if isSorted :
        if count == len(inp)-1:
            print(f"last step : {inp} move[{move}]")
            break
        else:
            print(f"{count} step : {inp} move[{move}]") 
    else:
        print(f"last step : {inp} move[None]")
        break
    count +=1
    
