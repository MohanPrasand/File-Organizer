from fileorganizer import FileOrganizer
from tkinter import *
from tkinter import messagebox
import os
os.chdir("c:/")
class Organizer:
    fileorganizerObj=FileOrganizer()
    root=None
    height=500
    width=800
    buttonHeight=30
    buttonWidth=70
    def __init__(self):
        self.root=Tk()
        self.root.title("File Organizer UI")
        self.root.geometry(f"{self.width}x{self.height}")
        self.fileLabel=Label(self.root,text="Folder Path:",font=("Roberto",10))
        self.fileLabel.place(x=10,y=5,height=self.buttonHeight,width=self.buttonWidth)
        self.fileInput=Entry(self.root)
        self.fileInput.insert(0,"c:\\")
        self.fileInput.place(x=5,y=30,height=self.buttonHeight,width=500)
        self.prevBtn=Button(self.root,text="<-",command=self.prevfolder)
        self.prevBtn.place(x=508,y=30,width=20,height=self.buttonHeight)
        self.fetchBtn=Button(self.root,text="Fetch",command=self.fetch)
        self.fetchBtn.place(x=545,y=30,height=self.buttonHeight,width=self.buttonWidth)
        self.organizeBtn=Button(self.root,text="Organize",command=self.organizer)
        self.organizeBtn.place(x=620,y=30,height=self.buttonHeight,width=self.buttonWidth)
        self.deorganizeBtn=Button(self.root,text="Deorganize",command=self.deorganizer)
        self.deorganizeBtn.place(x=700,y=30,height=self.buttonHeight,width=self.buttonWidth)
        self.frame=Canvas(self.root,background="gray")
        self.frame.place(x=5,y=70,width=self.width-10,height=self.height-70)
        self.fetch()
    def organizer(self):
        try:
            p=os.path.abspath(self.fileInput.get())
            self.fileorganizerObj.organize(p)
        except Exception as e:
            messagebox.showerror("Error",e)
        self.fetch()
    def deorganizer(self):
        try:
            p=os.path.abspath(self.fileInput.get())
            self.fileorganizerObj.deorganize(p)
        except Exception as e:
            messagebox.showerror("Error",e)
        self.fetch()
    def fetch(self):
        for i in self.frame.winfo_children():
            i.destroy()
        path=os.path.abspath(self.fileInput.get())
        if not os.path.exists(path):
            messagebox.showinfo("Incorrect","Path does not exists")
            return
        h=5
        l=5
        try:
            for i in os.listdir(path):
                if os.path.isdir(f"{path}\{i}"):
                    b=Button(self.frame,text=i,bg="white",font=("Roberto",10),justify="right",command=lambda m=i:self.addpath(m))
                else:
                    b=Label(self.frame,text=i,bg="yellow",font=("Roberto",10))
                b.place(x=l,y=h,height=self.buttonHeight,width=self.buttonWidth+50)
                l+=self.buttonWidth+40
                if l>=self.width-100:
                    l=5
                    h+=self.buttonHeight
                
            os.chdir(path)
        except:
            self.addpath(os.curdir)
            messagebox.showwarning("Permissin Denied","Permission denied to access this folder")
            
    def prevfolder(self):
        os.chdir("..")
        self.fileInput.delete(0,END)
        self.fileInput.insert(0,os.path.abspath(os.curdir))
        self.fetch()
    def addpath(self,p):
        self.fileInput.delete(0,END)
        self.fileInput.insert(0,os.path.abspath(p))
        self.fetch()
        
Organizer().root.mainloop()
        
