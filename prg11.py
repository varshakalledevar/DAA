def solove (n,row=0,cols=[],d1=set(),d2=set()):
    if row==n:
        for c in cols:
            print("."*c+"Q"+"."*(n-c-1))
        print()
        return
    for col in range(n):
        if col not in cols and row-col not in d1 and row+col not in d2:
            solove(n,row+1,cols+[col],d1|{row-col},d2|{row+col})
n=int(input("enter n:"))
solove(n)