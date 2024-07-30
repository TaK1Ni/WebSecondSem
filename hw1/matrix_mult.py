n = int(input())
A = [[0] * n for _ in range(n)]
B = [[0] * n for _ in range(n)]
for i in range(n):
    str1=input().split(" ")
    for j in range(n):
        A[i][j]=int(str1[j])
for i in range(n):
    str1=input().split(" ")
    for j in range(n):
        B[i][j]=int(str1[j])

C = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]

for i in range(n):
    for j in range(n):
        print(C[i][j], end=' ')
    print()