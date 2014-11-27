---
title: victory-condition
section: gameloop
layout: slide
class: default-slide

notes: |
  So our game loop is working fantastically, we can navigate through the rooms pretty much forever... but where's the fun in that?

  It's time to add a way to win our game.

  The way it's set up currently is so that if you manage to find your way into the tool shed, you win. Let's implement that.

  When we enter a room, we want to print the description of the room, and then IF the room we are in is the tool shed, end the game.

---

### Victory Condition

