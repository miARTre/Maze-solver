from tkinter import Tk, BOTH, Canvas

class Window: 
        def __init__(self, width, height):

            self.__root = Tk()
            self.__root.title("My Tkinter Window")
            self.__canvas = Canvas(self.__root, width=width, height=height)
            self.__canvas.pack()
            self.__running = False
            self.__root.protocol("WM_DELETE_WINDOW", self.close)
            

