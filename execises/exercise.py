# List of countries and filenames
countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']

# Use zip() to pair countries with filenames
for country, filename in zip(countries, filenames):
    # Open each file in write mode and write the country name to it
    with open(filename, 'w') as file:
        file.write(country)

print("Countries have been written to their respective files.")