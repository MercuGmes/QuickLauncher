import tkinter as tk
from tkinter import filedialog, messagebox
import os
import json

CONFIG_FILE = "quicklauncher_config.json"

class QuickLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("QuickLauncher")
        self.root.geometry("500x400")
        self.root.configure(bg="#2c3e50")
        
        tk.Label(root, text="QuickLauncher", font=("Arial", 16, "bold"), fg="white", bg="#2c3e50").pack(pady=10)
        
        self.buttons_frame = tk.Frame(root, bg="#2c3e50")
        self.buttons_frame.pack(pady=10)
        
        self.listbox = tk.Listbox(self.buttons_frame, width=50, height=10, font=("Arial", 12), bg="#34495e", fg="white", selectbackground="#1abc9c")
        self.listbox.pack(side=tk.LEFT)
        
        self.scrollbar = tk.Scrollbar(self.buttons_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        
        self.add_button = tk.Button(root, text="➕ Agregar Acceso", font=("Arial", 12), bg="#27ae60", fg="white", command=self.add_shortcut)
        self.add_button.pack(pady=5, ipadx=10, ipady=5)
        
        self.remove_button = tk.Button(root, text="❌ Eliminar Acceso", font=("Arial", 12), bg="#c0392b", fg="white", command=self.remove_shortcut)
        self.remove_button.pack(pady=5, ipadx=10, ipady=5)
        
        self.open_button = tk.Button(root, text="▶️ Abrir", font=("Arial", 12), bg="#2980b9", fg="white", command=self.open_selected)
        self.open_button.pack(pady=5, ipadx=20, ipady=5)
        
        self.shortcuts = []
        self.load_shortcuts()
    
    def add_shortcut(self):
        filepath = filedialog.askopenfilename(title="Selecciona un archivo o programa")
        if filepath:
            self.shortcuts.append(filepath)
            self.listbox.insert(tk.END, os.path.basename(filepath))
            self.save_shortcuts()
    
    def remove_shortcut(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            del self.shortcuts[index]
            self.listbox.delete(index)
            self.save_shortcuts()
    
    def open_selected(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            os.startfile(self.shortcuts[index])
    
    def save_shortcuts(self):
        with open(CONFIG_FILE, "w") as file:
            json.dump(self.shortcuts, file)
    
    def load_shortcuts(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as file:
                self.shortcuts = json.load(file)
                for shortcut in self.shortcuts:
                    self.listbox.insert(tk.END, os.path.basename(shortcut))

if __name__ == "__main__":
    root = tk.Tk()
    app = QuickLauncher(root)
    root.mainloop()
