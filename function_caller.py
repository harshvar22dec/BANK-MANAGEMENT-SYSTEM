from FUNCTION_DEF import *
while True:
    print(''' 
                WELCOME IN CIVIL PUBLIC BANK
            Press E for Enquiry.
                press D for Deposition.
                    Press W for Withdrawl
                        Press N for New Account
                            Press S for Admin Services''')
    activity=input('\t').upper()
    if activity=='E':enquiry()
    elif activity=='D':deposition()
    elif activity=='W':withdrawl()
    elif activity=='N':New_account()
    elif activity=='S':admin()
    else:print('Wrong Entry!')
