import tkinter as tk
from Train import linear_svm
from to_db import to_db


def picker():
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename

    Tk().withdraw()
    filename = askopenfilename()
    return filename


def predval():
    fn = picker()
    print(fn)
    ls = linear_svm(fn)[0]
    l.insert(tk.END, '{},'.format(ls))
    df = [fn, int(ls)]
    to_db(df)


root = tk.Tk()
# position
w = 600
h = 300
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
# icon
root.configure(background='black')
root.title("SVM")
# text

l = tk.Text(root, bg='white', height=3, width=25)
l.grid(row=19, column=7, padx=150, pady=30)
B = tk.Button(text="Pick Image", command=predval)
B.config(height=2, width=12)
B.grid(row=20, column=7, padx=150, pady=20)
q = tk.Button(text="Quit", command=quit)
q.config(height=2, width=12)
q.grid(row=21, column=7, padx=250)
root.mainloop()
