pin=int(input('enter your pin number: \t'))
if pin==112233:
    print('pin is satisfied')
    account=input(' seleect your account type : \t')
    
    if account=='saving':
        print('account type is matched')
        amount=int(input('enter the amount to withdraw : \t'))
        balance=100000
        if amount<balance:
            print(amount, 'is debited from your account')
        else:
            print('insufficient funds in your account')
    else:
        print('account type is not matched')

else:
    print('pin is incorrect')



'''
account=str(input(' seleect your account type : \t'))
if acoount=='saving':
    print('account number is matched')
    amount=int(input('enter the amount to withdraw : \t'))
    balance=100000
    if amount<balance:
        print(amount, 'is debited from your account')
    else:
        print('insufficient funds in your account')
else:
    print('account number is not matched')
'''






# this is changed from the remote server github account
