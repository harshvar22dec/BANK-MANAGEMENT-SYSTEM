from datetime import datetime
def admin():
    response=input('''press C for change the Password
                press R to remove a user
                press A to remove all user data\t''').upper()
    if response=='C':change_password()
    elif response=='R':removeuser()
    elif response=='A':removeall()
    else:print('Wrong Entry')
def removeuser():
    if transac_server_password():
        ac_no=input('Enter Account No. to be Deleted\t')
        cust_name=input('Enter Full Name of the Customer\t')
        obj=open('data.txt','r');found=0
        cust_data=obj.readlines();obj.close();obj=open('data.txt','w')
        if confirmation_passw():
            for i in cust_data:
                if not i.startswith(ac_no) and i.split('%*')[0]!=ac_no:obj.write(i)
                else:found=1
            obj.close();print('Successfully Done') if found==1 else print('Account not found!')
def removeall():
    if transac_server_password() and confirmation_passw():obj=open('data.txt','w');obj.close()
    print('Successfully Erased!')


def transac_server_password():#this function is built for safe transaction:employee, other than desktop owner can't make a transaction
    obj=open('encryption.txt','r')
    curr_pass=obj.read()
    obj.close()
    if input('Enter Desktop Password\t')==curr_pass:return True
    else:print('Wrong Password, Process Failed');return False

def confirmation_passw():
    '''this function is built for confirmation:if user made any mistake,that mistake could be cleared
    before consideration'''
    obj = open('encryption.txt', 'r')
    curr_pass = obj.read()
    obj.close()
    if input('Confirm Desktop Password\t') == curr_pass:
        return True
    else:
        print('Wrong Password, Process Failed');return False

def change_password():#this function is access when you type "access":if yo forgot password, it handles
    obj=open('encryption.txt','r')
    curr_pwd=obj.read();obj.close()
    if input('Enter Current Password\t')==curr_pwd and transac_server_password() and confirmation_passw():
        new_pwd=input('Enter New Password\t')
        obj=open('encryption.txt','w')
        obj.write(new_pwd)
        return print('Successfully Done!')
    else:print('Wrong Password,Try Again!')

def New_account():
    if transac_server_password():
        ac_no=input('Enter Account No.\t')
        obj=open('data.txt','r')
        existence=obj.readlines()
        for i in existence:
            if i.startswith(ac_no):print('Sorry, This Account No. Already exists! ');obj.close();return False
        cust_name=input('Enter Name of the Customer\t').upper()
        amount=input('Enter Your first Deposition Amount in Rupees\t')
        if confirmation_passw():
            obj=open('data.txt','a')
            obj.write(ac_no+'%*'+cust_name+'%*'+amount+'%*'+'NEW ACCOUNT CREATED ON '+'%*'+str(datetime.now())[:-7]+'\n')
            obj.close()
            if obj.closed:print('Successfully Done!')

def deposition():
    if transac_server_password():
        ac_no=input('Enter Account No.\t')
        cus_name = input('Enter Name of the Customer\t').upper()
        obj=open('data.txt','r+')
        cus_data=obj.readlines();confirmation='unknown'
        for i in range(len(cus_data)):
            if cus_data[i].startswith(ac_no) and cus_name in cus_data[i]:
                amount = input('Enter Amount to deposit\t')
                updat=cus_data[i].split('%*')
                updat[3]='DEPOSITED ON '
                updat[4]=str(datetime.now())[:-7]
                print(f'Amount before deposition: Rs. {updat[2]}')
                try:
                    updat[2]=str(float(updat[2])+abs(float(amount)))
                    print(f'Amount After deposition: Rs. {updat[2]}')
                    cus_data[i]='%*'.join(updat)+'\n'
                    obj.close()
                    if obj.closed:
                        if confirmation_passw():
                            obj=open('data.txt','w')
                            for i in cus_data:
                                obj.write(i)
                            obj.close()
                            if obj.closed:print('Successfully Done! ')
                            confirmation=True
                        else:confirmation=False
                except:print('Wrong Amount Entered\t');return ''
        if confirmation=='unknown':print("This Account No. doesn't exist")
        elif not confirmation:print('Wrong Confirmation Password! ')

def withdrawl():
    if transac_server_password():
        ac_no=input('Enter Account No.\t')
        cus_name = input('Enter Name of the Customer\t').upper()
        obj=open('data.txt','r+')
        cus_data=obj.readlines();confirmation='unknown'
        for i in range(len(cus_data)):
            if cus_data[i].startswith(ac_no) and cus_name in cus_data[i]:
                amount = input('Enter Amount to withdraw\t')
                updat=cus_data[i].split('%*')
                updat[3]='WITHDRAWLED ON '
                updat[4]=str(datetime.now())[:-7]
                print(f'Amount before WITHDRAWL: Rs. {updat[2]}')
                try:
                    updat[2] = str(float(updat[2])-abs(float(amount)))
                    print(f'Amount After WITHDRAWL: Rs. {updat[2]}')
                    cus_data[i] = '%*'.join(updat) + '\n'
                    obj.close()
                    if obj.closed:
                        if confirmation_passw():
                            obj = open('data.txt', 'w')
                            for i in cus_data:
                                obj.write(i)
                            obj.close()
                            if obj.closed: print('Successfully Done! ')
                            confirmation = True
                        else:
                            confirmation = False
                except:
                    print('Wrong Amount Entered\t');return ''
        if confirmation == 'unknown':
            print("This Account No. doesn't exist")
        elif not confirmation:
            print('Wrong Confirmation Password! ')

def enquiry():
    if transac_server_password():
        obj=open('data.txt','r')
        cust_data=obj.readlines()
        ac_no = input('Enter Account No.\t')
        cus_name = input('Enter Name of the Customer\t').upper()
        for i in cust_data:
            if i.startswith(ac_no) and cus_name in i:
                found=i.split('%*')
                print(f'\nAccount No.: {found[0]}\nNAME: {found[1]}\t\tBALANCE: {found[2]}\nLast Activity:{found[3][:-4]}')
                break
        else:print("This Account doesn't exist")

