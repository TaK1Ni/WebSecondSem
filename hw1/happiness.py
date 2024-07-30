n, m = map(int, input().split())
arr = list(input().split(" "))

happy=0

A = {value for value in input()}
B = {value for value in input()}

for val in arr:
    if val in A: 
        happy += 1
    if val in B: 
        happy -= 1

print(happy)