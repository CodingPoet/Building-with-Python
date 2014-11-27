---
title: tip-function-length
section: gameloop
layout: slide
class: default-slide

notes: |
  While we're here, let's take a closer look at our `enterRoom` function.

  When functions are longer than about 10 lines, it pays to look closely at them and see if the code might be doing more than the function name describes. 

  Is there some functionality we can group and split off into another function with a sensible name?

  At the moment, this function:

  - Prints the name and description of the room
  - Prints out all the door options for the room
  - Prompts the user to make a choice

---


### Pro Tip: Function length

    # enter a specific room
    def enterRoom(self, roomName):
    
        room = self.rooms[roomName]
        
        # describe the room
        print("")
        print(room.name)
        print(room.description)
        print("")
        
        if room.name == "Tool Shed":
            self.end()
        else:
            self.askWhatToDo(room)

