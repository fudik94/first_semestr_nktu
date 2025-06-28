while True:
    user_input = input("Enter the number of a month or word 'done': ").strip() 
    if user_input.lower() == 'done':
        break
    try:
        numb_month = int(user_input)
        
       
        if numb_month < 1 or numb_month > 12:
            print("The number of a month must be in the range [1-12]")
       
        elif numb_month in [1, 3, 5, 7, 8, 10, 12]:
            print("The number of days in this month is 31")
       
        elif numb_month == 2:
            print("The number of days in this month is 28")
       
        elif numb_month in [4, 6, 9, 11]:
            print("The number of days in this month is 30")
    

    except ValueError:
        print("Please enter a number")
