# Reference : http://pythonstudy.xyz/python/article/401-%EC%A0%95%EA%B7%9C-%ED%91%9C%ED%98%84%EC%8B%9D-Regex

import re
 
text = "phone number 010-1234-5678. use regrex"
 
regex = re.compile(r'(\d{3})-(\d{4}-\d{4})')
match = regex.search(text)
common = match.group(1)
num = match.group(2)
fullNum = match.group()
print(common, num) # 010 1234-5678


text2 = "phone number 010-1234-5678. use regrex"
 
regex2 = re.compile(r'(?P<first>\d{3})-(?P<num2>\d{4}-\d{4})')
match2 = regex2.search(text2)
first = match2.group("first")
num2 = match2.group("num2")
print(first, num2)  # 010 1234-5678
