"""
ABCDEF
ABCDE
ABCD
ABC
AB
A
"""

a=int(input())
for i in range(a+1,0,-1):
    for j in range(1,i+1):
        print(chr(64+j),end="")
    print()
