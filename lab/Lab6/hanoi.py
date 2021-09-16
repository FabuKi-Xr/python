def move(n,Fromlist:list,tolist:list,auxlist:list,maxn) : #(n,from rod,to rod,auxrod) #จำนวนบรรทัด = maxn

    if n == 1 :
        print('move',n, 'from ', Fromlist[0],'to', tolist[0])
        tolist.append(Fromlist.pop())
        tower(maxn)
    else :       
        move(n-1,Fromlist,auxlist,tolist,maxn) #from , aux , to                 
        print('move',n, 'from ', Fromlist[0], 'to', tolist[0])
        tolist.append(Fromlist.pop())
        tower(maxn)
        move(n-1,auxlist,tolist,Fromlist,maxn)#aux , to , from
def tower(maxn=0):   
    if maxn > 0 :
                if maxn == x:
                    print ("|  |  |")
                if len(A) > maxn: #กรณีปริ้นท์อันเเรก
                    print(str(A[maxn]),end="  ")
                else: 
                    print("|",end="  ")

                if len(B) > maxn: #กรณีมีการย้ายห่วง
                    print(str(B[maxn]),end="  ")
                else: 
                    print ("|",end="  ")
                if len(C) > maxn:
                    print(str(C[maxn]),end="  ")
                else:
                    print ("|",end="  ")
                print("")# newline
                tower(maxn-1)

    #base case : maxn < 0 do nothing
global x ;
global A,B,C #from,aux,to
n = int(input("Enter Input : "))
x = n
A,B,C = ['A'],['B'],['C']
A.extend(range(n,0,-1))
tower(n)
move(n,A,C,B,n)
