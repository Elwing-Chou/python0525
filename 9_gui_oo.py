import tkinter as tk

class MyFrame(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.e1 = tk.Entry(self)
        self.e1.pack()
        self.b1 = tk.Button(self, text="轉換", command=self.click)
        self.b1.pack()
        self.l1 = tk.Label(self, text="按上面做轉換")
        self.l1.pack()

    def click(self):
        score = float(self.e1.get())
        score = score ** 0.5 * 10
        self.l1["text"] = str(score)

window = tk.Tk()
f1 = MyFrame(window)
f1.pack(side=tk.LEFT)
f2 = MyFrame(window)
f2.pack(side=tk.LEFT)
window.mainloop()