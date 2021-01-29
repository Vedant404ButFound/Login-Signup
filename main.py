import pandas as pd
import hashlib
import re

df = pd.read_excel('db.xlsx')
def signUp(usenName:str,pass1:str,pass2:str,MobileNo:str='',Email:str=''):
    global df        
    pass1s = hashlib.sha1(pass1.encode()).hexdigest()
    pass2s = hashlib.sha1(pass2.encode()).hexdigest()
    if pass1s == pass2s:
        noRows = df.shape[0]
        df.loc[noRows,'User Name'] = usenName
        df.loc[noRows,'Password'] = pass1s
        df.loc[noRows,'Mobile No.'] = MobileNo
        df.loc[noRows,'Email'] = Email
        df.to_excel('db.xlsx',index=False)
        print('Account Cretaed Successfully')
    else:
        print('Passwords Did not Match')
def logIn(loguserName:str,logPassword:str):
    logPassword = hashlib.sha1(logPassword.encode()).hexdigest()
    UserInd = df.index[df['User Name']==loguserName][0]
    logpass = str(df.loc[UserInd,'Password'])
    if logpass==logPassword:
        print('Log In Sucessfully !!!')
    else:
        print('Wrong User Name Or Password')
def deleteAccount(deluserName:str,delPassword:str):
    delPassword = hashlib.sha1(delPassword.encode()).hexdigest()
    UserInd = df.index[df['User Name']==deluserName][0]
    delpass = str(df.loc[UserInd,'Password'])
    if delpass==delPassword:
        df.drop(UserInd,inplace=True)
        df.reset_index(drop=True)
        df.to_excel('db.xlsx',index=False)
        print('Account Deleted Sucessfully !!!')
    else:
        print('Wrong User Name Or Password')
userInp = input('What Do You Want To Do ?\n(1) Press [S]ign Up\n(2) Press [L]og In\n(3) Press [D]elete Account\n\n')
if userInp.lower() == 's':
    Name = input('Enter A Unique Username :\n').lower()
    # Name = hashlib.sha1(Name.encode()).hexdigest()
    userList = [user.lower() for user in df['User Name']]
    if Name in userList:
        print('User Name Is Already Taken')
    else:
        pass1 = input('Enter A Password :\n')
        pass2 = input('Renter Your Password :\n')
        mobileOrmail = input('Enter Mobile No. Or Email Id :\n')
        if mobileOrmail.isdigit():
            signUp(Name,pass1,pass2,MobileNo=mobileOrmail)
        elif re.match(r'[a-zA-Z0-9!#$%^&*()_+<>,./?;:]+@+[a-zA-Z0-9!#$%^&*()_+<>,./?;:].[a-zA-Z0-9.]+',mobileOrmail):
            signUp(Name,pass1,pass2,Email=mobileOrmail)
        else:
            print('Invaild Mobile No. Or Email Address')
elif 'l' == userInp.lower():
    Name = input('Enter A Your Username :\n')
    password = input('Enter Your Password : \n')
    logIn(Name,password)
elif 'd' == userInp.lower():
    Name = input('Enter A Your Username :\n')
    password = input('Enter Your Password : \n')
    deleteAccount(Name,password)
else:
    print('Invalid Input !!!')
