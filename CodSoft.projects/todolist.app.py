import json
import os
import tkinter as tk
from tkinter import messagebox, font
class ToDoList :
    def __init__(self):
        self.a = ''
        self.list1 = []
        self.jsonlist = []

    def getelement(self):
        n = int(input('Enter Number of elements: '))
        for i in range(n):
            self.a = input()
            self.list1.append(self.a)

    def jsonconversion(self):

        if os.path.exists('list1.json'):
            with open('list1.json', 'r') as file:
                old_data = json.load(file)
        else:
            old_data = []


        old_data.extend(self.list1)


        with open('list1.json', 'w') as f:
            json.dump(old_data, f)

        self.jsonlist = old_data

    def displayelement(self):
        for idx, ele in enumerate(self.jsonlist, 1):
            print(f'{idx}.',ele)

    def removeelement(self):
        q = int(input('Enter index of the Task you want to remove: '))
        if 1 <= q <= len(self.jsonlist):
            self.jsonlist.pop(q-1)
            print('Task Removed!!\nNew List :')
            for idx, ele in enumerate(self.jsonlist, 1) :
                print(f'{idx}.', ele)
        else :
            print('Enter a valid index!')
        with open('list1.json', 'w') as f:
            json.dump(self.jsonlist, f)




class ToDoListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("450x500")
        self.root.configure(bg="#f0f4f7")

        self.task_input = tk.StringVar()
        self.task_list = []
        self.custom_font = font.Font(family="Helvetica", size=12)

        self.load_tasks()

        tk.Label(root, text="Add a Task", font=("Helvetica", 14, "bold"), bg="#f0f4f7").pack(pady=10)

        input_frame = tk.Frame(root, bg="#f0f4f7")
        input_frame.pack()

        self.entry = tk.Entry(input_frame, textvariable=self.task_input, font=self.custom_font, width=28)
        self.entry.pack(side=tk.LEFT, padx=5)

        self.add_btn = tk.Button(input_frame, text="Add", bg="#4CAF50", fg="white", width=10, command=self.add_task)
        self.add_btn.pack(side=tk.LEFT)

        # Task list area with scroll
        self.canvas = tk.Canvas(root, bg="#f0f4f7", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.task_frame = tk.Frame(self.canvas, bg="#f0f4f7")

        self.task_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.task_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=10, pady=10)
        self.scrollbar.pack(fill=tk.Y, side=tk.RIGHT)

        self.clear_btn = tk.Button(root, text="Clear Completed", bg="#f44336", fg="white", command=self.clear_completed)
        self.clear_btn.pack(pady=10)

        self.display_tasks()

    def load_tasks(self):
        if os.path.exists("list1.json"):
            try:
                with open("list1.json", "r") as file:
                    data = json.load(file)
                    # Support both old (str) and new (dict) formats
                    self.task_list = [{"text": t, "done": False} if isinstance(t, str) else t for t in data]
            except json.JSONDecodeError:
                self.task_list = []
        else:
            self.task_list = []

    def save_tasks(self):
        with open("list1.json", "w") as file:
            json.dump(self.task_list, file)

    def add_task(self):
        text = self.task_input.get().strip()
        if text:
            self.task_list.append({"text": text, "done": False})
            self.task_input.set("")
            self.save_tasks()
            self.display_tasks()
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")

    def toggle_task(self, idx):
        self.task_list[idx]["done"] = not self.task_list[idx]["done"]
        self.save_tasks()
        self.display_tasks()

    def clear_completed(self):
        self.task_list = [task for task in self.task_list if not task["done"]]
        self.save_tasks()
        self.display_tasks()

    def display_tasks(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for idx, task in enumerate(self.task_list):
            task_text = task["text"]
            is_done = task.get("done", False)

            frame = tk.Frame(self.task_frame, bg="#f0f4f7")
            frame.pack(fill=tk.X, pady=2, padx=5)

            chk_var = tk.BooleanVar(value=is_done)
            chk = tk.Checkbutton(frame, variable=chk_var, command=lambda i=idx: self.toggle_task(i), bg="#f0f4f7")
            chk.pack(side=tk.LEFT)

            label_font = self.custom_font.copy()
            label_font.configure(overstrike=int(is_done))

            label_color = "#888" if is_done else "black"

            label = tk.Label(frame, text=task_text, font=label_font, fg=label_color, bg="#f0f4f7", anchor="w")
            label.pack(side=tk.LEFT, fill=tk.X, expand=True)




if __name__ == "__main__":
    mode = input("Enter mode (console/gui): ").strip().lower()

    if mode == "console":
        obj = ToDoList()
        obj.getelement()
        obj.jsonconversion()
        obj.displayelement()
        obj.removeelement()
    elif mode == "gui":
        root = tk.Tk()
        app = ToDoListGUI(root)
        root.mainloop()
    else:
        print("Invalid mode. Use 'console' or 'gui'")