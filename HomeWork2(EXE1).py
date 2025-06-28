stud_points = int(input("Enter the number of points:"))

if stud_points > 100 :
        print("You cannot obtain so many points")
elif stud_points < 0 :
        print("You cannot obtain negative points")
elif stud_points >= 66 :
        print("Gongrats!The obtained points are enough to be considered for admission")
elif stud_points < 66 :
        print("Kahjuks!The obtained points are NOT enough to be considered for admission ")
else:
    print("something went wrong")