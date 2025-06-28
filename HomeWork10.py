import datetime
with open("dates.txt") as fl:
    dictor = {}
    for line in fl:
        line = line.strip()  
        
        date = datetime.datetime(int(line[0:4]), int(line[5:7]), int(line[8:10]))
        numDay = date.weekday()  
        
        match numDay:
            case 0:
                dictor[line] = "Monday"
            case 1:
                dictor[line] = "Tuesday"
            case 2:
                dictor[line] = "Wednesday"
            case 3:
                dictor[line] = "Thursday"
            case 4:
                dictor[line] = "Friday"
            case 5:
                dictor[line] = "Saturday"
            case 6:
                dictor[line] = "Sunday"

for date, weekday in dictor.items():
    print(f"{date} => {weekday}")

with open('dates_with_day.txt', 'w') as file:
    for date, weekday in dictor.items():
        file.write(f"{date}: {weekday}\n")
