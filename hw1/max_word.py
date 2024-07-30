import re

f = open('file/example.txt',encoding='utf-8', mode='r')

words = re.findall(r'\w+', f.read())
sort_word = sorted(words, key=len, reverse=True)

mx_word=[]
mx_word.append(sort_word[0])
for word in words:
    if len(word)==len(sort_word[0]) and word!=sort_word[0]:
        mx_word.append(word)

for resul in mx_word: print(resul)


f.close()