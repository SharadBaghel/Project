from textwrap import fill
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")

        # =================variables=====================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

# 2 image
        img1 = Image.open(r"college_images\smart-attendance.jpg")
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lb1 = Label(self.root, image=self.photoimg1)
        f_lb1.place(x=0, y=0, width=800, height=200)

        # 3 image
        img2 = Image.open(r"college_images\students.jpg")
        img2 = img2.resize((800, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb1 = Label(self.root, image=self.photoimg2)
        f_lb1.place(x=800, y=0, width=800, height=200)

    # 4 bgimage
        img3 = Image.open(r"college_images\bg13.png")
        img3 = img3.resize((1600, 900), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1600, height=900)

        title_lb1 = Label(bg_img, text="Attendance Management System", font=("times new romen", 35, "bold"), bg="white",
                          fg="dark green")
        title_lb1.place(x=0, y=0, width=1600, height=50)

        main_Frame = Frame(bg_img, bd=2, bg="white")
        main_Frame.place(x=10, y=55, width=1570, height=675)

        # left label Frame
        Left_frame = LabelFrame(main_Frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=770, height=650)

        img_left = Image.open(
            r"college_images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((760, 150), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lb1 = Label(Left_frame, image=self.photoimg_left)
        f_lb1.place(x=5, y=0, width=760, height=130)

        left_inside_frame = Frame(Left_frame, bd=2,relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=135, width=720, height=370)

        # label and entry
        # atttendance id
        attendanceId = Label(left_inside_frame, text="Attendance ID :", font=("times new roman", 13, "bold"),
                              bg="white")
        attendanceId.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceID = ttk.Entry(left_inside_frame, width=20,
                                  textvariable=self.var_atten_id,font=("times new roman", 13, "bold"))
        attendanceID.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        #name
        rollLabel1 = Label(left_inside_frame, text="Roll:", font=("times new roman", 13, "bold"),
                              bg="white")
        rollLabel1.grid(row=0, column=2, padx=4, pady=8,)

        atten_roll = ttk.Entry(left_inside_frame, width=20,
                                  textvariable=self.var_atten_name,font=("times new roman", 13, "bold"))
        atten_roll.grid(row=0, column=3,pady=8,)

        #date
        namelabel = Label(left_inside_frame, text="Name:", font=("times new roman", 13, "bold"),
                              bg="white")
        namelabel.grid(row=1, column=0,)

        atten_name = ttk.Entry(left_inside_frame, width=20,
                                  textvariable=self.var_atten_name,font=("times new roman", 13, "bold"))
        atten_name.grid(row=1, column=1,pady=8,)

        # Department

        deplabel = Label(left_inside_frame, text="Department:", font=("times new roman", 13, "bold"),
                              bg="white")
        deplabel.grid(row=1, column=2,)

        atten_dep = ttk.Entry(left_inside_frame, width=20,
                                  textvariable=self.var_atten_dep,font=("times new roman", 13, "bold"))
        atten_dep.grid(row=1, column=3,pady=8,)

        #time

        timelabel = Label(left_inside_frame, text="Time:", font=("times new roman", 13, "bold"),
                              bg="white")
        timelabel.grid(row=2, column=0,)

        atten_time = ttk.Entry(left_inside_frame, width=20,
                                  textvariable=self.var_atten_time,font=("times new roman", 13, "bold"))
        atten_time.grid(row=2, column=1,pady=8,)

        # Date

        datelabel = Label(left_inside_frame, text="Date:", font=("times new roman", 13, "bold"),
                              bg="white")
        datelabel.grid(row=2, column=2,)

        atten_date = ttk.Entry(left_inside_frame, width=20,
                                  textvariable=self.var_atten_date,font=("times new roman", 13, "bold"))
        atten_date.grid(row=2, column=3,pady=8,)

        ##attendance

        attendancelabel = Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 13, "bold"),
                              bg="white")
        attendancelabel.grid(row=3, column=0,)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

         # Buttons Frame
        btn_Frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_Frame.place(x=0, y=300, width=754, height=35)

        btn_save = Button(btn_Frame, text="Import csv",command=self.importCsv,width=18, font=("times new roman", 13, "bold"),
                          bg="blue", fg="white", bd=4)
        btn_save.grid(row=0, column=0)

        btn_update = Button(btn_Frame, text="Export csv",command=self.exportCsv,width=18,
                            font=("times new roman", 13, "bold"), bg="blue", fg="white", bd=4)
        btn_update.grid(row=0, column=1)

        btn_delete = Button(btn_Frame, text="Update", width=18,
                            font=("times new roman", 13, "bold"), bg="blue", fg="white", bd=4)
        btn_delete.grid(row=0, column=2)

        btn_reset = Button(btn_Frame, text="Reset",command=self.reset_data,width=18,
                           font=("times new roman", 13, "bold"), bg="blue", fg="white", bd=4)
        btn_reset.grid(row=0, column=3)

        

        # right label Frame
        Right_frame = LabelFrame(main_Frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=790, y=10, width=720, height=650)

        table_Frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_Frame.place(x=5, y=5, width=700, height=445)

        #+++++++++++++++scroll bar table+++++++++++++++++++++++

        scroll_x=ttk.Scrollbar(table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_Frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_Frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #==============fetch data==============

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)


    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("ALl File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv     
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("ALl File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                     exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows= content ['values']
        self.var_atten_id.set( rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set( "")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")







        





if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()

    def new_method(self):
        return ("ALl File","*.*")