"""
A
AB
ABC
ABCD
ABCDE
"""
a=int(input())
b=1
for i in range(2,a+2):
    for j in range(1,i):
        print(chr(64+j),end="")
    print()
