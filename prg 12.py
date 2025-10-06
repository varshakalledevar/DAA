def subset_sum(arr,target,i=0,path=[]):
    if sum(path)==target:
        print(path)
        return
    if i>=len(arr) or sum(path)>target:
        return
    subset_sum(arr,target,i+1,path+[arr[i]])
    subset_sum(arr,target,i+1,path)
arr=list(map(int,input("enter elements:").split()))
target=int(input("enter the sum:"))
print("subset with sum",target,":")
subset_sum(arr,target)
