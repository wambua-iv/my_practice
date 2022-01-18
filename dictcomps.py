DIAL_CODES = [(86, 'China'),(91, 'India'),(1, 'United States'),(62, 'Indonesia'),(55, 'Brazil'),(92, 'Pakistan'),(880, 'Bangladesh'),(234, 'Nigeria'),(7, 'Russia'),(81, 'Japan')]
country_codes = {country: code for code, country in DIAL_CODES}

print(country_codes)

colors = ['black', 'white']
sizes = ['S', 'L', 'M']

t_shirts = [{color: size} for color in colors for size in sizes]
print(repr(t_shirts))


#avoid complex comprehensions