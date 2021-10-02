def capital_indexes():
    print('Enter a string with capital leters without any order:')
    sentence=input()
    upperCase=[]
    for everyCharacter in sentence:
        if everyCharacter.isupper() is True:
            upperCase.append(sentence.index(everyCharacter))
    print(upperCase)
capital_indexes()
