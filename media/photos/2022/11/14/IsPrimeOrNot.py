import re


def isPrimeOrNot(n):
    if n==1:
        return "not a Prime"
    for i in range(2,n):
        if n%i==0:
            return "not a Prime"
            break
    else:
        return "Prime Number"

print(isPrimeOrNot(11))
