# Reference : https://stackoverflow.com/questions/8286554/using-python-find-anagrams-for-a-list-of-words
# https://en.wikipedia.org/wiki/Anagram

import re 
worker = re.compile(r'\s+') 

def isAnagram(str1, str2):
    str1_list = list(worker.sub('',str1).lower())
    str1_list.sort()
    print(str1_list)
    str2_list = list(worker.sub('',str2).lower())
    str2_list.sort()
    print(str2_list)

    return (str1_list == str2_list)

str1="McDonald's restaurants" 
str2="Uncle Sam's standard rot"

print(isAnagram(str1, str2)) # True




