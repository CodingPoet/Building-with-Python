---
title: loop-identification
section: gameloop
layout: slide
class: default-slide

notes: |
  So we've come across our first instance of having to repeat some pretty serious code.

  If we take a closer look at what we are trying to achieve with our game, we see that there is a good chunk of it in the middle which will actually be repeated for every move the player makes.

  The steps of "describe room", "offer options" and "choose option" occur for every room in the game.

  So, let's identify the code which does those steps, and split it out into its own function where we can reuse it over and over.

---

### Loop Identification

- Set Up Game
- Introduction
- Enter Room
	- Describe Room
	- Offer options
	- Choose option
- End Game
