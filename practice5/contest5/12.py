import re 

text = input()

res = re.findall(r"\d+", text)
new_res = []

for i in res:
    if len(i) >= 2:
        new_res.append(i)

for i in new_res:
    print(i, end=" ")
    