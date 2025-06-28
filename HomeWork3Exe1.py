def number_of_days(numb_mon):
    days=0
    if numb_mon< 1 or numb_mon >12:
        print("The number of a month must be in the range [1-12]")
        return None  
    elif numb_mon in {1, 3, 5, 7, 8, 10, 12}:
        days=31
    elif numb_mon== 2:
        days= 28
        print("Sometimes 29 days in a leap year")
    elif numb_mon in {4, 6, 9, 11}:
        days=30
    return days
numb_of_mon=int(input("Enter the number of a month: "))
days_in_mon=number_of_days(numb_of_mon)

if days_in_mon is not None:  
    print("That month has ",days_in_mon, "days.")
