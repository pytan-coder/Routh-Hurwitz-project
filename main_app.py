from Tkinter import *
from routh_class_4 import Routh

root = Tk()
root.title("Routh-Hurwitz Stability Calculator")
root.geometry("300x300")

app = Frame(root)
app.grid()

G_string = ''
H_string = ''

def G_function(entry_box):
    global G_string
    G_string = G_entry.get()
    print G_string
    do_matrix(G_string)

def H_function(entry_box):
    global H_string
    H_string = H_entry.get()
    print H_string
    do_matrix(H_string)

def do_matrix(entry_str):
    string = Routh(entry_str)
    string.update_matrix()
    new = string.get_matrix()
    for idx, item in enumerate(new):
        res_box.insert(END, idx)
        res_box.insert(END, ' ')
    
        res_box.insert(END, item)
        res_box.insert(END, '\n')

# input widgets
G_label = Label(app, text = "G(s)")
G_label.grid(column = 0, row = 0, padx = 5, pady = 5)

G_entry = Entry(app, width = 20)
G_entry.grid(column = 1, row = 0, padx = 5, pady = 5)
G_entry.bind('<Return>', G_function)

H_label = Label(app, text = "H(s)")
H_label.grid(column = 0, row = 1, padx = 5, pady = 5)

H_entry = Entry(app, width = 20)
H_entry.grid(column = 1, row = 1, padx = 5, pady = 5)
H_entry.bind('<Return>', H_function)

results = Label(app, text = "Matrix")
results.grid(column = 0, row = 3, padx = 5, pady = 5)

res_box = Text(app, width = 30, height = 6)
res_box.grid(column = 0, row = 5, padx = 5, pady = 5,
             rowspan = 4, columnspan = 2,  sticky = 'N')

##assess = Button(app, text = "Assess", command = do_matrix, width=button_width)
##assess.grid(column = 0, row = 0, padx = 2, pady = 2)

mainloop()

