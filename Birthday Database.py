import sys
birthday={'John':'Apr 6','Robert':'Jan 2','Wayne':'Oct 10'}
print('Enter the name:')
name=input()
if name in birthday.keys():
    print('Birthday of '+name+' is on '+birthday[name])
else:
    print('The name is not in database.')
    print('Would you like to include '+name+' in database?')
    answer=input()
    if answer=='yes':
        print('Enter the birthdate of '+name)
        birthdate=input()
        birthday[name]=birthdate
        print('Enter the correct name:')
        name=input()
        while name in birthday.keys():
            print('Birthday of '+name+' is on '+birthday[name])
            sys.exit()
        while name not in birthday.keys():
            print('Name  '+name+ ' not in database,please fuck off')
            sys.exit()