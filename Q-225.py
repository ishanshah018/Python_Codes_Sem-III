def fibo():
    n=int(input("Enter how many times:"))
    a=0
    b=1
    count=0
    if n<=0:
        print("Enter any number more than 0(positive)")
    elif n==1:
        print("Fibonacci sequence: ",a)
    else:
        print("Fibonacci sequence:")
        while count<n:
            print(a,end=" ")
            c=a+b
            a=b
            b=c
            count+=1
fibo()
