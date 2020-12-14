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

        self.var_R = tk.StringVar()
        self.var_R.set(0)
        self.var_R.trace("w", self.entry_update)
        self.entry_R = tk.Entry(self, textvariable=self.var_R, width=200)
        self.entry_R.pack()

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

        self.varColor = tk.StringVar()
        self.entryColor = tk.Entry(textvariable = self.varColor, width=200)
        self.entryColor.pack()

    def update_bg(self, *args):
        self.canv.configure(bg= "#%02x%02x%02x" % (self.scale_R.get(),self.scale_G.get(),self.scale_B.get()))
        self.var_R.set(self.scale_R.get())
        self.varColor.set(self.canv["background"])

    def entry_update(self, *args,**kwargs):
        r = self.var_R.get()
        if r.isdigit():
            self.scale_R.set(r)
        else:
            pass

    def quit(self, event=None):
        super().quit()


app = Application()
app.geometry("500x600")
app.mainloop()
