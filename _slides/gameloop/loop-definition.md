---
title: loop-definition
section: gameloop
layout: slide
class: default-slide

notes: |
  So let's take  everything we've added so far and move it to a new function called `enterRoom`.

  Don't forget to create a function parameter called `roomName` so we know which room to enter!

  Also make sure to use the generic `roomName` in place of our old hard-coded `"Alleyway"`.

---


### Loop Definition

    def enterRoom(self, roomName):
        
        room = self.rooms[roomName]
        print(room.name)
        print(room.description)
        
        # print out the options
        print("Options:")
            
        # list the door options
        for door in room.doors:
            print ("[" + door.button + "] " + door.name)
            
        # ask the user to make a choice
        print("")
        buttonPressed = input("What next? ")