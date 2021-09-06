import turtle
import tkinter as tk
from settings import *

class App:
    def __init__(self, master) -> None:
        self.master = master
        self.master.title("Epidemic Simulator")
        
        self.canvas = tk.Canvas(master)
        self.canvas.config(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.canvas.pack(side=tk.LEFT)
        
        self.turtle_screen = turtle.TurtleScreen(self.canvas)
        self.turtle_screen.bgcolor('black')
        self.turtle_screen.screensize(TURTLE_WIDTH, TURTLE_HEIGHT)
        
        self.turtle = turtle.RawTurtle(self.turtle_screen, shape="turtle")
        self.turtle.color("green")
 
    
if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    

