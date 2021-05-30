def linear_search(list,key):
    for i in range(len(list)):
        if list[i]==key:
            return i
    return -1
list=input("enter the list of numbers: ")
list=list.split()
list=[int(x) for x in list]
key=int(input("the number to search for: "))
index=linear_search(list,key)
if index<0:
    print("{} was not found".format(key))
else:
    print("{} was found at index {}".format(key,index))
