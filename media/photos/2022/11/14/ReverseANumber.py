
# Reverse A Number In Python

N=123

ans=0
while N!=0:
    ans=ans*10+N%10
    N=N//10

print(ans)