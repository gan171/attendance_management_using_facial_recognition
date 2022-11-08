from tkinter import * 
from PIL import Image,ImageTk
from tkinter import ttk
from login import Login
from viewatt import viewatt

class decide:
    def __init__(self,root):
        self.root=root
        self.root.title("Student login")
        self.root.geometry("1366x768+0+0")
        img=Image.open(r"C:\Users\91970\Desktop\facerec33\Python_Test_Projects\Images_GUI\pexels-the-happiest-face-)-866351.jpg")
        img=img.resize((1366,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"C:\Users\91970\Desktop\facerec33\Python_Test_Projects\Images_GUI\pexels-the-happiest-face-)-866351.jpg")
        bg1=bg1.resize((1366,768),Image.Resampling.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)

        std_img_btn=Image.open(r"C:\Users\91970\Documents\Python_Test_Projects\Images_GUI\std1.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)
        std_b1 = Button(bg_img,command=self.view,image=self.std_img1,cursor="hand2")
        std_b1.place(x=350,y=100,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.root,text="View Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=350,y=280,width=180,height=45)


        std_img_btn=Image.open(r"C:\Users\91970\Documents\Python_Test_Projects\Images_GUI\log.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.std_img2=ImageTk.PhotoImage(std_img_btn)
        std_b2 = Button(bg_img,command=self.login,image=self.std_img2,cursor="hand2")
        std_b2.place(x=650,y=100,width=180,height=180)

        std_b1_2 = Button(bg_img,command=self.login,text="Admin Login",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_2.place(x=650,y=280,width=180,height=45)
    
    def login(self):
        self.new_window=Toplevel(self.root)
        self.app=Login(self.new_window)
    def view(self):
        self.new_window=Toplevel(self.root)
        self.app=viewatt(self.new_window)








if __name__ == "__main__":
    root= Tk()
    app=decide(root)
    root.mainloop()

