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

#Assuming that the floor does not need to be painted and room is a cuboid with no windows
PaintNeeded = ((height*length)*2) + ((height*width)*2) + (width*length)
print(PaintNeeded, "m^2") 
