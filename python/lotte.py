myLotte = input()
if(myLotte.isnumeric() and len(myLotte) == 6):
    if(myLotte == "046750"):
        print("คุณถูกรางวัลที่ 1")
    elif(myLotte[0:3] == "421" or myLotte[0:3] == "666" ):
        print("คุณถูกรางวัลเลขหน้า 3 ตัว")
    elif(myLotte[3:6] == "160" or myLotte[3:6] == "355" ):
        print("คุณถูกรางวัลเลขท้าย 3 ตัว")
    elif(myLotte[4:6] == "23"):
        print("คุณถูกรางวัลเลขท้าย 2 ตัว")
    else:
        print("น่าเสียดาย คุณไม่ถูกรางวัล")
else:
    print("หมายเลขไม่ถูกต้อง")
    