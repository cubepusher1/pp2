import re

text = input()
sub_text = input()

match = re.findall(sub_text, text)

print(len(match))