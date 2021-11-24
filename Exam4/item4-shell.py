def shell(l, dIncrements):
    count = 0
    for inc in dIncrements: 
        isSwap = True
        for i in range(inc,len(l)): 
            iEle = l[i]   
            for j in range(i, -1, -inc):
                count += 1
                if iEle<l[j-inc] and j >= inc:
                    l[j] = l[j-inc]
                    isSwap = True
                else:
                    l[j] = iEle
                    break
                print(count,l)

    return count

print(' *** Shell sort ***')
l = list(map(int,input('Enter some numbers : ').split()))
dIncrements = [3,1]
print(shell(l, dIncrements))
print(str(l))
