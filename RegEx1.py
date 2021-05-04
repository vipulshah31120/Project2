import re
regex = r"([a-zA-Z]) (\d+)"
match = re.search(regex, 'I was born on dec 31')

if match != None :
    print('Match at Index %s, %s' % (match.start(), match.end()))
    print('Full Match: %s' % (match.group(0)))
    print('Month: %s' % (match.group(1)))
    print('Day: %s' % (match.group(2)))

else :
    print('The Regex pattern Doesn\'t Match')


