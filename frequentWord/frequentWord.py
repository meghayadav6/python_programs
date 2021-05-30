fname = input("Enter file name: ")
num_words = 0
frequent_word=" "
frequency=0
words=[]
with open(fname, 'r') as file:
    for line in file:
        line_word = line.lower().replace(',','').replace('.','').split(" ")
        num_words+=len(line_word)
        for w in line_word:
            words.append(w)
    for i in range(0,len(words)):
        count=1
        for j in range(i+1,len(words)):
            if(words[i]==words[j]):
                count=count+1
        if(count>frequency):
            frequency=count
            frequent_word=words[i]
print("Number of words:")
print(num_words)
print("most repeated word: "+frequent_word)
print("frequency of repeated word: "+str(frequency))


