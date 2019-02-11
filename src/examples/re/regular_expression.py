import re

text = 'This is a string with term1, but not the other term.'

result = re.search('term1', text)

print(result.start(), result.end())

found_all = re.findall('match', 'Here is one match, here is another match')

print(found_all)

