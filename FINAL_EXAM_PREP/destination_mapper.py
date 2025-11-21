import re

regex = r'([=/])([A-Z][A-Za-z]{2,})\1'
string_to_manipulate = input()

matches = re.findall(regex, string_to_manipulate)
print(matches)
final_matches = [match[1] for match in matches]
total_points = sum(len(city) for city in final_matches)

print('Destinations: ' + ', '.join(final_matches))
print(f'Travel Points: {total_points}')
