year = int(input("entry a number of year: "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is leap.".format(year))
        else:
            print("{0} is not leap".format(year))
    else:
        print("{0} is leap".format(year))
else:
    print("{0} is not ".format(year))

