import os

current_dir = os.path.dirname(__file__)

def file_search(name, path=current_dir):
    flag=0
    for root, dirs, files in os.walk(path):
        if name in files:
            f = open(name)
            for _ in range(5): 
                print(f.readline())
                flag=1
                return ''
    if flag==0:
        return f"Файл {name} не найден"