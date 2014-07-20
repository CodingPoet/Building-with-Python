### Conditional Play

	if score > 1000:
		print("You won a gold trophy!")
	elif score > 800:
		print("You won a silver trophy!")
	else:
		print("Sorry, you didn't win any trophy")


Note:
All conditional statements are made up of combinations of `if`, `elif` and `else`, in that order.

The word `elif` is short for "else if". In plain English, you might say it means "otherwise, if this other test is true...".

The tests `if` and `elif` both need boolean tests attached, to figure out whether the code they house should be run.

The `else` part of a conditional statement houses code which should only be run if none of the other tests work out to a value of true.

Open up the sample file `02-conditionals.py` and see if you can add support for a bronze trophy awarded when your score is over 600 points.

You can change the value of `score` to test your code.

