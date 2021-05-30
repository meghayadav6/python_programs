def compute_gcd(x,y):
    if x<y:
        smaller=x
    else:
        smaller=y
    for i in range(1,smaller+1):
        if(x%i==0)and(y%i==0):
            gcd=i
    return gcd
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
print("The G.C.D. of ", num1," and ", num2," is = ", compute_gcd(num1, num2))
