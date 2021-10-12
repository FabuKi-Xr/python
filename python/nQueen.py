from itertools import permutations
import time
# N=int(input("Enter n : "))
# sol=0
# cols = range(N)
# for combo in permutations(cols):                      
#     if N==len(set(combo[i]+i for i in cols))==len(set(combo[i]-i for i in cols)):
#         sol += 1
#         print('Solution '+str(sol)+': '+str(combo)+'\n')  
#         print("\n".join(' o ' * i + ' X ' + ' o ' * (N-i-1) for i in combo) + "\n\n\n\n")

print("Iterative")
for i in range(7):
  N=i+4
  def print_table():
      for row in range(N):
          print(table[row])

  def put_queen(x,y):
      if table[y][x] == 0:
          for m in range(N):
              table[y][m] = 1
              table[m][x] = 1
              table[y][x] = 2
              if y+m <= N-1 and x+m <= N-1:
                  table[y+m][x+m] = 1
              if y-m >= 0 and x+m <= N-1:
                  table[y-m][x+m] = 1
              if y+m <= N-1 and x-m >= 0:
                  table[y+m][x-m] = 1
              if y-m >= 0 and x-m >= 0:
                  table[y-m][x-m] = 1
          return True
      else:
          return False
  start=time.perf_counter()
  table = [[0]*N for _ in range(N)]
  temp = []
  for i in range(N):
    temp.append(i)    
  perms = permutations(temp)


  num_comb = 0

  for perm in perms:
      if put_queen(perm[0], 0) == True :
          if N==1:
  #          print_table()
            num_comb += 1
  #          print(f"solution{num_comb}")
  #          print(" ")
          elif N>1:
            if put_queen(perm[1], 1) == True :
              if N==2:
  #              print_table()
                num_comb += 1
  #              print(f"solution{num_comb}")
  #              print(" ")
              elif N>2: 
                if put_queen(perm[2], 2) == True:
                  if N==3:
  #                  print_table()
                    num_comb += 1
  #                  print(f"solution{num_comb}")
  #                  print(" ")
                  elif N>3:
                    if put_queen(perm[3], 3) == True:
                      if N==4:
  #                      print_table()
                        num_comb += 1
  #                      print(f"solution{num_comb}")
  #                      print(" ")
                      elif N>4 :
                        if put_queen(perm[4], 4) == True:
                          if N==5:
  #                         print_table()
                            num_comb += 1
  #                          print(f"solution{num_comb}")
  #                          print(" ")
                          elif N>5:
                            if put_queen(perm[5], 5) == True:
                              if N==6:
  #                              print_table()
                                num_comb += 1
  #                              print(f"solution{num_comb}")
  #                              print(" ")
                              elif N>6:
                                if put_queen(perm[6], 6) == True:
                                  if N==7 :
  #                                  print_table()
                                    num_comb += 1
  #                                  print(f"solution{num_comb}")
  #                                  print(" ")
                                  elif N>7:
                                    if put_queen(perm[7], 7) == True:
                                      if N==8 :
  #                                     print_table()
                                        num_comb += 1
  #                                      print(f"solution{num_comb}")
  #                                      print(" ")
                                      elif N>8:
                                        if put_queen(perm[8], 8) == True:
                                          if N==9 :
  #                                          print_table()
                                            num_comb += 1
  #                                          print(f"solution{num_comb}")
  #                                          print(" ")
                                          elif N>9:
                                            if put_queen(perm[9], 9) == True:
                                              if N==10 :
  #                                              print_table()
                                                num_comb += 1
  #                                              print(f"solution{num_comb}")
  #                                              print(" ")
      table = [[0] * N for _ in range(N)]
  stop=time.perf_counter()
  print("N = {}".format(N))
  print("time = {}".format(stop-start))