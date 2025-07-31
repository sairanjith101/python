'''#multiple value in list
number = [1,2,3,4,5]
cube = [num*num*num for num in number]
print(cube)

#upper case
language = ['python', 'java', 'perl', 'sql']
upper_case = [langs.upper() + ' ' +'language!!!' for langs in language]
print(upper_case)
'''

#sort the list besed on value
marks = [80,40,30,60,20,90]
pass_mark = [m for m in marks if m>=50]
print(pass_mark)
print(sorted (pass_mark) [-2])