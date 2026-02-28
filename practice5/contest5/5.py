import re

text = input()

if (re.search(r"^[a-z]", text) and re.search(r"\d$", text)) or re.search(r"^[A-Z]", text) and re.search(r"\d$", text):
    print("Yes")
else:
    print("No")
