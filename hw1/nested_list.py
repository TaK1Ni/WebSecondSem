n = int(input())
records = []

for _ in range(n):
    name = input()
    score = float(input())
    records.append([name, score])

records.sort(key=lambda x: x[1])

second_highest_score = sorted(set([s[1] for s in records]))[-2]

names = [record[0] for record in records if record[1] == second_highest_score]

for name in names:
    print(name)