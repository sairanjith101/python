# Step 1: Read the contents of sampleFile.txt
with open('sampleFile.txt', 'r') as file:
    lines = file.readlines()

# Step 2: Sort the lines in ascending order
sorted_lines = sorted(lines)

# Step 3: Write the sorted lines to a new file, sortedFile.txt
with open('sortedFile.txt', 'w') as sorted_file:
    sorted_file.writelines(sorted_lines)

print("The lines have been sorted and written to sortedFile.txt.")
