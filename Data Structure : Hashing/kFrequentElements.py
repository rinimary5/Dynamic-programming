def second(a):
    return a[1]
final=[]
nums=list(map(int,input("Enter the list").split()))
k=int(input("Enter value of K"))
dict={ }
for i in nums:
    dict[i]=0
#To get the frequency
for i in nums:
    dict[i]=dict[i]+1
#Sorting in descending order inorder to get most frequent elements at top
result=sorted(dict.items(),key=second,reverse=True)
#For printing top K frequent elements
for i in range(k):
    final.append(result[i][0])
print(final)