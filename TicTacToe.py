import sys
tttboard={'top L':' ','top M':' ','top R':' ','mid L':' ','mid M':' ','mid R':' ','bot L':' ','bot M':' ','bot R':' '}
def printboard(board):
    print(board['top L'] + '|' + board['top M'] + '|' + board['top R'])
    print('-+-+-')
    print(board['mid L'] + '|' + board['mid M'] + '|' + board['mid R'])
    print('-+-+-')
    print(board['bot L'] + '|' + board['bot M'] + '|' + board['bot R'])

turn='X'
for i in range(9):
    printboard(tttboard)
    print('Turn for '+turn+' .Move on which space?')
    move=input()
    tttboard[move]=turn
    while int(i)>4:
        if tttboard['top L']==tttboard['top M'] and tttboard['top M']==tttboard['top R']:
            printboard(tttboard)
            print('The player '+tttboard['top L']+' has won.')
            print('Congrats!!')
            sys.exit()
        elif tttboard['mid L']==tttboard['mid M'] and tttboard['mid M']==tttboard['mid R']:
            printboard(tttboard)
            print('The player '+tttboard['mid L']+' has won.')
            print('Congrats!!')
            sys.exit()
        elif tttboard['bot L']==tttboard['bot M'] and tttboard['bot M']==tttboard['bot R']:
            printboard(tttboard)
            print('The player '+tttboard['bot L']+' has won.')
            print('Congrats!!')
            sys.exit()
        elif tttboard['top L']==tttboard['mid L'] and tttboard['mid L']==tttboard['bot L']:
            printboard(tttboard)
            print('The player '+tttboard['bot L']+' has won.')
            print('Congrats!!')
            sys.exit() 
        elif tttboard['top M']==tttboard['mid M'] and tttboard['mid M']==tttboard['bot M']:
            printboard(tttboard)
            print('The player '+tttboard['bot M']+' has won.')
            print('Congrats!!')
            sys.exit()
        elif tttboard['top R']==tttboard['mid R'] and tttboard['mid R']==tttboard['bot R']:
            printboard(tttboard)
            print('The player '+tttboard['bot R']+' has won.')
            print('Congrats!!')
            sys.exit()
        elif tttboard['top L']==tttboard['mid M'] and tttboard['mid M']==tttboard['bot R']:
            printboard(tttboard)
            print('The player '+tttboard['bot R']+' has won.')
            print('Congrats!!')
            sys.exit()
        elif tttboard['top R']==tttboard['mid M'] and tttboard['mid M']==tttboard['bot L']:
            printboard(tttboard)
            print('The player '+tttboard['bot L']+' has won.')
            print('Congrats!!')
            sys.exit()
        else:
            break
    if turn=='X':
           turn='O'
    else:
        turn='X'
printboard(tttboard)