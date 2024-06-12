side1=int(input("Enter side1:\n"))
side2=int(input("Enter side2:\n"))
side3=int(input("Enter side3:\n"))
if side1==side2==side3:
    print("Equilateral Triangle")
elif side1==side2 or side1==side3:
    print("Isoceles Triangle")
else:
    print("No Sides are Equal or Scalene")
