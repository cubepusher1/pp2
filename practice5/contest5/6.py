import re 

text = input()

email = re.search(r"[\w.-]+@[\w.-]+\.\w+", text)

if email:
    print(email.group())
else:
    print("No email")