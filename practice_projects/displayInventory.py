stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory:")
    total_num = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        total_num += v
    print("Total number of items: " + str(total_num))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.setdefault(item, 0)

addToInventory(stuff, dragonLoot)
displayInventory(stuff)
