---
title: user-input
section: creatingprograms
layout: slide
class: default-slide

notes: |
  Phew! Now we can ask the user where they would like to go next!

  Under the door list, add in a user input prompt.

  Run your program to check that everything is working as expected.

  So we are asking for the user to make a choice, and we are storing that choice in the `buttonPressed` variable, but then what?

  We would need to repeat the same code as we had for our alleyway - print out the name of the room, the description, and the options. That's a lot of repeated code, and what about all the other rooms we might enter?

  It's finally time to take a look at implementing a game loop.

---


### User input

    # ask the user to make a choice
    print("")
    buttonPressed = input("What next? ")
