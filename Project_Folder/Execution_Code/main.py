from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
from tkinter import messagebox
from tkinter.ttk import Combobox
import pymysql.connections
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user = "root",
    passwd = "",
    port = "3306",
    database = "test2"

)
if db.is_connected():
    print("Success")

class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Devices")
        self.root.geometry("1200x500+100+50")
        self.root.resizable(False, False)
        self.bg = ImageTk.PhotoImage(file="images/devices.jpg")
        self.bg_image = Label(self.root,bg="snow").place(x=0, y=0, relheight=1, relwidth=1)
        Next_Frame = Frame(self.root,bg="snow")
        Next_Frame.place(x=340, y=90, height=380, width=500)
        title = Label(Next_Frame,text="Press Next To View Devices", bg="snow", font=("Impact", 25, "bold")).place(x=60, y=23)
        next_but = Button(Next_Frame,cursor="hand2", text="Next", bg="#d25d17", fg="white",
                            font=("times new roman", 16),command=self.next_but ).place(x=220.0, y=120)
        title = Label(Next_Frame, text="View Configurations", bg="snow", font=("Impact", 25, "bold")).place(x=110,
                                                                                                                   y=200)
        next_but = Button(Next_Frame, cursor="hand2", text="Configurations", bg="#d25d17", fg="white",
                          font=("times new roman", 16), command=self.view_configs).place(x=180.0, y=280)

    def next_but(self):
        """self.root.title("Devices")
        self.root.geometry("1200x500+100+50")
        self.root.resizable(False, False)
        """
        Next_Frame = Frame(self.root, bg="snow")
        Next_Frame.place(x=0, y=0, relheight=1200, relwidth=500)

        Label1 = Label(Next_Frame,text="Device 1 ", bg="snow", font=("Impact", 25, "bold")).place(x=60, y=23)
        self.bg = ImageTk.PhotoImage(file="images/device1.jpg")
        self.bg1=Button(Next_Frame,image=self.bg,cursor="hand2",command=self.dev1).place(x=55,y=80,height=100,width=140)
        Label2 = Label(Next_Frame, text="Device 2 ", bg="snow", font=("Impact", 25, "bold")).place(x=480.0, y=23)
        self.bg2 = ImageTk.PhotoImage(file="images/device2.jpg")
        self.bg22 = Button(Next_Frame, image=self.bg2, cursor="hand2",command=self.dev2 ).place(x=480.0, y=80, height=85, width=140)
        Label3 = Label(Next_Frame, text="Device 3 ", bg="snow", font=("Impact", 25, "bold")).place(x=880.0, y=23)
        self.bg3 = ImageTk.PhotoImage(file="images/device3.jpg")
        self.bg33 = Button(Next_Frame, image=self.bg3, cursor="hand2",command=self.dev3 ).place(x=880.0, y=80, height=85, width=140)
        Label4 = Label(Next_Frame, text="Device 4 ", bg="snow", font=("Impact", 25, "bold")).place(x=280.0, y=260)
        self.bg4 = ImageTk.PhotoImage(file="images/device4.jpg")
        self.bg44 = Button(Next_Frame, image=self.bg4, cursor="hand2",command=self.dev4 ).place(x=280.0, y=315, height=85, width=140)
        Label5 = Label(Next_Frame, text="Device 5 ", bg="snow", font=("Impact", 25, "bold")).place(x=710.0, y=260)
        self.bg5 = ImageTk.PhotoImage(file="images/device5.jpg")
        self.bg55 = Button(Next_Frame, image=self.bg5, cursor="hand2",command=self.dev5 ).place(x=710.0, y=315, height=85, width=140)
        Back = Button(Next_Frame,command=self.back, cursor="hand2", text="Back", bg="#d25d17", fg="white",
                          font=("times new roman", 16),).place(x=570.0, y=420)
        self.valuesall = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")


    def view_configs(self):
        Next_Frame = Frame(self.root, bg="snow")
        Next_Frame.place(x=0, y=0, relheight=1200, relwidth=500)
        Label1 = Label(Next_Frame, text="Device 1 ", bg="snow", font=("Impact", 25, "bold")).place(x=60, y=23)
        self.bg = ImageTk.PhotoImage(file="images/device1.jpg")
        self.bg1 = Button(Next_Frame, image=self.bg, cursor="hand2", command=self.view_dev1).place(x=55, y=80, height=100,
                                                                                              width=140)
        Label2 = Label(Next_Frame, text="Device 2 ", bg="snow", font=("Impact", 25, "bold")).place(x=480.0, y=23)
        self.bg2 = ImageTk.PhotoImage(file="images/device2.jpg")
        self.bg22 = Button(Next_Frame, image=self.bg2, cursor="hand2", command=self.view_dev2).place(x=480.0, y=80,
                                                                                                height=85, width=140)
        Label3 = Label(Next_Frame, text="Device 3 ", bg="snow", font=("Impact", 25, "bold")).place(x=880.0, y=23)
        self.bg3 = ImageTk.PhotoImage(file="images/device3.jpg")
        self.bg33 = Button(Next_Frame, image=self.bg3, cursor="hand2", command=self.view_dev3).place(x=880.0, y=80,
                                                                                                height=85, width=140)
        Label4 = Label(Next_Frame, text="Device 4 ", bg="snow", font=("Impact", 25, "bold")).place(x=280.0, y=260)
        self.bg4 = ImageTk.PhotoImage(file="images/device4.jpg")
        self.bg44 = Button(Next_Frame, image=self.bg4, cursor="hand2", command=self.view_dev4).place(x=280.0, y=315,
                                                                                                height=85, width=140)
        Label5 = Label(Next_Frame, text="Device 5 ", bg="snow", font=("Impact", 25, "bold")).place(x=710.0, y=260)
        self.bg5 = ImageTk.PhotoImage(file="images/device5.jpg")
        self.bg55 = Button(Next_Frame, image=self.bg5, cursor="hand2", command=self.view_dev5).place(x=710.0, y=315,
                                                                                                height=85, width=140)
        Back = Button(Next_Frame, command=self.back, cursor="hand2", text="Back", bg="#d25d17", fg="white",
                      font=("times new roman", 16), ).place(x=570.0, y=420)


    def view_dev1(self):
        self.view_device("device1")

    def view_dev2(self):
        self.view_device("device2")

    def view_dev3(self):
        self.view_device("device3")

    def view_dev4(self):
        self.view_device("device4")
    def view_dev5(self):
        self.view_device("device5")

    def view_device(self,name):

        self.Next_Frame = Frame(self.root, bg="snow")
        self.Next_Frame.place(x=0, y=0, relheight=1200, relwidth=500)
        Label1 = Label(self.Next_Frame, text="Viewing The Configurations For "+str.upper(name), bg="snow",
                       font=("Impact", 25, "bold")).place(x=330, y=23)
        self.fetch_dev_details(name)
        Label1 = Label(self.Next_Frame, text = str.upper(name),bg="snow",
                       font=("Impact", 20, "bold")).place(x=20, y=100)
        self.bg = ImageTk.PhotoImage(file="images/"+name+".jpg")
        self.bg1 = Label(self.Next_Frame, image=self.bg, cursor="hand2").place(x=20, y=170,height=100,width=140)
        Label1 = Label(self.Next_Frame, text="Memory AR     ", bg="snow",font=("Times New Roman", 15,)).place(x=180, y=100)
        Label1 = Label(self.Next_Frame, text="Memory DR     ", bg="snow", font=("Times New Roman", 15,)).place(x=380, y=100)
        Label1 = Label(self.Next_Frame, text="Index Register", bg="snow", font=("Times New Roman", 15,)).place(x=580, y=100)
        Label1 = Label(self.Next_Frame, text="Accumulator   ", bg="snow", font=("Times New Roman", 15,)).place(x=780, y=100)
        Label1 = Label(self.Next_Frame, text="Time-Stamp   ", bg="snow", font=("Times New Roman", 15,)).place(x=980,y=100)
        x=220
        y=150.00
        for row in self.record:
            for i in range(1,6):
                Label1 = Label(self.Next_Frame, text=row[i], bg="snow",font=("Times New Roman", 15,)).place(x=x,y=y)
                x = x+190
            y = y+40
            x = 220
        Back = Button(self.Next_Frame, command=self.view_configs, cursor="hand2", text="Back", bg="#d25d17", fg="white",
                      font=("times new roman", 16), ).place(x=570.0, y=420)

    def fetch_dev_details(self,name):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                port="3306",
                database="test2")
            mycursor = mydb.cursor()

            sql = "Select * from config_table where device_name = %s"
            dname = (name,)
            mycursor.execute(sql,dname,"order by time_Stamp desc")

            #mycursor.execute("select * from config_table where device_name = '%s'",(name))
            #print(name)
            self.record = mycursor.fetchall()
            mydb.commit()
            if self.record == None:
                messagebox.showerror("Error", "No Configurations Found", parent=self.root)
            else:
                #print("Success")

                mydb.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error Due to : {str(ex)}", parent=self.root)

    def back(self):
        Login(root)

    def dev1(self):
        devname = "device1"
        self.Next_Frame = Frame(self.root, bg="snow")
        self.Next_Frame.place(x=0, y=0, relheight=1200, relwidth=500)
        Label1 = Label(self.Next_Frame, text="Set The Configurations For Device 1 ", bg="snow", font=("Impact", 25, "bold")).place(x=330, y=23)
        self.Configs(devname)

    def dev2(self):
        devname = "device2"
        self.Next_Frame = Frame(self.root, bg="snow")
        self.Next_Frame.place(x=0, y=0, relheight=1200, relwidth=500)
        Label1 = Label(self.Next_Frame, text="Set The Configurations For Device 2 ", bg="snow",
                       font=("Impact", 25, "bold")).place(x=330, y=23)
        self.Configs(devname)

    def dev3(self):
        devname = "device3"
        self.Next_Frame = Frame(self.root, bg="snow")
        self.Next_Frame.place(x=0, y=0, relheight=1200, relwidth=500)
        Label1 = Label(self.Next_Frame, text="Set The Configurations For Device 3 ", bg="snow",
                       font=("Impact", 25, "bold")).place(x=330, y=23)
        self.Configs(devname)

    def dev4(self):
        devname = "device4"
        self.Next_Frame = Frame(self.root, bg="snow")
        self.Next_Frame.place(x=0, y=0, relheight=1200, relwidth=500)
        Label1 = Label(self.Next_Frame, text="Set The Configurations For Device 4 ", bg="snow",
                       font=("Impact", 25, "bold")).place(x=330, y=23)
        self.Configs(devname)

    def dev5(self):
        devname = "device5"
        self.Next_Frame = Frame(self.root, bg="snow")
        self.Next_Frame.place(x=0, y=0, relheight=1200, relwidth=500)
        Label1 = Label(self.Next_Frame, text="Set The Configurations For Device 5 ", bg="snow",
                       font=("Impact", 25, "bold")).place(x=330, y=23)
        self.Configs(devname)

    def Configs(self,name):

        n = StringVar()
        MAR=Label(self.Next_Frame,text="Memory Address Register",bg="snow", font=("Impact", 20, "bold")).place(x=130, y=100)
        self.marlist=ttk.Combobox(self.Next_Frame,width=10,textvariable=n)
        self.marlist['values']=self.valuesall
        self.marlist['state']='readonly'
        self.marlist.place(x=500,y=110.0)
        self.marlist.current(0)
        n = StringVar()
        MDR = Label(self.Next_Frame, text="Memory Data Register", bg="snow", font=("Impact", 20, "bold")).place(x=130, y=250)
        self.mdrlist = ttk.Combobox(self.Next_Frame, width=10, textvariable=n)
        self.mdrlist['values'] = self.valuesall
        self.mdrlist['state'] = 'readonly'
        self.mdrlist.place(x=500, y=260.0)
        self.mdrlist.current(0)
        n = StringVar()
        IR = Label(self.Next_Frame, text="Index Register", bg="snow", font=("Impact", 20, "bold")).place(x=750, y=100)
        self.irlist = ttk.Combobox(self.Next_Frame, width=10, textvariable=n)
        self.irlist['values'] = self.valuesall
        self.irlist['state'] = 'readonly'
        self.irlist.place(x=950, y=110.0)
        self.irlist.current(0)
        n = StringVar()
        AC = Label(self.Next_Frame, text="Accumulator", bg="snow", font=("Impact", 20, "bold")).place(x=750,y=250)
        self.aclist = ttk.Combobox(self.Next_Frame, width=10, textvariable=n)
        self.aclist['values'] = self.valuesall
        self.aclist['state'] = 'readonly'
        self.aclist.place(x=950, y=260.0)
        self.aclist.current(0)

        submit_button = Button(self.Next_Frame,command=self.submit, cursor="hand2", text="Submit", bg="#d25d17", fg="white",
                          font=("times new roman", 16),).place(x=530.0, y=420)
        Back = Button(self.Next_Frame, command=self.next_but, cursor="hand2", text="Back", bg="#d25d17", fg="white",
                      font=("times new roman", 16), ).place(x=680.0, y=420)
        self.devname = name

    def submit(self):
        if (self.marlist.get() == "" or self.mdrlist.get() == "" or self.irlist.get() == "" or self.aclist.get() == "" ):
            messagebox.showerror("Error","Fields Cannot Be Null")
        else:
            try:
                marval = int(self.marlist.get())
                mdrval = int(self.mdrlist.get())
                irval = int(self.irlist.get())
                acval = int(self.aclist.get())
                #print(self.devname)
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    port="3306",
                    database="test2")
                mycursor = mydb.cursor()
                mycursor.execute("insert into config_table (device_name,mar,mdr,ir,ac) values (%s,%s,%s,%s,%s)",
                                 (self.devname,
                                 marval,
                                 mdrval,
                                 irval,
                                 acval,
                                 )
                                 )
                mydb.commit()
                messagebox.showinfo("Success","Entry Successful")
                #print(marval)
                #print(mdrval)
                #print(irval)
                #print(acval)
            except Exception as ex:
                messagebox.showerror("Error", f"Error Due to : {str(ex)}", parent=self.root)
print("bye")
root = Tk()
obj = Login(root)
root.mainloop()