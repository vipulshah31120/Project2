import re
def main() :
    password = "Drake2458"
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

    pat = re.compile(reg)           # compiling regex
    mat = re.search(pat, password)  # searching regex

    if mat :                        #validating conditions
        print('Password is Valid.')
    else :
        print('Password is Invalid.')

if __name__ == '__main__':
    main()
