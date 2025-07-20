# Ask user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the rows
row = 0

# Outer loop controls the number of rows
while row < size:
    # Inner loop prints '*' in a single row
    for col in range(size):
        print("*", end="")  # Don't go to a new line after each star
    print()  # After each row, move to the next line
    row += 1  # Move to the next row