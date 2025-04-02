# List of countries
countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]

# Loop through each country in the list
for country in countries:
    # Create a filename based on the country name (e.g., "Albania.txt")
    filename = f"{country}.txt"

    # Open the file in write mode and write the country name as content
    with open(filename, 'w') as file:
        file.write(country)

print("Text files have been created for each country.")