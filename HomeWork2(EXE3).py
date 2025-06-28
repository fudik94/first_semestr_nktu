try:
    numb_month=int(input("Enter the number of a month:"))
    typ_year=int(input("Enter a year:"))


    if numb_month <0 or numb_month >12 :
        print(" The number of a month must be in the range [1-12]")
    elif numb_month == 1:
        print("That month has 31 days in it.")
    elif numb_month == 2:
        print("That month has 28 or 29(depends of year) days in it.")
    elif numb_month == 3:
        print("That month has 31 days in it.")
    elif numb_month == 4:
        print("That month has 30 days in it.")
    elif numb_month == 5:
        print("That month has 31 days in it.")
    elif numb_month == 6:
        print("That month has 30 days in it.")
    elif numb_month == 7:
        print("That month has 31 days in it.")
    elif numb_month == 8:
        print("That month has 31 days in it.")
    elif numb_month == 9:
        print("That month has 30 days in it.")
    elif numb_month == 10:
        print("That month has 31 days in it.")
    elif numb_month == 11:
        print("That month has 30 days in it.")
    elif numb_month == 12:
        print("That month has 31 days in it.")
    if typ_year % 4 ==0:
        if typ_year % 100 ==0:
             if typ_year % 400 ==0:
                  print("That month has 29 days in it (a leap year)")
             else:
                print("That month has 28 days in it (a common year)")
        else :
            print(" That month has 29 days in it (a leap year)")
    else :
       print("That month has 28 days in it (a common year)")


except ValueError :
            print("Pls enter a number.")
