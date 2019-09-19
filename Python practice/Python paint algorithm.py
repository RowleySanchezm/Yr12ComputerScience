
units = input("Please select one of the following; 1: Imperial, 2: Metric ")

if units == 1:
    print("Calculation for the amount of paint that a cuboid room needs:")
    height = float(input("Enter height in feet "))
    print(height)
    length = float(input("Enter length in feet "))
    print(length)
    width = float(input("Enter width in feet "))
    print(width)
elif units == 2:
    print("Calculation for the amount of paint that a cuboid room needs:")
    height = float(input("Enter height in metres "))
    print(height)
    length = float(input("Enter length in metres "))
    print(length)
    width = float(input("Enter width in metres "))
    print(width)
else:
    print("invalid input")
#End If
    
#Assuming that the floor does not need to be painted and room is a cuboid with no windows
PaintNeeded = ((height*length)*2) + ((height*width)*2) + (width*length)
print(PaintNeeded, "m^2") 
