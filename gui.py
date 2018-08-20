import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")
        
        #Botão direita
        self.right = tk.Button(self)
        self.right["text"] = "Direita\n"
        self.right["command"] = self.say_right
        self.right.pack(side="right")
        
        #Botão esquerda
        self.left = tk.Button (self)
        self.left["text"] = "Esquerda\n"
        self.left["command"] = self.say_left
        self.left.pack(side="left")
        
        #Botão baixo
        self.down = tk.Button (self)
        self.down["text"] = "Baixo\n"
        self.down["command"] = self.say_down
        self.down.pack(side="bottom")
        
        #Botão cima
        self.up = tk.Button (self)
        self.up["text"] = "Cima\n"
        self.up["command"] = self.say_up
        self.up.pack(side="top")

    # def say_hi(self):
        # print("hi there, everyone!")
        
    def say_right(self):
        print ("Direita!")
        
    def say_up(self):
        print ("Para cima!")
        
    def say_down(self):
        print ("Para baixo!")
        
    def say_left(self):
        print ("Esquerda!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
