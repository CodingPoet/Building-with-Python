---
title: algorithm-example
section: calculator
layout: slide
class: default-slide

notes: |
  :)

---

## Example of a Calculation Algorithm

If you're having trouble writing an algorithm, try this:

	# count total number of letters
	totalLetters = len(firstPerson) + len(secondPerson)

	# count number of letters that are the same
	matches = 0;

	for letter in firstPerson:
	    if letter in secondPerson:
	        matches += 1

	for letter in secondPerson: 
	    if letter in firstPerson:
        	matches += 1