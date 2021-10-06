speed = float(input(" *** Wind classification ***\nEnter wind speed (km/h) : "))
if speed>=0:
    print("Wind classification is ",end="")
    if speed >= 209.00:
        print("Super Typhoon.")
    elif speed >= 102.00:
        print("Typhoon.")
    elif speed >= 56.00:
        print("Tropical Storm.")
    elif speed >= 52.00:
        print("Depression.")
    else:
        print("Breeze.")
else:
    print("!!!Wrong value can't classify.")