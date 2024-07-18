def largesum(arr):
    suma=0
    max_sum=0
    #larsumsubarr=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)+1):
            subarr=arr[i:j]
            suma=sum(subarr)
            if suma>max_sum:
                max_sum=suma
                #larsumsubarr=subarr
    return max_sum
arr=list(map(int,input("Enter the array").split()))
print(largesum(arr))
