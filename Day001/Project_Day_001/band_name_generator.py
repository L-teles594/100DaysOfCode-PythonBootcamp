#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end

print("Welcome to the Band Name Generator.")
city = input("What's name of the city you grew up in?\n")
pet_name = input("What's your pet's name?\n")
band_name = " ".join([city, pet_name])
print(f'You band name coud be {band_name}')
