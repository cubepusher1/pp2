import re

with open("raw.txt", "r") as f:
    text = f.read()

pattern = re.compile(r"([A-Za-z ]+)\s+x(\d+)\s+\$(\d+\.\d{2})")

matches = pattern.findall(text)

total = 0

if matches:
    for item, qty, price in matches:
        print(f"Item: {item.strip()}, Quantity: {qty}, Price: ${price}, Total: ${round(int(qty)*float(price), 2)}")
        total += int(qty)*float(price)
else:
    print("No items found.")

if total != 0:
    print(f"Overall total is: {total}")