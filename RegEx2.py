import re

def findmonthanddate(string) :      #working of re.match()
    regex = r"([a-zA-Z]+) (\d+)"
    match = re.match(regex, string)

    if match == None :
        print('Not a Valid Date')
        return

    print('Given Data: ', (match.group()))
    print('Month: ', (match.group(1)))
    print('Day: ', (match.group()))


findmonthanddate('Dec 31')
print('')
findmonthanddate('I was Born on Dec 31')
