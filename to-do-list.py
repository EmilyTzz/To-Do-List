from tkinter import *

root = Tk()
monday_tasks = []
x_vars = []
root.title("To-Do List")
root.geometry('450x680') # Length + Height

app_title = Label(root, text = 'To-Do List for The Week:', font = ('Ink Free', 25))
app_title.pack(pady = 20)


def monday_clicked():
    global return_button, add_task, type_task
    monday.pack_forget()
    tuesday.pack_forget()
    wednesday.pack_forget()
    thursday.pack_forget()
    friday.pack_forget()
    saturday.pack_forget()
    sunday.pack_forget()
    return_button = Button(root, text = 'X')
    return_button.config(font= ('Ink Free', 15), bg = 'Red', command = return_menu)
    return_button.place(x=0, y=0)
    app_title.config(text='Things to do for Monday: ')
    type_task = Entry(root, width = 20, font = ('Ink Free', 25))
    type_task.place(relx = 0.5, rely = 0.9, anchor = 'center')
    add_task = Button(root, text = 'Add', width = 15, command = add_in_monday)
    add_task.config(bg = '#f0efa8' )
    add_task.place(relx = 0.5, rely = 0.953, anchor='center')
    for task in monday_tasks:
        task.pack()
    
def add_in_monday():
    checkbox_var = IntVar() # creates a variable that stores an integer
    task = Checkbutton(root, text = type_task.get(),
                       variable = checkbox_var,
                       onvalue = 1,
                       offvalue = 0,
                       command = lambda: delete_checkbox(task, checkbox_var))
    task.config(font=('Ink Free', 30), anchor = 'w')
    monday_tasks.append(task)
    x_vars.append(checkbox_var)
    task.pack()
    type_task.delete(0, END)


def delete_checkbox(checkbox, var):
    if var.get() == 1:
        checkbox.destroy()
        for checkbox in monday_tasks:
            monday_tasks.remove(checkbox)

def return_menu():
    global returned
    app_title.config(text='To-Do List for The Week: ')
    return_button.place_forget()
    type_task.place_forget()
    add_task.place_forget()
    monday.pack()
    tuesday.pack()
    wednesday.pack()
    thursday.pack()
    friday.pack()
    saturday.pack()
    sunday.pack()
    for task in reversed(monday_tasks):
        task.pack_forget()


monday = Button(root, text = 'Monday')
monday.config(font = ('Ink Free', 25), width = 12, bg = '#e67e7e', command = monday_clicked)

tuesday = Button(root, text = 'Tuesday')
tuesday.config(font = ('Ink Free', 25), width = 12, bg = '#e8b690')

wednesday = Button(root, text = 'Wedesday')
wednesday.config(font = ('Ink Free', 25), width = 12, bg = '#f0efa8')

thursday = Button(root, text = 'Thursday')
thursday.config(font = ('Ink Free', 25), width = 12, bg = '#b0e09b')

friday = Button(root, text = 'Friday')
friday.config(font = ('Ink Free', 25), width = 12, bg = '#ade8ed')

saturday = Button(root, text = 'Saturday')
saturday.config(font = ('Ink Free', 25), width = 12, bg = '#a59deb')

sunday = Button(root, text = 'Sunday')
sunday.config(font = ('Ink Free', 25), width = 12, bg = '#e6bee4')

monday.pack()
tuesday.pack()
wednesday.pack()
thursday.pack()
friday.pack()
saturday.pack()
sunday.pack()

root.mainloop()