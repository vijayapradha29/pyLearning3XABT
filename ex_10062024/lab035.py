alculate area of the circle
# input->radius
# output->area of circle
#we have taken float becoz user can give radius in points also
# datatypes->input->can be integer,float->lets tak float
# output->float


# core logic=pi*r*r
# pi=3.14
radius = input("Enter the radius:\n")  # this will give string value,so we need to convert it to float
radius = float(radius)
import math
# or
# radius=float(input("Enter the radius:/n")) can be given in single line also
print(math.pi)
area = math.pi * (radius ** 2)
area2 = math.pi * (math.pow(radius, 2))
print(area)
print(area2)
#or
import math
print(math.pi*(float(input("Enter the radius:\n"))**2))
#or
print(3.14*(float(input("Enter the Radius:\n"))**2))
