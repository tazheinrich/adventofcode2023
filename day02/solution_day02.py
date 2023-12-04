# Define input file
file = "input.txt"

# Read input file by line and clean it
with open(file, "r") as file:
    input = [line.strip() for line in file.readlines()]

# Define solutions
solution_part1 = 0
solution_part2 = 0

# Read input by line
for line in input:
    # Define each line as possible
    possible = True
    # Split line into id and draw
    id, draw = line.split(":")
    # Define dictionary to store values of second part
    color_counts = {"red": 0, "green": 0, "blue": 0}
    # Split draw into draws
    for draws in draw.split(";"):
        # Split draws into cubes
        for cubes in draws.split(","):
            # Split cubes into count and color
            count, color = cubes.split()
            # Convert count to integer
            count = int(count)
            # Looks for maximum number of cubes per color
            color_counts[color] = max(color_counts[color], count)
            # Check if the count the defined thresholds & add 0 if color not in draw
            if count > {"red": 12, "green": 13, "blue": 14}.get(color, 0):
                possible = False
    # Sum the integers of line number if possible is True
    if possible:
        solution_part1 +=int(id.split()[-1])        
    # Define the score for solution part 2
    score = 1
    # For values in color_counts add the values to score and multiply with 1
    for values in color_counts.values():
        score *= values
    # Add the scores for each step
    solution_part2 += score

# Print the solutions
print(f"The solution for part 1 is: {solution_part1}")
print(f"The solution for part 2 is: {solution_part2}")