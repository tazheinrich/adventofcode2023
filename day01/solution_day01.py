# Import re package to work with regular expressions
import re

# Define input file
file = "input.txt"

# Open file, read in lines and clean them
with open(file, "r") as file:
    input = [line.strip() for line in file.readlines()]

# Define solutions
solution_part1 = 0
solution_part2 = 0

# Define dictionary to translate verbal numbers to number symbols
names_numbers = {"names": ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],
                 "numbers": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                 }

# Define pattern to look for numbers and possibly overlapping names 
pattern = "(?=(" + "|".join(["\d"] + names_numbers["names"]) + "))"

# Loop through lines of input
for line in input:
    # Find every digit
    digit1 = re.findall(r"\d", line)
    # Store first and last digit as integerin double_digit1
    double_digit1 = int(digit1[0] + digit1[-1])
    # Sum each double digit for solution to first part
    solution_part1 += double_digit1

    # Look for digits in line defined in pattern
    digit2 = re.findall(pattern, line)
    # Loop through each element in found digits
    for i in range(len(digit2)):
        # If digit is in dictionary store index
        if digit2[i] in names_numbers["names"]:
            index = names_numbers["names"].index(digit2[i])
            digit2[i] = names_numbers["numbers"][index]
    # Convert to double digits
    double_digit2 = int(digit2[0] + digit2[-1])
    # Sum double digits for solution to first part
    solution_part2 += double_digit2

print(f"The solution for part 1 is: {solution_part1}")
print(f"The solution for part 2 is: {solution_part2}")