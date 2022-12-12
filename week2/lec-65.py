name = input("enter name: ")
temp = ""
for i in range(0,len(name)):
    if name[i] not in temp:
        print(name[i],":",name.count[i])
        temp+=name[i]