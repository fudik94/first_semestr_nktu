
temps_act = open('temps.txt', 'r')


f_temps=[]

for i in temps_act:
    c_degree = i.strip()  
    c_degree =float(c_degree)  
    f_degree = c_degree*1.8+32  
    f_temps.append(f_degree)  
    print("Temperature in F =", f_degree)

temps_act.close()

if f_temps:  
    sred_temp = sum(f_temps) / len(f_temps)
    max_temp = max(f_temps)
    min_temp = min(f_temps)

    print("Average temperature :",sred_temp)
    print("Maximum temperature :", max_temp)
    print("Minimum temperature :", min_temp)


else:

    print("Something wrong")
