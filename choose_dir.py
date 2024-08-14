import tkinter as tk
from tkinter import filedialog
import os
# import ipywidgets as widgets
# from ipywidgets import Layout, Box


def tkinter_dir_select():
    folder_path = None
    
    def select_folder():
        nonlocal folder_path
        folder_path = filedialog.askdirectory()
        if folder_path:
            print("選擇的資料夾路徑為:", folder_path)
            root.destroy()  # 關閉視窗
        else:
            print("未選擇任何資料夾。")
    
    # 建立主視窗
    root = tk.Tk()
    root.title("選擇資料夾")

    # 建立選擇按鈕
    select_button = tk.Button(root, text="選擇資料夾", command=select_folder)
    select_button.pack(padx=20, pady=20)

    # 開始GUI主迴圈
    root.mainloop()
    return folder_path

def input_for_dir_path():
    return input('Please input the directory path: ')

class ChooseDir:
    def __init__(self) -> None:
        self.dir_funcs = {"Current directory": os.getcwd, 
             "Input path": input_for_dir_path, 
             "Seclect on computer": tkinter_dir_select}
        self.dir_options = [name for name in self.dir_funcs.keys()]
        self.dir_drop = widgets.Dropdown(options=self.dir_options, description='Dir options:')
    
    def show_dir(self):
        self.dirpath = self.dir_funcs[self.dir_drop.value]()
        return self.dirpath