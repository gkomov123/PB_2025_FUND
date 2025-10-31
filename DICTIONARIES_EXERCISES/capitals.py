countries = input().split(", ")
capitals = input().split(", ")

# final_dict = {country: capital for country, capital in zip(countries, capitals)}
final_dict = dict(zip(countries, capitals))

for country, capital in final_dict.items():
    print(f"{country} -> {capital}")
