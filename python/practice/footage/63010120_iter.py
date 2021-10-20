### iteration ###
from itertools import permutations
import time
N=int(input("Enter n: "))
start=time.perf_counter()
print("========== iteration ============")
sol=0
cols = range(N)
for combo in permutations(cols):                      
    if N==len(set(combo[i]+i for i in cols))==len(set(combo[i]-i for i in cols)):
        sol += 1
          #print('Solution '+str(sol)+': '+str(combo)+'\n')  
          #print("\n".join(' o ' * i + ' X ' + ' o ' * (N-i-1) for i in combo) + "\n\n\n\n")
stop=time.perf_counter()
print("N = {}".format(N))
#print('number of Solution : '+str(sol))  
print("time = {}".format(stop-start))