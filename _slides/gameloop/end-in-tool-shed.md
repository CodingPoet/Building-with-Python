---
title: end-in-tool-shed
section: gameloop
layout: slide
class: default-slide

notes: |
  In our `enterRoom` function, immediately after we output the information about the current room, we need to check which room we are in.

  If the current room is the tool shed, we can call the `end` function which has already been set up.

  Run your game and see if the game ends correctly when you enter the tool shed.

---


### End in tool shed

    if room.name == "Tool Shed":
        self.end()

