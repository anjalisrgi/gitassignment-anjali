# Python program to check if year is a leap year or not

year = 6000


if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year for the given input ".format(year))


elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year for the given input  ".format(year))


else:
    print("{0} is not a leap year for the given input  ".format(year))