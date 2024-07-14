from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_recognition
import os
from attendance import Attendance 

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")

        # First Image
        img = Image.open(r"college_images\Stanford.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=500, height=130)

        # 2 image
        img1 = Image.open(r"college_images\Stanford.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lb1 = Label(self.root, image=self.photoimg1)
        f_lb1.place(x=550, y=0, width=500, height=130)

        # 3 image
        img2 = Image.open(r"college_images\Stanford.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb1 = Label(self.root, image=self.photoimg2)
        f_lb1.place(x=1100, y=0, width=500, height=130)

        # 4 bgimage
        img3 = Image.open(r"college_images\bg11.jpg")
        img3 = img3.resize((1600, 900), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1600, height=900)

        title_lb1 = Label(bg_img, text="Face Recognition System", font=("times new romen", 35, "bold"), bg="white",
                          fg="red")
        title_lb1.place(x=0, y=0, width=1600, height=50)

        # student button
        img4 = Image.open(r"college_images\face_detector1.jpg")
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, heigh=220)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2",
                      font=("times new romen", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=200, y=320, width=220, heigh=40)

        # Detect face button

        img5 = Image.open(r"college_images\face_detector1.jpg")
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b2 = Button(bg_img, image=self.photoimg4, cursor="hand2",command=self.face_data)
        b2.place(x=500, y=100, width=220, heigh=220)

        b2_1 = Button(bg_img, text="Face Recognition ", cursor="hand2",command=self.face_data, font=("times new romen", 15, "bold"),
                      bg="darkblue", fg="white")
        b2_1.place(x=500, y=320, width=220, heigh=40)

        # Attendace button

        img6 = Image.open(r"college_images\face_detector1.jpg")
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b3 = Button (bg_img, image=self.photoimg6, cursor="hand2",command=self.attendance_data)
        b3.place(x=800, y=100, width=220, heigh=220)

        b3_1 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_data, font=("times new romen", 15, "bold"),
                      bg="darkblue", fg="white")
        b3_1.place(x=800, y=320, width=220, height=40)

        # help button

        img8 = Image.open(r"college_images\face_detector1.jpg")
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b5 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.attendance_data)
        b5.place(x=1100, y=100, width=220, heigh=220)

        b5_1 = Button(bg_img, text="Help", cursor="hand2", font=("times new romen", 15, "bold"),
                      bg="darkblue", fg="white")
        b5_1.place(x=1100, y=320, width=220, heigh=40)

        # train faces data

        img9 = Image.open(r"college_images\face_detector1.jpg")
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.train_data)
        b6.place(x=200, y=400, width=220, heigh=220)

        b6_1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data ,font=("times new romen", 15, "bold"),
                      bg="darkblue", fg="white")
        b6_1.place(x=200, y=620, width=220, heigh=40)

        # photos faces

        img10 = Image.open(r"college_images\face_detector1.jpg")
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b7 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.open_images)
        b7.place(x=500, y=400, width=220, heigh=220)

        b7_1 = Button(bg_img, text="Photo Data", cursor="hand2", font=("times new romen", 15, "bold"),
                      bg="darkblue", fg="white", command=self.open_images)
        b7_1.place(x=500, y=620, width=220, heigh=40)

        # developer faces

        img11 = Image.open(r"college_images\face_detector1.jpg")
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b8 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        b8.place(x=800, y=400, width=220, heigh=220)

        b8_1 = Button(bg_img, text="Photo Data", cursor="hand2", font=("times new romen", 15, "bold"),
                      bg="darkblue", fg="white")
        b8_1.place(x=800, y=620, width=220, heigh=40)

        # exit faces button

        img12 = Image.open(r"college_images\face_detector1.jpg")
        self.photoimg12 = ImageTk.PhotoImage(img12)
        b9 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b9.place(x=1100, y=400, width=220, heigh=220)

        b9_1 = Button(bg_img, text="Photo Data", cursor="hand2", font=("times new romen", 15, "bold"),
                      bg="darkblue", fg="white")
        b9_1.place(x=1100, y=620, width=220, heigh=40)

    def open_images(self):
        os.startfile("data")

    # ----------------------------------------------------Functions Buttons------------------------------------------------------------

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)


    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)







if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
