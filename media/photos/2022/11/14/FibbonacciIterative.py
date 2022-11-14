# Print Fibonacci series in python using it method

# A Fibonacci series is a series in which next number is a sum of previous two numbers.
#input --> 4
#output--> 0 1 1 2

num=int(input("Enter number :- "))

print("Below is a fibonacci sequence...")

a,b=0,1

for i in range(0,num):
    if i<=1:
        print(i)
    else:
        result=a+b
        a=b
        b=result
        print(result)













