#!/usr/bin/python3

def showInstructions():
    print('''
            RPG Game
            ----------
            Commands:
              go [direction]
              get [item]
              exit
              status
    ''')

def showStatus():
    print('-----------------')
    print(f"You are in the {currentRoom}")
    print("Inventory: " + str(inventory))
    if "item" in rooms[currentRoom]:
        print(f"You see a {rooms[currentRoom]['item']}")
    print("---------------------")

inventory = []

rooms = {
            'Hall':     {
                        'south': 'Kitchen',
                        'east':  'Dining Room',
                        'west':  'Hall Closet',
                        'up':    'Attic',
                        'item':  'skeletonkey'
                        },
            'Kitchen':  {
                        'north': 'Hall',
                        'item':  'monster'
                        },
            'Dining Room': {
                        'west': 'Hall',
                        'south': 'Garden',
                        'item':  'cookies'
                        },
            'Garden':   {
                        'north': 'Dining room'
                        },
            'Hall Closet': {
                        'east': 'Hall',
                        'down': 'Cave of Bad Dreams',
                        'item': 'thermalsuit'
                        },
            'Cave of Bad Dreams':     {
                        'up':    'Hall Closet',
                        'north': 'Cave of Secrets',
                        'south': 'Cave of Lava',
                        'west':  'Cave of Frozen Memories',
                        'east':  'Cave of Oblivion',
                        'item':  'baddreams'
                        },
            'Cave of Secrets': {
                        'south': 'Cave of Bad Dreams',
                        'item': 'diamonds'
                        },
            'Cave of Lava': {
                        'north': 'Cave of Bad Dreams'
                        },
            'Cave of Frozen Memories': {
                        'east': 'Cave of Bad Dreams',
                        'item': 'frozencaveman'
                        },
            'Cave of Oblivion': {
                        'west': 'Cave of Bad Dreams'
                        }
        }

currentRoom = 'Hall'

while True:
    showInstructions()
    showStatus()
    move = ''
    while move == '':
        move = input("> ")

    move = move.lower().split()
    if move[0] == 'status':
        showStatus()

    if move[0] == 'exit':
        print("Get outta here you COWARD!")
        break

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("You cannot go that way!")

    if move[0] == 'get':
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            print(f"You just picked up {move[1]}!")
            del rooms[currentRoom]['item']

        else:
            print("You cannot pick that up!")

    if currentRoom == 'Cave of Bad Dreams':
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            print(f"You just picked up {move[1]}!")
            del rooms[currentRoom]['item']
            print("You will now have bad dreams forever!")

    if currentRoom == 'Garden' and 'skeletonkey' in inventory:
        print("You open the old rusty gate in the garden with the skeleton key and escape!  YOU WIN!")

    if currentRoom == 'Kitchen' and 'cookies' in inventory and 'monster' in rooms[currentRoom]['item']:
        print("The monster has just taken your cookies!!")
        del inventory['item']

    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print("A monster has you! Game Over Man!")
        break




