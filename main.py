from os.path import basename, splitext
import tkinter as tk

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

        self.scale_R = tk.Scale(self, from_=0 , to=255, orient=tk.HORIZONTAL,
            background="red",length=self.length,width=self.width, command=self.update_bg)
        self.scale_R.pack()

        self.scale_G = tk.Scale(self, from_=0 , to=255, orient=tk.HORIZONTAL,
            background="green",length=self.length,width=self.width, command=self.update_bg)
        self.scale_G.pack()

        self.scale_B = tk.Scale(self, from_=0 , to=255, orient=tk.HORIZONTAL,
            background="blue",length=self.length,width=self.width, command=self.update_bg)
        self.scale_B.pack()

        self.canv = tk.Canvas(self, background="#000000")
        self.canv.pack()

    def update_bg(self, *args):
        self.canv.configure(bg= "#%02x%02x%02x" % (self.scale_R.get(),self.scale_G.get(),self.scale_B.get()))

    def quit(self, event=None):
        super().quit()


app = Application()
app.geometry("500x500")
app.mainloop()
