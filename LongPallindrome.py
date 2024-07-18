def LongPallindrome(str):
    max_len=0
    output=" "
    for i in range(len(str)):
        for j in range(i+1,len(str)+1):
            sub=str[i:j]
            if sub==sub[::-1] and len(sub)>max_len:
                max_len=len(sub)
                output=sub

    return output
s=input("Enter the string")
print(LongPallindrome(s))