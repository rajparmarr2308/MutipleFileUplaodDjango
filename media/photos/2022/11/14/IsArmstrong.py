# Program to check a number is Armstrong or not in Python

# It is a number which is equal to the sum of cube of its digits.

# For eg: 153, 370 etc.

N=46
temp=N
ans=0

while temp!=0:
    i=temp%10
    ans=ans+pow(i,3)
    temp=temp//10


if N==ans:
    print("number is armstrong")
else:
    print("not armstrong")

