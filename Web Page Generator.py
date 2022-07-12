import tkinter as tk
from tkinter import *
from tkinter import ttk
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.L1 = Label(self.master, text="Enter custom text or click default page button")
        self.L1.grid(column=0, row=0,padx=(10,10) , pady=(10,10), stick=W) 
        self.E1 = Entry(self.master, width=100)
        self.E1.grid(column=0, row=1, padx=(10,10) , pady=(10,10))
        self.btn = Button(self.master, text="Default HTML Page", width=25, height=2, command=self.defaultHTML)
        self.btn.grid(column=0, row=2, padx=(10,10) , pady=(10,10), sticky=NS)
        self.btn = Button(self.master, text="Submit text", width=25, height=2, command=self.newHTML)
        self.btn.grid(column=0, row=2, padx=(10,10) , pady=(10,10), sticky=E)
        
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        


    def newHTML(self):
        htmlText = self.E1.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
    
        




        
        

        
        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
