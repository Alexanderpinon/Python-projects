import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import schedule
import time

class ParentWindow(Frame):
    #Creates button to select files from source directory
    self.sourceDir_btn = Button(text="Select Source", width=20)
    #Positions source button in GUI using tkinter grid()
    self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

    #creates entry for source directory selection
    self.source_dir = Entry(width=75)
    #postions entry in GUI using tkinter grid() padx and pady are the same as
    #the button to ensure they will line up
    self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30,0))

    self.destDir_btn = Button(text="Select Destination", width=20, command=self.sourceDir)
    self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))
    self.destination_dir = Entry(width=75)
    self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15,10))
                                            
    def _init_(self, master):
        Frame._init_(self)
        self.master.title("File Transfer")
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        self.transfer_btn.grid(row=2, column=1, padx=(200,0), pady=(0, 15))
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        self.exit_btn.grid(row=20, column=2, padx=(10, 40), pady=(0, 15))
                           

    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        self.source_dir.delete(0, END)
        self.source_dir.insert(0, selectSourceDir)


    def transferFiles(self):
        source = self.source_dir.get()
        destination = self.destination_dir.get()
        source_files = os.listdir(source)
        for i in source_files:
            shutil.move(source + '/' + i, destination)
            print(i + ' was successfully transferred.')
        schedule.every(24).hour.do(transferFiles)
            
    def exit_program(self):
        root.destroy()
                     


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
