# input-Enter Year-integer
year = int(input("Enter Year:\n"))
# output->string
# it is leap year,it is not leap year
# year=divisible by 4,its leap year
# year=not divisible by 4,its not leap year
# year=is divisible by 400 but not by 100
if year%4==0 and year%400==0:
   print("Leap Year")
elif year%100!=0:
    print("Not Leap Year")

