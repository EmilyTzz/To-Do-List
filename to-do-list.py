from tkinter import *

root = Tk()
monday_tasks = []
x_vars = []
root.title("To-Do List")
root.geometry('450x680') # Length + Height

app_title = Label(root, text = 'To-Do List for The Week:', font = ('Ink Free', 25))
app_title.pack(pady = 20)


def monday_clicked():
    global return_button, add_task, type_task, monday_task, delete_task
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

    add_task = Button(root, text = 'Add', width = 15, command = add_task_monday)
    add_task.config(bg = '#f0efa8' )
    add_task.place(relx = 0.35, rely = 0.953, anchor='center')

    delete_task = Button(root, text = 'Delete', width = 15, command = delete_task_monday)
    delete_task.config(bg = 'Red')
    delete_task.place(relx = 0.65, rely = 0.953, anchor='center')

    monday_task = Listbox(root,
                          bg="White",
                          font = ('Constantia',30),
                          width = 20,
                          selectmode = MULTIPLE)
    monday_task.pack()
    monday_task.config(height = monday_task.size()) 

    for monday_task in monday_tasks:
        monday_task.pack()
    
def add_task_monday():
    task = type_task.get().strip()
    if task:
        monday_tasks.append(monday_task)
        monday_task.insert(END, task)
        type_task.delete(0, END)


def delete_task_monday():
    for task in reversed(monday_task.curselection()):
        monday_task.delete(task)
        del monday_tasks[task]
   

def return_menu():
    global returned
    app_title.config(text='To-Do List for The Week: ')
    return_button.place_forget()
    type_task.place_forget()
    add_task.place_forget()
    delete_task.place_forget()
    monday.pack()
    tuesday.pack()
    wednesday.pack()
    thursday.pack()
    friday.pack()
    saturday.pack()
    sunday.pack()
    monday_task.pack_forget()



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