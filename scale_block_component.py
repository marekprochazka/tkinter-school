
from tkinter import Frame, Entry, Scale, HORIZONTAL

class BaseScaleBlock(Frame):
    def __init__(self, variable,bg_update_fun,length,width,color, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.entry_callback_command = (self.register(self.entry_callback))

        self.variable = variable
        self.bg_fun = bg_update_fun
        self.length = length
        self.width = width
        self.color = color

        self.variable.set(0)
        self.variable.trace("w",lambda *args, **kwargs : self.entry_update())
        self.entry = Entry(self, validate='all', validatecommand=(self.entry_callback_command, '%P'),  textvariable=self.variable, width=200)
        self.entry.pack()

        self.scale = Scale(self, from_=0 , to=255, orient=HORIZONTAL,
            background=self.color,length=self.length,width=self.width, command=self.bg_fun)
        self.scale.pack()


    def entry_update(self, *args,**kwargs):
        value = self.variable.get()
        if value.isdigit():
                self.scale.set(value)
        else:
            pass
        
    def entry_callback(self,value):
        if value == "":
            return True
        if value.isdigit():
            if int(value) <= 255:
                return True
        return False