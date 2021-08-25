print("*** Rabbit & Turtle ***")
d,Vr,Vt,Vf = input("Enter Input : ").split()
time = ((int)(d)/((int)(Vt)-(int)(Vr)))
print("{:.2f}".format((int)(Vf)*time))