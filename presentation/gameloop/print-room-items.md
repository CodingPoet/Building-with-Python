### Print Room Items

    # list the door options
    for door in room.doors:
        print ("[" + door.button + "] " + door.name)
        
    # list the item options
    for item in room.items:
        print ("[" + item.button + "] " + item.name)

Note:
Hiding a key is one thing, but we need to tell our player that the key exists in the room too.

We'll do this by adding any items in the room to the list of options we're already printing.

This means that every time you enter a room, your options will be a list of doors and items for you to choose from.

In our `askWhatToDo` method, add another loop which prints the room's items the same way it prints the room's doors.

You can copy the code for the doors and modify it to print items instead.

Run your game and find the key to check that it works.