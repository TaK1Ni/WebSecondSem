n = int(input())

arr=[]

for i in range(n):

    comanda = input().split(" ")
    
    if comanda[0]=="insert":
        arr.insert(int(comanda[1]),int(comanda[2]))

    elif comanda[0]=="print":
        print(arr)

    elif comanda[0]=="remove":
        arr.remove(int(comanda[1]))
        
    elif comanda[0]=="append": 
        arr.append(int(comanda[1]))

    elif comanda[0]=="sort": 
        arr.sort()

    elif comanda[0]=="pop": 
        arr.pop()

    elif comanda[0]=="reverse": 
        arr.reverse()



