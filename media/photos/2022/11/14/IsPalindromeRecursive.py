#Palindrome number is a number which reverse is equal to number itself.
# 121 > palidrome  123 > not a palindrome


number=int(input("Enter a number"))

def reverse(n):
    if n<10:
        return n
    else:
        return int(str(n%10)+ str(reverse(n//10)))

def isPalidrome(n):
    if number==reverse(n):
        return 1
    return 0


if isPalidrome(number)==1:
    print("palidrome")
else:
    print("not a palindrome")




