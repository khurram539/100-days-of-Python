weight = int(input("weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper == "K":
    converted = int(weight) / 0.45
    print("Weight in Lbs: " + converted)
else:  
    converted = int(weight) * 0.45
    print("Weight in Kgs: " + str(converted))

