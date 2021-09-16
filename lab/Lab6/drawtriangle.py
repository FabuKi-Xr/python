def staircase(n):
    if n>0:
        s="_"*(n-1)
        return (s+'#'*(x-len(s))+'\n')+staircase(n-1)
    if x == 0:
        return "Not Draw!"
    if n<0:
        s='#'*((n*-1))
        s="_"*((x*-1)-len(s))+s+'\n'+staircase(n+1)
        return s
    else:
        return ''
# global x
x = int(input("Enter Input : "))
print(staircase(x))
