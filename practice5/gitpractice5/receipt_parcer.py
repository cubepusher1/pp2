import re

with open("raw.txt", "r") as f:
    text = f.read()

pattern = re.compile(r"([A-Za-z ]+)\s+x(\d+)\s+\$(\d+\.\d{2})")

matches = pattern.findall(text)

if matches:
    for item, qty, price in matches:
        print(f"Item: {item.strip()}, Quantity: {qty}, Price: ${price}")
else:
    print("No items found.")