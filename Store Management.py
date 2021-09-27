store={ 
        'Cadburies':10,'KitKat':20,'DairyMilk':30,'Amul':20,'Ambrocia':120,
        'ParleG':10,'MarryGold':20,'BourBorn':25,'Milano':30,'Oreo':35,'50-50':40,
        'Doms Pen':3,'Apsara Eraser':'5','Doms Pencil':'10','Camel Crayons':20,'Classmate':30,
        'Nivia Football':500,'Pacer TennisBall':30,'SG Bat':300,'Yonex':1500,'Shuttle Cocks':35
      }

print('Enter the number of items:')
numItems=input()
price = 0
for i in range(int(numItems)):
    print('Enter the item name:')
    itemName=input()
    print('Enter the quantity of the '+itemName+' :')
    itemQuantity=input()
    price = price + (int(store[itemName])*int(itemQuantity))
print(price)    








