List = input("*** String Rotation ***\nEnter 2 strings : ").split()
round = 1
s1,s2 = List[0][-1]+List[0][:-1],List[1][1:]+List[1][0]
for i in range(len(List[0])*len(List[1])):
    if round <=5 or len(List[0]) == len(List[1])==6:
        print("{} {} {}".format(round,s1,s2))
    if s1 == List[0] and s2 == List[1]:
        if round >5 and not(len(List[0]) == len(List[1])==6):
            print(" . . . . . ")
            print("{} {} {}".format(round,s1,s2))
        print("Total of  {} rounds.".format(round))
        break
    else:
        round +=1
        s1,s2 = s1[-1]+s1[:-1],s2[1:]+s2[0]
