id=input('what is your id?')
password=input('what is your password?')

pwLength=len(password)

if(pwLength<6):
    print('length of password should be more than 6 long')

else:  
    print(f'{id}, well done')