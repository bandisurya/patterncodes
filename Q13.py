"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
a=int(input())
b=1
for i in range(a+1):
    for j in range(i):
        print(b,end=" ")
        b=b+1
    print()
