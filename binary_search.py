def binarySearch(list, key):
    start=0
    end=len(list)
    while start<end:
        mid=(start+end)// 2
        if list[mid]>key:
            end=mid
        elif list[mid]<key:
            start=mid+1
        else:
            return mid
    return -1
list=input("enter the sorted list of numbers: ")
list=list.split()
list=[int(x) for x in list]
key=int(input("the number to search for: "))
index=binarySearch(list,key)
if index<0:
    print("{} was not found".format(key))
else:
    print("{} was found at index {}".format(key,index))

