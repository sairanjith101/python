with open ('sample.txt', 'r+') as file1:
    with open ('new.txt', 'w+') as file2:
        lines = file1.readlines()
        lines.sort()
        result = file2.writelines(lines)

file1.close()
file2.close()