myList = []
N,M,Y = [int(e) for e in input().split()]
# 0:N 1:M 2:Y
B = int((N-(Y*(1-M)))/(M-1))
print(str(int(B+N))+" "+str(B))