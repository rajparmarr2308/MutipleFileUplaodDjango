# Print Fibonacci series in python using Recursive method

# A Fibonacci series is a series in which next number is a sum of previous two numbers.
#input --> 5
#output--> 0 1 1 2 3

num=int(input("Enter number :- "))

print("Below is a fibonacci sequence...")

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


for i in range(0,num):
    print(fib(i))



















