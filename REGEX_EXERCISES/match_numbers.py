import re

regex = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
numbers = input()
matches = re.finditer(regex, numbers)

for match in matches:
    print(match.group(), end=' ')
