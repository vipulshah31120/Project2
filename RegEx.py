import re
p = re.compile('[a-e]')
print(p.findall('Keepin my composure, never soberNever chokin, always smokin doja'))

p = re.compile('\d')
print(p.findall('I was born on 31st Dec, 1998'))

p = re.compile('\d+')                           # \d+ will match a group on [0-9], group of one or greater size
print(p.findall('I was born on 31st Dec, 1998'))

p = re.compile('\W')
print(p.findall('My Phone\'s Password is: *****'))  # \W matches to non alphanumeric characters.

p = re.compile('ab*')
print(p.findall('ababbbabbbaabbaaba'))              #Our RE is ab*, which ‘a’ accompanied by any no. of ‘b’s, starting from 0.
                                                    #Output ‘ab’, is valid because of single ‘a’ accompanied by single ‘b’.
                                                    #Output ‘abb’, is valid because of single ‘a’ accompanied by 2 ‘b’.
                                                    #Output ‘a’, is valid because of single ‘a’ accompanied by 0 ‘b’.
                                                    #Output ‘abbb’, is valid because of single ‘a’ accompanied by 3 ‘b’




