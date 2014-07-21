### Enable Door Locking

In door.py:

    def __init__(self, button, name, leadsTo, requiredItem = None):
        self.button = button
        self.name = name
        self.leadsTo = leadsTo
        self.requiredItem = requiredItem

Note:
And lock the door of the tool shed.

Update the door class so that we can say it has a required item.

Add a requiredItem property, and allow us to pass the value.

Provide a default of None so we don't have to set a requiredItem for every door.