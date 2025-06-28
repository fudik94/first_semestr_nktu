text_url=open('urls.txt','r')
count=0
for i in  text_url:
    i = i.strip()
    count=count+1
    username = i.split('/')[-1]
    surname = username.split('-')[-1]
    

    print(surname)

