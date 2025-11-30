import re

regex = r'[*^]+([A-Za-z ]{6,})[*^]+[^A-Za-z0-9]*\++([-+]?\d+(?:\.\d+)?,[-+]?\d+(?:\.\d+)?)\++'
string = input()

matches = re.findall(regex, string)

if matches:
    for match in matches:
        artifact_name = match[0]
        coords = match[1]
        print(f'Found {artifact_name} at coordinates {coords}.')
else:
    print('No valid artifacts found.')
