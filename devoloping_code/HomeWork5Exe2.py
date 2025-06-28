#https://oigus.ut.ee/et/tootaja/deniss-ruder

url = input("Please enter url: ")

username = url.split('/')[-1]
surname = username.split('-')[-1]
new_surname = surname.capitalize()

print("Surname is " + new_surname)
