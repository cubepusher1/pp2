import re 

res = re.compile(r"^\d+$")
text = input()

if bool(res.search(text)):
    print("Match")
else:
    print("No match")