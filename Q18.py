"""
E
D E
C D E
B C D E
A B C D E
"""
a=int(input())
for i in range(a,0,-1):
    for k in range(a-i+1,0,-1):
         print(chr(64+a-k+1),end=" ")
    print()
