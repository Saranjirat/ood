print(" *** Wind classification ***")
m = float(input("Enter wind speed (km/h) : "))
if m > 0 and m < 52:
    print("Wind classification is Breeze.")
elif m >= 52 and m < 56: 
    print("Wind classification is Depression.")
elif m >=56 and m < 102 :
    print("Wind classification is Tropical Storm.")
elif m >=102 and m < 209 :
    print("Wind classification is Typhoon.")
elif m >= 209:
    print("Wind classification is Super Typhoon.")    
elif m >= 230:
    print("Wind classification is Super Typhoon.")  
else :
    print("!!!Wrong value can't classify.")