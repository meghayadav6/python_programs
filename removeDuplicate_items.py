def createlist(a):
    list1=[]
    for n in a:
        if n not in list1:
            list1.append(n)
    return list1
a=list()
n=int(input("enter the size of list: "))
print("enter the number: ")
for i in range(n):
    x=int(input(""))
    a.append(int(x))
print("the new list: ",createlist(a))

