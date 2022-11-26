import tkinter as tk


class App():
    def __init__(self) -> None:
        self.window=tk.Tk()

        self.window.resizable(False,False)
        self.window.title('Discretization algorithms')
        self.window.geometry("400x300+10+10")

        #lines 
        self.lines_title=tk.Label(self.window,text="Draw lines")
        self.lines_title.pack(ipadx=50, ipady=50)

        #circles
        self.circle_title=tk.Label(self.window,text="Draw circles")
        self.circle_title.pack(ipadx=50, ipady=50)

        self.window.mainloop()


