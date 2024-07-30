text = input()
glasni = "AEIOU"
kevin_score, stuart_score = 0, 0

for i in range(len(text)):
    if text[i] in glasni: 
        kevin_score += len(text) - i
    else: 
        stuart_score += len(text) - i

if kevin_score > stuart_score: 
    print("Выиграл Кевин с",kevin_score)

elif kevin_score < stuart_score: 
    print("Выиграл Стюарт с",stuart_score)
else: 
    print("Ничья")    


