
units = input("Please select one of the following; 1: Imperial, 2: Metric ")

if units == 1:
    print("Calculation for the amount of paint that a cuboid room needs:")
    height = input("Enter height in feet ")
    height = float(height)
    print(height)
    length = input("Enter length in feet ")
    length = float(length)
    print(length)
    width = input("Enter width in feet ")
    width = float(width)
    print(width)
elif units == 2:
    ### SRC - Did you need to repeat all this code? Can you think of another way?
    print("Calculation for the amount of paint that a cuboid room needs:")
    height = input("Enter height in metres ")
    height = float(height)
    print(height)
    length = input("Enter length in metres ")
    length = float(length)
    print(length)
    width = input("Enter width in metres ")
    width = float(width)
    print(width)
else:
    print("invalid input")
#End If
#Assuming that the floor does not need to be painted and room is a cuboid with no windows
PaintNeeded = ((height*length)*2) + ((height*width)*2) + (width*length)
print(PaintNeeded, "m^2") 
