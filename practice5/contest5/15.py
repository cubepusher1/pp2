import re

text = input()

new_text = re.sub(r"(\d)", r"\1\1", text)

print(new_text)