# Guided Exploration No. 3
# Nayan Patel


# import random library
import random

# declaring empty list variable named possible_names. This will be used to store all of the rap names from the rap-names.txt file.
possible_names = []

# open file named 'rap-names-output.txt' with write 'w' access
outputFile = open('rap-names-output.txt', 'w')

# open 'rap-names.txt' with read 'r' access and assign a 'handle' to the file named dataFile.
with open('rap-names.txt', 'r') as dataFile:
    # iterate through each line in the **rap-names.txt** file, one line at a time.
    for name in dataFile:
        # append to the possible_names variable each line from the 'rap-name.txt' file. Use rstrip to remove line feed at the end of the line
        possible_names.append(name.rstrip())


# prompt the user for the number of rap names to generate
count = int(input('How many rap names would you like to create? '))
# prompt the user for how many parts should be part of the entire rap name.
parts = int(input('How many parts should the name contain? '))


# use a counted loop to generate the total number of rap names the user wants to generate
for i in range(count):
    # create an empty list that will hold the rap name parts
    name_parts = []
    # use counted loop for the number of rap names that the user wants as part of the names.
    for j in range(parts):
        # randomly select a name from the **possible_names** list and append it to the **name_parts** list.
        # Using the **random.randint()** method to generate a number from 0 to the length of the **possible_names** list and then subtract one from it.
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])

        # use .write() method to write generated rap name to 'rap-names-output.txt' Take the name_parts list contents and use .join method to glue them together with a space. Add a new line character "\n" to the end of the string.
    outputFile.write(f"{' '.join(name_parts)}\n")
    # Display the newly generated rap name
    print(f"{' '.join(name_parts)}")


# close the 'rap-names-output.txt' file
outputFile.close()
