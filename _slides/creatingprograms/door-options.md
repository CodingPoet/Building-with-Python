---
title: door-options
section: creatingprograms
layout: slide
class: default-slide

notes: |
  So the player is in the Alleyway, now we need to give them some options.

  We need to list all of the available doors.

  We'll add the code to show the door options immediately after the room decription.

  First we'll print out a heading which says "Options", and then use a loop to print out each of the doors along with the key to press to go through them.

  Run your program :) Happy? Onwards!

---

### Door options

    # print out the options
    print("Options:")
        
    # list the door options
    for door in room.doors:
        print ("[" + door.button + "] " + door.name)


