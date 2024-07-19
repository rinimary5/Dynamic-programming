nums=list(map(int,input("Enter the list").split()))
target=int(input("Enter the target"))
sum=0
result=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            result.append(i)
            result.append(j)
print(result)


