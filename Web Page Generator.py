import tkinter as tk
from tkinter import *
from tkinter import ttk
import webbrowser


win = Tk()

#Set the geometry
win.geometry("700x250")

# Define a function to return the Input data
def get_data():
   label.config(text= entry.get(), font= ('Helvetica 13'))

#Create an Entry Widget
entry = Entry(win, width= 42)
entry.place(relx= .5, rely= .5, anchor= CENTER)

#Inititalize a Label widget
label= Label(win, text="", font=('Helvetica 13'))
label.pack()

#Create a Button to get the input data
ttk.Button(win, text= "use custom or default", command= get_data).place(relx= .7, rely= .5, anchor= CENTER)



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(padx=(10,10) , pady=(10,10))
        self.btn = Button(self.master, text="Submit text", width=30, height=2, command=self.SubmitButton)
        self.btn.grid(padx=(10,10) , pady=(10,10))
        
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")


    def SubmitButton(self):
        tkLabel.showinfo("choose font")

    
        




        
        

        
        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
