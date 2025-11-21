import re

regex = r'([=][A-Z]{1}[A-Za-z]{2,}[=])|([\/][A-Z]{1}[A-Za-z]{2,}[\/])'
string_to_manipulate = input()

matches = re.findall(regex, string_to_manipulate)
total_points = 0
final_matches = []

for cities_tuple in matches:
    for city in cities_tuple:
        if city == '':
            continue
        final_matches.append(city[1:len(city) - 1])
        total_points += len(city[1:len(city) - 1])

print('Destinations: ' + ', '.join(final_matches))
print(f'Travel Points: {total_points}')
