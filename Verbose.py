import re

def validate_email(email) :
    regex_email = re.compile(r""" 
                            ^([a-z0-9_\.-]+)
                             @
                             ([0-9a-z\.-]+)
                             \.
                             ([a-z] {2,6})$
                            """, re.VERBOSE | re.IGNORECASE)

    res = regex_email.fullmatch(email)

    if res :
        print('{} is Valid. Details are Given: \n'.format(email))
        print('local:{}'.format(res.group(1)))
        print('Domain:{}'.format(res.group(2)))
        print('Top level domain:{}'.format(res.group(3)))
        print()

    else :
        print('{} is Invalid \n'.format(email))

validate_email("nielnitinmukesh124@gmail.com")
validate_email('King@yahoo.com@')
validate_email('Nima2@gmail.com')
validate_email('Romanpierce@@yahoo.com')