#demonstrate finally
# No exception Exception raised in try block
try :
    a = 5//0
    print(a)

except ZeroDivisionError :
    print('Can\'t be devided by Zero')

finally :
    print('It will always get printed')

#-----------------------------------------------------------------------------------------------------
# try for unsafe code
try :
    amount = 1000
    if amount<2000 :
        raise ValueError('Insufficient Amount!!')
    else :
        print('You can buy the Voucher.')

except ValueError as e :
    print(e)