try:


    filename=input("Enter the file name:")
    text_url=open(filename,'r')
    count=0
    for i in  text_url:
        i = i.strip()
        count=count+1
    

        print(count,i)

except FileNotFoundError:
    print("Something Wrong, try wright correct folder name")



