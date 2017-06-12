#! python3
'''inventory'''

import os

STUFF = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
DRAGON_LOOT = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    '''display'''
    print("Inventory:")
    total_num = 0
    for k, value in inventory.items():
        print(str(value) + " " + k)
        total_num += value
    print("Total number of items: " + str(total_num))

def add_to_inventory(inventory, added_items):
    '''add item to inventory'''
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.setdefault(item, 0)

add_to_inventory(STUFF, DRAGON_LOOT)
display_inventory(STUFF)

os.system('pause')
