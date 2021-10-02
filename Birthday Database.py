import sys
import re

birthday = {'John':'Apr 6','Robert':'Jan 2','Wayne':'Oct 10'}

print('Enter the name:')
name=input()

if name in birthday.keys():
    print('Birthday of '+name+' is on '+birthday[name])

else:
    print('The name is not in database.')
    print('Do you want to see the entire databse?')
    reply=input()
    if reply=='yes':
        for names,bdate in birthday.items():
            print('Birthday of '+names+' is on '+bdate)

    print('Would you like to include '+name+' in database?')
    answer=input()
    if answer=='yes':
        print('Enter the birthdate of '+name)
        birthdate=input()
        # matching birthdate pattern
        birthdayRegex=re.compile(r'\w+\s\d\d')
        while birthdayRegex.search(birthdate) is None or birthdate[0].islower():
               print('The pattern of birthdate is : \w+\s\d\d. \nFor example Oct 06 is a valid pattern.')
               print('Please enter the correct pattern birthdate of '+name+' .')
               birthdate=input()
               birthday[name]=birthdate
       
        else:
            birthday[name]=birthdate

        print('Enter the correct name:')
        name=input()
        while name in birthday.keys():
            print('Birthday of '+name+' is on '+birthday[name])
            sys.exit()
        while name not in birthday.keys():
            print('Name '+name+' not in database.')
            sys.exit()