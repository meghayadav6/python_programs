def MaxList():
    list=[]
    N=int(input("Enter Number of Values: "))
    for i in range (0,N):
        x=int(input("Enter a Value: "))
        list.append(x)
    print(list)
    Max=list[0]
    j=1
    while j<N:
        if list[j]>Max :
            Max=list[j]
        j=j+1
    print(" The Maximum Element in the List is: ",Max)
MaxList()
