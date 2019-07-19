inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory['Pocket']=''

# print(inventory)
inventory["Pocket"]=['seashell', 'strange berry', 'lint']
# print(inventory)
# xx=inventory["backpack"]
# xx.remove('dagger')
# print(xx)
inventory['backpack'].remove('dagger')
inventory['gold']=[v for v in range(1,50,1)]
print(inventory)