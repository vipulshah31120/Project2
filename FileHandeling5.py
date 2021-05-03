file1 = open('Text2.txt', 'w')
L = ['Stefan Salvatore\n', 'Damon Salvatore\n', 'Klaus Mikealson\n', 'Elijah Mikealson\n']

file1.write('The Originals\n')
file1.writelines(L)
file1.close()                       # to change file access modes

file1 = open('Text2.txt', 'r+')
print('Output of Read Function is: ')
print()

file1.seek(0)                       # seek(n) takes the file handle to the nth
                                    # bite from the beginning.

print('Output of Readline Function is: ')
print(file1.readline())
print()

file1.seek(0)

print('Output of Read(9) function is: ')
print(file1.read(9))
print()

file1.seek(0)

print('Output of Readline(9) is: ')
print(file1.readline(9))
print()

file1.seek(0)

print('Output of Readlines function is: ')
print(file1.readlines())
print()
file1.close()

file1 = open('Text2.txt', 'a')              # append mode
file1.write('Marcellus')
file1.close()

