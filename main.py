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
        self.var_G = tk.StringVar()
        self.var_B = tk.StringVar()

        self.varColor = tk.StringVar()

        self.saved_data = self.get_save_data()

        if self.saved_data:
            self.varColor.set(self.saved_data)
        

        #TODO make component out of each entry/scale block
        self.var_R.set(0)
        self.var_R.trace("w",lambda *args, **kwargs : self.entry_update(col="R"))
        self.entry_R = tk.Entry(self, textvariable=self.var_R, width=200)
        self.entry_R.pack()

        self.scale_R = tk.Scale(self, from_=0 , to=255, orient=tk.HORIZONTAL,
            background="red",length=self.length,width=self.width, command=self.update_bg)
        self.scale_R.pack()

        self.var_G.set(0)
        self.var_G.trace("w",lambda *args, **kwargs : self.entry_update(col="G"))
        self.entry_G = tk.Entry(self, textvariable=self.var_G, width=200)
        self.entry_G.pack()

        self.scale_G = tk.Scale(self, from_=0 , to=255, orient=tk.HORIZONTAL,
            background="green",length=self.length,width=self.width, command=self.update_bg)
        self.scale_G.pack()

        self.var_B.set(0)
        self.var_B.trace("w",lambda *args, **kwargs : self.entry_update(col="B"))
        self.entry_B = tk.Entry(self, textvariable=self.var_B, width=200)
        self.entry_B.pack()

        self.scale_B = tk.Scale(self, from_=0 , to=255, orient=tk.HORIZONTAL,
            background="blue",length=self.length,width=self.width, command=self.update_bg)
        self.scale_B.pack()

        self.canv = tk.Canvas(self, background="#000000")
        self.canv.pack()

        if self.saved_data:
            self.update_scales_and_canvas()

        self.entryColor = tk.Entry(textvariable = self.varColor, width=200)
        self.entryColor.pack()

    def update_bg(self, *args):
        self.canv.configure(bg= "#%02x%02x%02x" % (self.scale_R.get(),self.scale_G.get(),self.scale_B.get()))
        self.var_R.set(self.scale_R.get())
        self.var_G.set(self.scale_G.get())
        self.var_B.set(self.scale_B.get())

        self.varColor.set(self.canv["background"])

    def entry_update(self, col, *args,**kwargs):
        if col == "R":
            r = self.var_R.get()
            if r.isdigit():
                self.scale_R.set(r)
            else:
                pass
        elif col == "G":
            g = self.var_G.get()
            if g.isdigit():
                self.scale_G.set(g)
            else:
                pass
        else:
            b = self.var_B.get()
            if b.isdigit():
                self.scale_B.set(b)
            else:
                pass

    def get_save_data(self):
        with open("last_color.txt", "r") as data:
            return data.read()

    def update_scales_and_canvas(self):
        data = self.saved_data.lstrip("#")
        r,g,b = tuple(int(data[i:i+2],16) for i in (0,2,4))
        self.scale_R.set(r)
        self.scale_G.set(g)
        self.scale_B.set(b)
        self.update_bg()

    def quit(self, event=None):
        with open("last_color.txt","w") as save:
            save.write(self.varColor.get())
        self.destroy()


app = Application()
app.protocol("WM_DELETE_WINDOW", app.quit)
app.geometry("500x600")
app.mainloop()
