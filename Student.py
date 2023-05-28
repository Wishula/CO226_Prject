from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image

class student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1000x500+200+100")
        self.root.title("Student Management System")
        self.root.resizable(False, False)
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()