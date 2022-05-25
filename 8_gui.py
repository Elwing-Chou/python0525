import tkinter as tk

def click():
    score = float(e1.get())
    score = score ** 0.5 * 10
    l1["text"] = str(score)

window = tk.Tk()
# 元件 = 創造元件(老爸)
# 元件.pack()
# 請一定先創造框框(Frame)
f1 = tk.Frame(window)
f1.pack()
e1 = tk.Entry(f1)
e1.pack()
b1 = tk.Button(f1, text="轉換", command=click)
b1.pack()
l1 = tk.Label(f1, text="按上面做轉換")
l1.pack()
window.mainloop()