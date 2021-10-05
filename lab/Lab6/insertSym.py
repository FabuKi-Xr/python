def length(txt):
    if txt[0:] == txt[-1]: # เริ่มที่ตัวหน้าสุด
        print(txt[0],end="*")
        return 1
    s = length(txt[:-1]) #เอาตัวหลังสุดออก
    if s%2 == 0:
        print(txt[s],end = "*")
    else:
        print(txt[s],end="~")
    return s+1
print("\n",length(input("Enter Input : ")),sep="")