def selection_sort(list):
    for i in range(0,len(list)-1):
        smallest=i
        for j in range(i+1,len(list)):
            if list[j]<list[smallest]:
                smallest=j
        list[i],list[smallest]=list[smallest],list[i]
list=input("enter the list of numbers: ").split()
list=[int(x) for x in list]
selection_sort(list)
print("sorted list: ",end='')
print(list)
