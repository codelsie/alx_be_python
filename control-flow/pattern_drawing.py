# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to go through each row
while row < size:
    # Use a for loop to print asterisks in each row
    for _ in range(size):
        print("*", end="")  # Print * without newline
    print()  # Move to the next line after a row
    row += 1