n=int(input())
if n!=0:
    A=input()
    A=list(A.split(" "))

    A=list(set(A))
    for i in range(len(A)): 
        A[i]=int(A[i])
    A.sort(reverse=True)
    print(A[1])
else:
    print()