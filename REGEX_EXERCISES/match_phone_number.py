import re

regex = r'\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b'
phone_numbers = input()

matches = re.findall(regex, phone_numbers)

print(", ".join(matches))
