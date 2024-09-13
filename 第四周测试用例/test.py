import pdb

pdb.set_trace()
def bubble_sort(arr):
    n=len(arr)
    for j in range(n):
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                x=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=x
    return arr
print(bubble_sort([4,2,1,8,7,6,5]))
