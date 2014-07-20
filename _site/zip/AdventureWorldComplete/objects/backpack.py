class Backpack(object):

	# set up the backpack object
    def __init__(self):
    		# use an array to store all the backpack items
            self.items = []


    # get an item from the backpack by name
    def getItem(self, wantedItemName):
        
        # Set the item to 'None' to start with.
        # This assumes we don't have it.
        wantedItem = None
        
        # Look for the item in the items array.
        # If we find it, store it in the wantedItem variable
        for item in self.items:
            if item.name == wantedItemName:
                wantedItem = item
        
        # Return the wantedItem.
        # If we don't have the item, the value will be 'None'
        # If we do have the item, the value will be an Item object
        return wantedItem
        
    