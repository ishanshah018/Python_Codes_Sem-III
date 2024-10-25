def reverse(n):
    sum=0
    while n!=0:
        rem=n%10
        sum=sum*10+rem
        n=n//10
    print("Reversed Number is:",sum)

n=int(input("Enter any number to reverse it; "))
reverse(n)
