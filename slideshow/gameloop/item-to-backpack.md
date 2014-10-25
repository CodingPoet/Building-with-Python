### Item to Backpack

    # act based on the door or item selected
    if chosenDoor != None:
        self.enterRoom(chosenDoor.leadsTo)     
    elif chosenItem != None:
        self.takeItem(chosenItem, room)
        self.askWhatToDo(room)

Note:
Instead of plain old `self.enterRoom()` we need something a little more complicated now.
