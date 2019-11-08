

with open("log.txt","r") as f:
    data = f.readlines()


logs = {}
for i in range(len(data)):
    data[i] = data[i].replace("\n","")

print(data[2])
buf = 0
for i in range(len(data)):
    if(buf == 0):
        if(data[i].split(',')[0] == "giris"):
            print(i)
            print("error")
        else:
            buf = 1
    else:
        if(data[i].split(',')[0] == "cikis"):
            print(i)
            print("error")
        else:
            buf = 0
       
