import re

a = input("enter 2 numbers by space\n")

pattern_1 = r'\s+'
cleaned = re.sub(pattern_1, ' ', a)
pattern_2 = r'\d+ \d+'
# a = a.strip(' .')
print(cleaned)