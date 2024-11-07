"""Develop a to-do list application where users can add, remove, and view tasks.
Use functions to handle each of these actions."""

# Make it a GUI (tkinter)
#   Screen (vertical rectangle)
#       Light green background color

#   I need to be able to add a task
#       Add task button (Add task button)

#           Text box

# When I click on add task, cursor should automatically go to next text box

# I need to be able to remove the task
#       Remove task button (X button)

import tkinter as tk

# Define the global task_list to hold tasks
task_list = []

def window():
    # SCREEN
    screen = tk.Tk()
    screen.geometry("400x450")
    screen.configure(background="#a4f5b7")
    screen.title("To-Do List")

    return screen

# def scrolling(screen):
#     # SCROLL BAR
#     scroll = tk.Scrollbar(screen,
#                           activebackground="#f0f0f0",
#                           cursor="double_arrow",
#                           orient="vertical",
#                           command=screen.yview,
#                           width=10)
#
#     # Link the scrollbar to the canvas' vertical scrolling
#     screen.configure(yscrollcommand=scroll.set)
#
#     # Pack the scrollbar within the frame
#
#     #screen.pack(side="left", fill="both", expand=True)
#
#     scroll.pack(side="right", fill="y")
#
#     scroll.pack()
#
#     return scroll

def remove(task, task_list, remove_button):
    # Destroy the task and its corresponding remove button
    task.destroy()
    remove_button.destroy()
    task_list.remove(task)  # Remove from the task list

def open_text(screen):  # I put screen to because a surface is needed.
    # TEXT BOX
    task = tk.Text(screen,
                   bg="#f0f0f0",
                   fg="black",
                   highlightbackground="black",
                   highlightcolor="black",
                   bd=2,
                   width=15,
                   height=2,
                   cursor="xterm",
                   insertbackground="black",
                   font=("Comic Sans MS", 13, "italic"))

    task.pack(padx=10, pady=5)

    # REMOVE BUTTON
    remove_button = tk.Button(screen,
                              text="X",
                              fg="blue",
                              highlightbackground="red",
                              highlightcolor="red",
                              bd=0,
                              cursor="box_spiral",
                              width=1,
                              height=1,
                              font=("Comic Sans MS", 15),
                              command=lambda: remove(task, task_list, remove_button))

    remove_button.pack(pady=5)

    task_list.append(task)  # Add the task to the task list

    return task

def add_buttons(screen):
    # ADD BUTTONS
    add_button = tk.Button(screen,
                           text="Add task",
                           bd=3,
                           fg="black",
                           highlightbackground="black",
                           highlightcolor="black",
                           width=10,
                           height=2,
                           cursor="circle",
                           command=lambda: open_text(screen))

    add_button.pack(pady=5)

    return add_button


def running():
    screen = window()
    add_buttons(screen)
    screen.mainloop()


running()
