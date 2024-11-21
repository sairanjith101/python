with open ('samplefile.txt', 'r+') as file1:
    with open ('newfile.txt', 'w+') as file2:
        lines = file1.readlines()
        for line in lines:
            if "melon" in line.lower():
                file2.writelines(line)

file1.close()
file2.close()