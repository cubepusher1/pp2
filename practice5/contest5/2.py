import re

text = input()
sub_text = input()

if re.search(sub_text, text):
    print("Yes")
else:
    print("No")