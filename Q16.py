"""
A
BB
CCC
DDDD
EEEEE
"""
a=int(input())
b=1
for i in range(1,a+1):
    for j in range(1,i+1):
        print(chr(64+b),end="")
    print()
    b=b+1
