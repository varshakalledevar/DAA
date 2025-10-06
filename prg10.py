def knapsack(wt,val,W):
    ratio=[(val[i]/wt[i],wt[i],val[i])for i in range(len(wt))]
    ratio.sort(reverse=True)
    total=0
    for r,w,v in ratio:
        if W>=w:
            W-=w;total+=v
        else:
            total+=r*W;break
    return total
n=int(input("enter items:"))
wt=[];val=[]
for i in range(n):
    w,v=map(int,input(f"Weight Value{i+1}:").split())
    wt.append(w);val.append(v)
W=int(input("Capacity:"))
print("Max value:",knapsack(wt,val,W))