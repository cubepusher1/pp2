import re

text = input()

match = re.search(r"^Hello", text)
if match:
    print("Yes")
else:
    print("No")