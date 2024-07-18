def sequence(seq,word):
    count=0
    for i in range(len(seq)):
        for j in range(i+1,len(seq)+1):
            sub=seq[i:j]
            if sub==word:
                count=count+1
    return count
seq=input("Enter the sequence")
word=input("Enter the word")
print(sequence(seq,word))