n=int(input())
times=[]
for i in range(n):
    entry, exit = map(int, input().split())
    times.append([entry, exit])
T = int(input())
pasage_count=0

for time in times:
    if time[0] <= T <= time[1]: 
        pasage_count+=1

print(pasage_count)