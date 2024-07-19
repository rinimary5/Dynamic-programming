s=input("Enter the string")
dict={ }
max_len=0
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        substr=s[i:j]
        list1=list(substr)
        #print(list1)
        for q in list1:
            dict[q]=0
        for r in list1:
            dict[r]=dict[r]+1
        count=0
        for t in list1:
            if dict[t]==1:
                count=count+1
        if count==len(list1) and count>max_len:
            max_len=count
print(max_len)

