import os
import tkinter as tk
from tkinter import filedialog
from sglm import utils, glm_fit

def create_project():
    project_name = project_name_entry.get()
    project_dir = project_dir_entry.get()
    utils.create_new_project(project_name, project_dir)

# Set tkinter params
root = tk.Tk()
root.title("Simple GLM GUI")
root.geometry("750x270")


# Create an entry box for Project Name
project_name_entry = tk.Entry(root)
project_name_entry.pack()
project_name_title = tk.Label(root, text="Choose a project name")
project_name_title.pack()

# Create an entry box for Project Directory
project_dir_entry = tk.Entry(root)
project_dir_entry.pack()
project_dir_title = tk.Label(root, text="Choose a project directory")
project_dir_title.pack()

project_name = project_name_entry.get()
project_dir = project_dir_entry.get()

#Create button
create_project_button = tk.Button(root, text="Create a project",command=create_project)
create_project_button.pack()

# Start the tkinter main loop
root.mainloop()