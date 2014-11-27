---
title: item-to-backpack
section: gameloop
layout: slide
class: default-slide

notes: |
  Instead of plain old `self.enterRoom()` we need something a little more complicated now.

  
---


### Item to Backpack

    # act based on the door or item selected
    if chosenDoor != None:
        self.enterRoom(chosenDoor.leadsTo)     
    elif chosenItem != None:
        self.takeItem(chosenItem, room)
        self.askWhatToDo(room)

