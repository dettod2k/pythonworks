weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in LBS is: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in KGS is: " + str(converted))
