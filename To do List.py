from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

tasks_list = [] 

def main_screen():
    global my_entry
    global lb
    global Entry
    global Listbox
    main = Tk()
    main.title("TO DO LIST")
    main.geometry("800x500")
    main.resizable(False, False)

    # Load the background image using PIL
    background_image = Image.open("bgimage.png")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = Label(main, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame = Frame(main,bg=main.cget("bg"))
    frame.pack()

    # Heading Frame
    heading_main = Label(frame, text="TO DO LIST", font=("Algerian", "50"),bg="#B9CCD0", fg="black", anchor="center")
    heading_main.grid()

    # ListBox Frame
    frame2 = Frame(main)
    frame2.pack(anchor=W, padx=18, pady=15, side=LEFT, after=frame)
    lb = Listbox(frame2, width=29, height=14, bg='#efdecd', font=('Algerian', 18), bd=2, fg='#000000',
                 highlightthickness=1, selectbackground='#666666', activestyle="dotbox")
    lb.pack(side=LEFT)
    # Scrollbar
    ysb = Scrollbar(frame2)
    ysb.pack(side=RIGHT, fill=BOTH)
    lb.config(yscrollcommand=ysb.set)
    ysb.config(command=lb.yview)

    load_tasks()
    for task in tasks_list:
        lb.insert(END, task)

    # Entry Box
    my_entry = Entry(main, font=('Bookmanstyle', 16), width=22)
    my_entry.pack(anchor=W, padx=30, pady=40)
    
    # Create a transparent canvas for buttons
    canvas_for_buttons = Canvas(main, highlightthickness=0,bg=main.cget("bg"))
    canvas_for_buttons.pack(anchor=W, padx=35)

    add_button = Button(canvas_for_buttons, text="ADD", font=("Algerian", "20"), padx=24, bg="RosyBrown2",
                        command=lambda: NewTask(my_entry, lb))
    add_button.pack(side=LEFT)

    delete_button = Button(canvas_for_buttons, text="DELETE", font=("Algerian", "20"), bg="RosyBrown2",
                           command=lambda: DeleteTask(lb))
    delete_button.pack(side=RIGHT)

    button_frame2 = Frame(main, bg=main.cget("bg")) 
    button_frame2.pack(anchor=W, padx=70,pady=30) 
    save_button = Button(button_frame2, text="SAVE TASKS", font=("Algerian", "20"), bg="RosyBrown2",
                         command=lambda: save_tasks())
    save_button.pack(anchor=S,side=BOTTOM)

    main.mainloop()

def load_tasks():
    global tasks_list
    tasks_list = [] 

    try:
        with open('tasks.txt', 'r') as tasks_list_file:
            tasks_list = [task.strip() for task in tasks_list_file.readlines()]
    except FileNotFoundError:
        pass

def NewTask(entry: Entry, listbox: Listbox):
    task = entry.get()
    if task != "":
        lb.insert(END, task)
        tasks_list.append(task)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter Task First.")

def DeleteTask(listbox: Listbox):
    selected_index = listbox.curselection()
    if selected_index:
        del tasks_list[selected_index[0]]
        listbox.delete(selected_index)
        save_tasks()

def save_tasks():
    with open('tasks.txt', 'w') as tasks_list_file:
        for task in tasks_list:
            tasks_list_file.write(f'{task}\n')

main_screen()
