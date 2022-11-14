
#Palindrome number is a number which reverse is equal to number itself.
# 121 > palidrome  123 > not a palindrome

number=int(input("enter a number : "))

temp=number
reverse=0

while temp!=0:
    reverse=reverse*10 + temp%10
    temp=temp//10

if number==reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")


