nums=list(input().split())
dict={ }
final=[]
count=0
for i in nums:

    dict[i]=(sorted(list(i)))
for i in nums:
    result = []
    if i not in result:
        result.append(i)
    for j in nums:
        if i!=j and dict[i]==dict[j] and j not in result:
            result.append(j)
    if sorted(result)not in final:
        final.append(sorted(result))

print(final)
