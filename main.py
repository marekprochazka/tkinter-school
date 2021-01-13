from os.path import basename, splitext
import tkinter as tk
from scale_block_component import BaseScaleBlock

# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "HexScaler"
    length = 400
    width = 50

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)


        self.var_R = tk.StringVar()
        self.var_G = tk.StringVar()
        self.var_B = tk.StringVar()

        self.varColor = tk.StringVar()

        self.saved_data = self.get_save_data()

        if self.saved_data:
            self.varColor.set(self.saved_data)
        

        self.red_block = BaseScaleBlock(variable = self.var_R, bg_update_fun=self.update_bg, length= self.length, width = self.width, color="red")
        self.green_block = BaseScaleBlock(variable = self.var_G, bg_update_fun=self.update_bg, length= self.length, width = self.width, color="green")
        self.blue_block = BaseScaleBlock(variable = self.var_B, bg_update_fun=self.update_bg, length= self.length, width = self.width, color="blue")
        self.red_block.pack()
        self.green_block.pack()
        self.blue_block.pack()
        

        self.canv = tk.Canvas(self, background="#000000")
        self.canv.pack()

        if self.saved_data:
            self.update_scales_and_canvas()

        self.entryColor = tk.Entry(textvariable = self.varColor, width=200)
        self.entryColor.pack()

    def update_bg(self, *args):
        self.canv.configure(bg= "#%02x%02x%02x" % (self.red_block.scale.get(),self.green_block.scale.get(),self.blue_block.scale.get()))
        self.red_block.variable.set(self.red_block.scale.get())
        self.green_block.variable.set(self.green_block.scale.get())
        self.blue_block.variable.set(self.blue_block.scale.get())


        self.varColor.set(self.canv["background"])


    def get_save_data(self):
        with open("last_color.txt", "r") as data:
            return data.read()

    def update_scales_and_canvas(self):
        data = self.saved_data.lstrip("#")
        r,g,b = tuple(int(data[i:i+2],16) for i in (0,2,4))
        self.red_block.variable.set(r)
        self.green_block.variable.set(g)
        self.blue_block.variable.set(b)
        self.update_bg()

    def quit(self, event=None):
        with open("last_color.txt","w") as save:
            save.write(self.varColor.get())
        self.destroy()


app = Application()
app.protocol("WM_DELETE_WINDOW", app.quit)
app.geometry("500x600")
app.mainloop()
