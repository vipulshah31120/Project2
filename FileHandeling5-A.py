# append data to a file using 'with' statement
L = ['Stefan Salvatore\n', 'Damon Salvatore\n', 'Klaus Mikealson\n', 'Elijah Mikealson\n']

with open('Text2.txt', 'w') as file1 :
    file1.write('Hello\n')
    file1.writelines(L)

with open('Text2.txt', 'a') as file1 :
    file1.write('Today')

with open('Text2.txt', 'r+') as file1 :
    print(file1.read())

