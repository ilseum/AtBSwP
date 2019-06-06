myPets = ['Zophie', 'Pooka', 'Fatty']
print('Enter pet name:')
name = input()
if name not in myPets:
    print('no pet name ' + name)
else:
    print(name + ' is my pet.')
