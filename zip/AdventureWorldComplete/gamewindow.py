from tkinter import *

class GameWindow(object):

    def __init__(self, game, room):    
        self.window = Tk()
        self.window.title('Adventure World')
        
        self.game = game
        self.room = room
        self.create_background()
        self.create_text()
        self.create_buttons()
        
        self.window.mainloop()
        
        
    def create_background(self):
        self.background_image = PhotoImage(file = 'images/smiley.gif')
        self.pic = Label(self.window, image = self.background_image)
        self.pic.pack()
        
    
    def create_text(self):
        description_text = Label(self.window, text = self.room.description)
        description_text.pack()
        
        
    def create_buttons(self):
        for door in self.room.doors:
            button = Button(
                self.window,
                text=door.name,
                command=lambda: self.game.openDoor(door, self.room)
            )
            button.pack()
        
    
