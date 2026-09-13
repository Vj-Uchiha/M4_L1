def match_words(words):
   lis=[]
   count=0
   for word in words:
    print(word)
    if len(word) > 1 and word[0] == word[-1]:
            count+=1
            lis=lis.append(word)
    print("The number of words which have the same 1st and last character are: ", lis)
    return count

words_count=match_words(["nayan", "Vedant", "racecar", "wow"])
print("The number of words having the same 1st and last letter is: ", words_count)