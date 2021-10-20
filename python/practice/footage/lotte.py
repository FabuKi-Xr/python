myLotte = input()
isGetReward = False
if(myLotte.isnumeric() and len(myLotte) == 6):
    if(myLotte == "046750"):
        print("คุณถูกรางวัลที่ 1")
        isGetReward = True
    if(myLotte[0:3] == "421" or myLotte[0:3] == "666" ):
        print("คุณถูกรางวัลเลขหน้า 3 ตัว")
        isGetReward = True
    if(myLotte[3:6] == "160" or myLotte[3:6] == "355" ):
        print("คุณถูกรางวัลเลขท้าย 3 ตัว")
        isGetReward = True
    if(myLotte[4:6] == "23"):
        print("คุณถูกรางวัลเลขท้าย 2 ตัว")
        isGetReward = True
    if(not isGetReward):
        print("น่าเสียดาย คุณไม่ถูกรางวัล")
else:
    print("หมายเลขไม่ถูกต้อง")
    