my_list = ['name (given name if applicable)', 'last name', 'phone number', 'date of birth']

my_f = open('text_1.txt', 'w')
personalInfo = [(input(f'Enter your {el}: ')) + '\n' for el in my_list]
my_f.writelines(personalInfo)
my_f.close()

print()
my_f = open('text_1.txt', 'r', encoding='utf-8')

content = my_f.readlines()

print(f'There are {len(content)} lines in the file.\n')
for i in range(len(content)):
    line = content[i][:-1]
    print(f'The {i + 1} line is "{line}".\nIn the {i + 1} line there are {len(content[i].split())} word(s).\n')
my_f.close()
