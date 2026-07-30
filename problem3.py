def stringstats(sentence1):
    sentence=[i for i in sentence1 if i.isalpha() or i==' ']
    words=("".join(sentence)).split()
    letters=""
    vowels=0
    upper=0
    count_letter={}
    count_words={}
    ans=[]
    for i in sentence:
        if i.lower() in ['a','e','i','o','u']:
            vowels+=1
        if i.isalpha():
            letters+=i
        if i.isupper():
            upper+=1
    for i in letters.lower():
        if i in count_letter:
            count_letter[i]+=1
        else:
            count_letter[i]=1
    for i in words:
        count_words[i]=len(i)
    for i in words:
        if count_words[i]==max(count_words.values()):
            ans.append(i)
    return len(set(letters.lower())), vowels, upper, max(count_letter.values()), sorted(ans)[0]
print(stringstats('The quick brown fox, named Roxanne, jumped over Bruno, a lazy dog.'))
