

fruitList = dict()
charact = dict()
days3 = dict()
totalNumber = 0
totalTypes = 0

filename = input("Enter the file name: ")


with open(filename) as file:

    next(file)

    for i in file:

        totalNumber+=1

        i = i.rstrip("\n")

        arr = i.split(",")


        if arr[0] in fruitList.keys():

            fruitList[arr[0]] +=1

        else:
            fruitList[arr[0]] = 1
            totalTypes+=1


        temp = (arr[0],arr[2],arr[3])

        if temp in charact.keys():
            charact[temp]+=1
        else:
            charact[temp] = 1
        

        days = int(arr[4])

        if days >3:
            if arr[0] in days3.keys():
                days3[arr[0]] +=1
            else:
                days3[arr[0]] = 1


descending = sorted(fruitList.items(),key = lambda kv:kv[1],reverse=True)


print("Total number of fruit: ",totalNumber)
print("Types of fruit: ",totalTypes)
print("The number of each type of fruit in descending order")
for i in descending:
    print(i[0],": ",i[1])
print("The characteristics (size, color, shape, etc.) of each fruit by type")

for i in charact:
    print(charact[i]," ",i[0],":",i[1],",",i[2])
    
print("Have any fruit been in the basket for over 3 days")
strL = ""
length = len(days3)

for index,i in enumerate(days3):
    strL += str(days3[i]) + " "+ str(i)
    if (index != length-1):
        strL+= "s and "
    else:
        strL += "s are over 3 days old"
print(strL)
        