#backend
import csv
from tkinter import simpledialog
import mysql.connector
from tkinter import *
from tkinter import messagebox
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root=customtkinter.CTk()
root.title("Census Record System")
root.geometry("1000x1200+10+10")
root.config(bg="#bca0dc")

def table1():

    def c1():
        tu = Label(root,text="Enter user : ",bd=2,width=40,height=2,font=(18),bg="#3c1361")
        tu.pack(padx=10,pady=10)
        ent1 = Entry(root,bd=2,width=40,font=(18))
        ent1.pack(padx=10,pady=10)
        tpass = Label(root,text="Enter password : ",bd=2,width=40,height=2,font=(18),bg="#3c1361")
        tpass.pack(padx=10,pady=10)
        ent2 = Entry(root,bd=2,width=40,font=(18),show = "*")
        ent2.pack(padx=10,pady=10)
        tdb = Label(root,text="Database name : ",bd=2,width=40,height=2,font=(18),bg="#3c1361")
        tdb.pack(padx=10,pady=10)
        ent3 = Entry(root,bd=2,width=40,font=(18),)
        ent3.pack(padx=10,pady=10)

        def c1del():
            tu.after(1,tu.destroy)
            tpass.after(1,tpass.destroy)
            tdb.after(1,tdb.destroy)
            ent1.after(1,ent1.destroy)
            ent2.after(1,ent2.destroy)
            ent3.after(1,ent3.destroy)
            btn5.after(1,btn5.destroy)

        def dbsetup():
            global entT1,entT2,entT3
            entT1 = ent1.get()
            entT2 = ent2.get()
            entT3 = ent3.get()

            mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2)
            mycursor = mydb.cursor()
            mycursor.execute("CREATE DATABASE {}".format(entT3))
            mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
            mycursor = mydb.cursor()
            mycursor.execute("create table if not exists census_info(First_Name varchar(64) not null,Last_Name varchar(64) null,Date_Of_Birth date not null,Email_ID varchar(255) not null unique,Aadhar_Number varchar(16) not null primary key,Father_Name varchar(64) not null,Mother_Name varchar(64)  not null,City_And_State varchar(100) not null);")

        btn5 = Button(root,text="Save.",activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32),command=lambda:[table2(),c1del(),dbsetup()])
        btn5.pack(padx=10,pady=10)

    def c2():
        tu = Label(root,text="Enter user : ",bd=2,width=40,height=2,font=(18),bg="#3c1361")
        tu.pack(padx=10,pady=10)
        ent1 = Entry(root,bd=2,width=40,font=(18))
        ent1.pack(padx=10,pady=10)
        tpass = Label(root,text="Enter password : ",bd=2,width=40,height=2,font=(18),bg="#3c1361")
        tpass.pack(padx=10,pady=10)
        ent2 = Entry(root,bd=2,width=40,font=(18),show = "*")
        ent2.pack(padx=10,pady=10)
        tdb = Label(root,text="Database name : ",bd=2,width=40,height=2,font=(18),bg="#3c1361")
        tdb.pack(padx=10,pady=10)
        ent3 = Entry(root,bd=2,width=40,font=(18))
        ent3.pack(padx=10,pady=10)

        def vals():
            global entT1,entT2,entT3
            entT1 = ent1.get()
            entT2 = ent2.get()
            entT3 = ent3.get()

        def c2del():
            tu.after(1,tu.destroy)
            tpass.after(1,tpass.destroy)
            tdb.after(1,tdb.destroy)
            ent1.after(1,ent1.destroy)
            ent2.after(1,ent2.destroy)
            ent3.after(1,ent3.destroy)
            btn4.after(1,btn4.destroy)

        btn4 = Button(root,text="Save.",activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32),command=lambda:[table2(),c2del(),vals()])
        btn4.pack(padx=10,pady=10)

    def btncdel():
        btnc1.after(1,btnc1.destroy)
        btnc2.after(1,btnc2.destroy)

    btnc1 = Button(root,text="Automatic Configuration (An Automatic Configuration from Scratch.)",command = lambda:[c1(),btncdel()],activebackground="#800080",bg = "#7c5295",bd=2,width=60,height=2,font=(18))
    btnc1.pack(pady=10)
    
    btnc2 = Button(root,text="Manual Configuration (For Pre-Made Database Only,You can setup table later on in pre-made database.)",command = lambda:[c2(),btncdel()],activebackground="#800080",bg = "#7c5295",bd=2,width=86,height=2,font=(18))
    btnc2.pack(pady=10)
    

    

def btn1del():
    btn1.after(1,btn1.destroy)

btn1 = Button(root,text="Click me to Start Setup",command = lambda:[table1(),btn1del()],activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32))
btn1.pack(pady=10)

def newwin():
    root=customtkinter.CTk()
    root.title("Test Win.")
    root.geometry("100x200+10+10")
    root.config(bg="#bca0dc")
    root.mainloop()

#setup

def dcensus(): #DELETE A RECORD FROM DATABASE #COMPLETE

    a = 0
    mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
    mycursor = mydb.cursor()
    dchoice = simpledialog.askstring("Delete A Record from Database","Enter Aadhar Number to Delete the Record(XXXX-XXXX-XXXX)")
    if len(dchoice) == 0:
        messagebox.showerror('Error', 'Error: No Aadhar Number provided.')
    else:
        mycursor.execute('SELECT * FROM census_info')
        myresult = mycursor.fetchall()
        for i in myresult:
            if dchoice == i[4]:
                a = a+1
                mycursor.execute("DELETE FROM census_info WHERE Aadhar_Number='{}'".format(dchoice))
                mydb.commit()
                messagebox.showinfo("Successful",  "Deleted record from the Database.")
                break
        if a == 0:
            messagebox.showerror("Error",  "No Entries exists with this Aadhar number in database.")

def lcensus(): #SHOW ALL THE RECORDS IN DATABASE #COMPLETE
    mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM census_info ORDER BY First_Name')
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        messagebox.showerror("Error","No Records to show in database.")
    else:
        def swin():
            mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
            mycursor = mydb.cursor()
            a = 1
            mycursor.execute('SELECT * FROM census_info ORDER BY First_Name')
            myresult = mycursor.fetchall()
            root=customtkinter.CTk()
            root.title("Records in Database.")
            root.geometry("400x600")
            root.config(bg="#D586FF")
            scrollbar = Scrollbar(root)
            scrollbar.pack( side = RIGHT, fill = Y )
            listbox = Listbox(root, yscrollcommand = scrollbar.set,bg="#D586FF",font="32",height = "33")
            listbox.pack(fill = BOTH)
            for i in myresult:
                listbox.insert(END,"Record Number : "+str(a))
                listbox.insert(END,"First Name : "+i[0])
                listbox.insert(END,"Last Name : "+i[1])
                listbox.insert(END,"Date Of Birth : "+str(i[2]))
                listbox.insert(END,"Email ID : "+i[3])
                listbox.insert(END,"Aadhar Number : "+i[4])
                listbox.insert(END,"Father's Name : "+i[5])
                listbox.insert(END,"Mother's Name : "+i[6])
                listbox.insert(END,"City & State : "+i[7])

                listbox.pack()
                scrollbar.config( command = listbox.yview )

                a = a+1
            root.resizable(False,False)
            root.mainloop()
        swin()

def scensus():#SEARCH FOR A RECORD IN DATABASE #COMPLETE
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="census_info")
    mycursor = mydb.cursor()
    a = 0
    schoice = simpledialog.askstring("Search for a record","Enter Aadhar number to search record+")
    mycursor.execute('SELECT * FROM census_info ORDER BY First_Name')
    myresult = mycursor.fetchall()
    for i in myresult:
        if schoice == i[4]:
            a = 1
            b = i
            break
    if a == 1:
        def show():
            root=customtkinter.CTk()
            root.title("Records in Database.")
            root.geometry("400x600")
            root.config(bg="#D586FF")
            scrollbar = Scrollbar(root)
            scrollbar.pack( side = RIGHT, fill = Y )
            listbox = Listbox(root, yscrollcommand = scrollbar.set,bg="#D586FF",font="32",height="33")
            listbox.pack(fill = BOTH)
            listbox.insert(END,"First Name : "+b[0])
            listbox.insert(END,"Last Name : "+b[1])
            listbox.insert(END,"Date Of Birth : "+str(b[2]))
            listbox.insert(END,"Email ID : "+b[3])
            listbox.insert(END,"Aadhar Number : "+b[4])
            listbox.insert(END,"Father's Name : "+b[5])
            listbox.insert(END,"Mother's Name : "+b[6])
            listbox.insert(END,"City & State : "+b[7])

            root.resizable(False,False)
            root.mainloop()
        show()
    else:
        messagebox.showerror("Error","No Records exists with this Aadhar number in database.")

def icensus(): #ADD A RECORD TO THE DATABASE #COMPLETE

            mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
            mycursor = mydb.cursor()
            
            mycursor.execute('SELECT Aadhar_Number,Date_Of_Birth FROM census_info ORDER BY First_Name')
            myresult = mycursor.fetchall()

            def addvals():
                x = []
                First_Name = FNameEnt.get()
                Last_Name = LNameEnt.get()
                Date_Of_Birth = DOBEnt.get()
                Email = EIDEnt.get()
                Aadhar_Number = ANumberEnt.get()
                Father_Name = FatherNameEnt.get()
                Mother_Name = MNameEnt.get()
                City_And_State = CASEnt.get()

                a = 0
                if len(myresult) == 0:
                    y = (First_Name, Last_Name, Date_Of_Birth,Email,Aadhar_Number,Father_Name,Mother_Name,City_And_State)
                    x.append(y)
                else:
                    for i in myresult: 
                        if Aadhar_Number == i[0]:
                            a = a + 1
                            break
                        else:
                            y = (First_Name, Last_Name, Date_Of_Birth,Email,Aadhar_Number,Father_Name,Mother_Name,City_And_State)
                            x.append(y)

                if a == 1:
                    messagebox.showerror("Error","Same Aadhar Number address already exists in database,Try Again.")
                else:
                    sqlform = "INSERT INTO census_info(First_Name,Last_Name,Date_Of_Birth,Email_ID,Aadhar_Number,Father_Name,Mother_Name,City_And_State) VALUES (%s, %s, %s, %s,%s, %s, %s, %s)"
                    mycursor.executemany(sqlform,x)
                    mydb.commit()
                    messagebox.showinfo("Successful","Updated Entries in Database.")

            def addi():
                global FNameEnt,LNameEnt,DOBEnt,EIDEnt,ANumberEnt,FatherNameEnt,MNameEnt,CASEnt
                root=Tk()
                root.title("Records in Database.")
                root.geometry("400x1000")
                root.config(bg="#D586FF")

                
                FName = Label(root,text="Enter your First Name",bd=2,width=40,height=2,font=(18),bg="#3c1361")
                FName.pack(padx=10,pady=10)
                FNameEnt = Entry(root,bd=2,width=40,font=(18))
                FNameEnt.pack(padx=10,pady=10)
                LName = Label(root,text="Enter your Last Name",bd=2,width=40,height=2,font=(18),bg="#3c1361")
                LName.pack(padx=10,pady=10)
                LNameEnt = Entry(root,bd=2,width=40,font=(18))
                LNameEnt.pack(padx=10,pady=10)
                DOB = Label(root,text="Enter your Date Of Birth(YYYY-MM-DD)",bd=2,width=40,height=2,font=(18),bg="#3c1361")
                DOB.pack(padx=10,pady=10)
                DOBEnt = Entry(root,bd=2,width=40,font=(18))
                DOBEnt.pack(padx=10,pady=10)
                EID = Label(root,text="Enter your Email ID",bd=2,width=40,height=2,font=(18),bg="#3c1361")
                EID.pack(padx=10,pady=10)
                EIDEnt = Entry(root,bd=2,width=40,font=(18))
                EIDEnt.pack(padx=10,pady=10)
                ANumber = Label(root,text="Enter your Aadhar Number",bd=2,width=40,height=2,font=(18),bg="#3c1361")
                ANumber.pack(padx=10,pady=10)
                ANumberEnt = Entry(root,bd=2,width=40,font=(18))
                ANumberEnt.pack(padx=10,pady=10)
                FatherName = Label(root,text="Enter your Father's Name",bd=2,width=40,height=2,font=(18),bg="#3c1361")
                FatherName.pack(padx=10,pady=10)
                FatherNameEnt = Entry(root,bd=2,width=40,font=(18))
                FatherNameEnt.pack(padx=10,pady=10)
                MName = Label(root,text="Enter your Mother's Name",bd=2,width=40,height=2,font=(18),bg="#3c1361")
                MName.pack(padx=10,pady=10)
                MNameEnt = Entry(root,bd=2,width=40,font=(18))
                MNameEnt.pack(padx=10,pady=10)
                CAS = Label(root,text="Enter your City and State(City/State)",bd=2,width=40,height=2,font=(18),bg="#3c1361")
                CAS.pack(padx=10,pady=10)
                CASEnt = Entry(root,bd=2,width=40,font=(18))
                CASEnt.pack(padx=10,pady=10)

                BTN = Button(root,text="SAVE",activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32),command = addvals)
                BTN.pack(padx=10,pady=10)

                root.resizable(False,False)
                root.mainloop()

            addi()

def rcensus(file1): #READ A CSV AND APPEND ITS ALL ENTRY TO DATABASE #COMPLETE
    mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
    mycursor = mydb.cursor()
    y=[]
    x = t = d = 0
    mycursor.execute('SELECT Aadhar_Number,Email_ID FROM census_info ORDER BY First_Name')
    myresult = mycursor.fetchall()
    with open(file1, "r") as f:
        reader = csv.reader(f)
        trash = f.readline()
        for j in reader:
            if len(j) == 0:
                a = list(j)
            else:
                y.append(j)
        if len(y) == 0:
            d = d + 1

        if d == 0:
            if len(myresult) > len(y):

                for z in myresult:
                    for f in y:
                        if z[0] == f[4] or z[1] == f[3]:
                            def error1():
                                messagebox.showerror("Error",  "Database already contains data,Remove this entry either from database or from the CSV file.")
                                root=customtkinter.CTk()
                                root.title("Records in Database.")
                                root.geometry("400x600")
                                root.config(bg="#D586FF")
                                scrollbar = Scrollbar(root)
                                scrollbar.pack( side = RIGHT, fill = Y )
                                listbox = Listbox(root, yscrollcommand = scrollbar.set,bg="#D586FF",font="32",height="33")
                                listbox.pack(fill = BOTH)
                                listbox.insert(END,"First Name : "+f[0])
                                listbox.insert(END,"Last Name : "+f[1])
                                listbox.insert(END,"Date Of Birth : "+str(f[2]))
                                listbox.insert(END,"Email ID : "+f[3])
                                listbox.insert(END,"Aadhar Number : "+f[4])
                                listbox.insert(END,"Father's Name : "+f[5])
                                listbox.insert(END,"Mother's Name : "+f[6])
                                listbox.insert(END,"City & State : "+f[7])

                                root.resizable(False,False)
                                root.mainloop()
                            error1()
                            t = t+1
                            break
                        else:
                                x = x+1
            else:
                for f in y:
                    for z in myresult:
                        if z[0] == f[4] or z[1] == f[3]:
                            def error2():
                                messagebox.showerror("Error",  "Database already contains data,Remove this entry either from database or from the CSV file.")
                                root=customtkinter.CTk()
                                root.title("Records in Database.")
                                root.geometry("400x600")
                                root.config(bg="#D586FF")
                                scrollbar = Scrollbar(root)
                                scrollbar.pack( side = RIGHT, fill = Y )
                                listbox = Listbox(root, yscrollcommand = scrollbar.set,bg="#D586FF",font="32",height="33")
                                listbox.pack(fill = BOTH)
                                listbox.insert(END,"First Name : "+f[0])
                                listbox.insert(END,"Last Name : "+f[1])
                                listbox.insert(END,"Date Of Birth : "+str(f[2]))
                                listbox.insert(END,"Email ID : "+f[3])
                                listbox.insert(END,"Aadhar Number : "+f[4])
                                listbox.insert(END,"Father's Name : "+f[5])
                                listbox.insert(END,"Mother's Name : "+f[6])
                                listbox.insert(END,"City & State : "+f[7])

                                root.resizable(False,False)
                                root.mainloop()
                            error2()
                            t = t+1
                            break
                        else:
                                x = x+1
            
            if t == 0:
                sqlform = "INSERT INTO census_info(First_Name,Last_Name,Date_Of_Birth,Email_ID,Aadhar_Number,Father_Name,Mother_Name,City_And_State) VALUES (%s, %s, %s, %s,%s, %s, %s, %s)"
                mycursor.executemany(sqlform,y)
                mydb.commit()
                messagebox.showinfo("Successful","Imported All Data.")

        else:
            messagebox.showerror("Error","No Data Available in CSV file.")

def wcensus(file1): #APPEND ALL THE REC FROM DATABASE TO CSV FILE #COMPLETE
    mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
    mycursor = mydb.cursor()
    j = ["First Name","Last Name","Date Of Birth","Email ID","Aadhar Number","Father's Name","Mother's Name","City & State"]
    mycursor.execute('SELECT * FROM census_info ORDER BY First_Name')
    myresult = mycursor.fetchall()
    with open(file1, "w+") as f:
        if len(myresult) > 0:
            writer = csv.writer(f)
            writer.writerow(j)
            for i in myresult:
                y = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                writer.writerow(y)
            messagebox.showinfo("Successful","Exported All Data to CSV file.")
        else:
            messagebox.showerror("Error","No Records in Database to Export.")

def ucensus(): #UPDATE ANY ENTRY INTO DATABASE #COMPLETE

    root=Tk()
    root.title("Update Records in Database.")
    root.geometry("400x565")
    root.config(bg="#D586FF")

    def fup():
        mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM census_info ORDER BY First_Name')
        root=customtkinter.CTk()
        root.title("Update Complete Record.")
        root.geometry("400x600")
        root.config(bg="#D586FF")
        SAadhar = Label(root, text="Enter Aadhar Number to search for record.",bd=2,width=40,height=2,font=(18),bg="#3c1361")
        SAadhar.pack(padx=10,pady=10)
        SAadharEntry = Entry(root,bd=2,width=40,font=(18))
        SAadharEntry.pack(padx=10,pady=10)
        FName = Label(root,text="Enter your First Name",bd=2,width=40,height=2,font=(18),bg="#3c1361")
        FName.pack(padx=10,pady=10)
        FNameEnt = Entry(root,bd=2,width=40,font=(18))
        FNameEnt.pack(padx=10,pady=10)

        def fvals():
            global ufname,ufsearch
            ufsearch = SAadharEntry.get()
            ufname = FNameEnt.get()

        def execute():
            fvals()
            mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
            mycursor = mydb.cursor()
            mycursor.execute("UPDATE census_info SET First_Name='{}' WHERE Aadhar_Number='{}'".format(ufname,ufsearch))
            mydb.commit()
            root.destroy()
            messagebox.showinfo("Successful","Updated First Name in database.")

        BTN = Button(root,text="SAVE",activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32),command = execute)
        BTN.pack(padx=10,pady=10)

        root.resizable(False,False)
        root.mainloop()

    def lup():
        mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM census_info ORDER BY First_Name')
        root=customtkinter.CTk()
        root.title("Update Complete Record.")
        root.geometry("400x600")
        root.config(bg="#D586FF")
        SAadhar = Label(root, text="Enter Aadhar Number to search for record.",bd=2,width=40,height=2,font=(18),bg="#3c1361")
        SAadhar.pack(padx=10,pady=10)
        SAadharEntry = Entry(root,bd=2,width=40,font=(18))
        SAadharEntry.pack(padx=10,pady=10)
        LName = Label(root,text="Enter your Last Name",bd=2,width=40,height=2,font=(18),bg="#3c1361")
        LName.pack(padx=10,pady=10)
        LNameEnt = Entry(root,bd=2,width=40,font=(18))
        LNameEnt.pack(padx=10,pady=10)

        def lvals():
            global ulname,ufsearch
            ufsearch = SAadharEntry.get()
            ulname = LNameEnt.get()

        def execute():
            lvals()
            mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
            mycursor = mydb.cursor()
            mycursor.execute("UPDATE census_info SET Last_Name='{}' WHERE Aadhar_Number='{}'".format(ulname,ufsearch))
            mydb.commit()
            root.destroy()
            messagebox.showinfo("Successful","Updated Last Name in database.")

        BTN = Button(root,text="SAVE",activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32),command = execute)
        BTN.pack(padx=10,pady=10)

        root.resizable(False,False)
        root.mainloop()

    def dobup():
        mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM census_info ORDER BY First_Name')
        root=customtkinter.CTk()
        root.title("Update Complete Record.")
        root.geometry("400x600")
        root.config(bg="#D586FF")
        SAadhar = Label(root, text="Enter Aadhar Number to search for record.",bd=2,width=40,height=2,font=(18),bg="#3c1361")
        SAadhar.pack(padx=10,pady=10)
        SAadharEntry = Entry(root,bd=2,width=40,font=(18))
        SAadharEntry.pack(padx=10,pady=10)
        DOB = Label(root,text="Enter your Date Of Birth(YYYY-MM-DD)",bd=2,width=40,height=2,font=(18),bg="#3c1361")
        DOB.pack(padx=10,pady=10)
        DOBEnt = Entry(root,bd=2,width=40,font=(18))
        DOBEnt.pack(padx=10,pady=10)
        def dobvals():
            global udob,ufsearch
            ufsearch = SAadharEntry.get()
            udob = DOBEnt.get()

        def execute():
            dobvals()
            mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
            mycursor = mydb.cursor()
            mycursor.execute("UPDATE census_info SET Date_Of_Birth='{}' WHERE Aadhar_Number='{}'".format(udob,ufsearch))
            mydb.commit()
            root.destroy()
            messagebox.showinfo("Successful","Updated Date of Birth in database.")

        BTN = Button(root,text="SAVE",activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32),command = execute)
        BTN.pack(padx=10,pady=10)

        root.resizable(False,False)
        root.mainloop()

    def eidup():
        mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM census_info ORDER BY First_Name')
        root=customtkinter.CTk()
        root.title("Update Complete Record.")
        root.geometry("400x600")
        root.config(bg="#D586FF")
        SAadhar = Label(root, text="Enter Aadhar Number to search for record.",bd=2,width=40,height=2,font=(18),bg="#3c1361")
        SAadhar.pack(padx=10,pady=10)
        SAadharEntry = Entry(root,bd=2,width=40,font=(18))
        SAadharEntry.pack(padx=10,pady=10)
        EID = Label(root,text="Enter your Email ID",bd=2,width=40,height=2,font=(18),bg="#3c1361")
        EID.pack(padx=10,pady=10)
        EIDEnt = Entry(root,bd=2,width=40,font=(18))
        EIDEnt.pack(padx=10,pady=10)
        def eidvals():
            global uemail,ufsearch
            ufsearch = SAadharEntry.get()
            uemail = EIDEnt.get()

        def execute():
            eidvals()
            mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
            mycursor = mydb.cursor()
            mycursor.execute("UPDATE census_info SET Email_ID='{}' WHERE Aadhar_Number='{}'".format(uemail,ufsearch))
            mydb.commit()
            root.destroy()
            messagebox.showinfo("Successful","Updated Email ID in database.")

        BTN = Button(root,text="SAVE",activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32),command = execute)
        BTN.pack(padx=10,pady=10)

        root.resizable(False,False)
        root.mainloop()

    def aadharup():
        mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM census_info ORDER BY First_Name')
        root=customtkinter.CTk()
        root.title("Update Complete Record.")
        root.geometry("400x600")
        root.config(bg="#D586FF")
        SAadhar = Label(root, text="Enter Aadhar Number to search for record.",bd=2,width=40,height=2,font=(18),bg="#3c1361")
        SAadhar.pack(padx=10,pady=10)
        SAadharEntry = Entry(root,bd=2,width=40,font=(18))
        SAadharEntry.pack(padx=10,pady=10)
        ANumber = Label(root,text="Enter your Aadhar Number",bd=2,width=40,height=2,font=(18),bg="#3c1361")
        ANumber.pack(padx=10,pady=10)
        ANumberEnt = Entry(root,bd=2,width=40,font=(18))
        ANumberEnt.pack(padx=10,pady=10)
        def aadharvals():
            global uadhaar,ufsearch
            ufsearch = SAadharEntry.get()
            uadhaar = ANumberEnt.get()

        def execute():
            aadharvals()
            mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
            mycursor = mydb.cursor()
            mycursor.execute("UPDATE census_info SET Aadhar_Number='{}' WHERE Aadhar_Number='{}'".format(uadhaar,ufsearch))
            mydb.commit()
            root.destroy()
            messagebox.showinfo("Successful","Updated Aadhar Number in database.")

        BTN = Button(root,text="SAVE",activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32),command = execute)
        BTN.pack(padx=10,pady=10)

        root.resizable(False,False)
        root.mainloop()

    def fatherup():
        mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM census_info ORDER BY First_Name')
        root=customtkinter.CTk()
        root.title("Update Complete Record.")
        root.geometry("400x600")
        root.config(bg="#D586FF")
        SAadhar = Label(root, text="Enter Aadhar Number to search for record.",bd=2,width=40,height=2,font=(18),bg="#3c1361")
        SAadhar.pack(padx=10,pady=10)
        SAadharEntry = Entry(root,bd=2,width=40,font=(18))
        SAadharEntry.pack(padx=10,pady=10)
        FatherName = Label(root,text="Enter your Father's Name",bd=2,width=40,height=2,font=(18),bg="#3c1361")
        FatherName.pack(padx=10,pady=10)
        FatherNameEnt = Entry(root,bd=2,width=40,font=(18))
        FatherNameEnt.pack(padx=10,pady=10)
        def f1vals():
            global uf1name,ufsearch
            ufsearch = SAadharEntry.get()
            uf1name = FatherNameEnt.get()

        def execute():
            f1vals()
            mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
            mycursor = mydb.cursor()
            mycursor.execute("UPDATE census_info SET Father_Name='{}' WHERE Aadhar_Number='{}'".format(uf1name,ufsearch))
            mydb.commit()
            root.destroy()
            messagebox.showinfo("Successful","Updated Father's Name in database.")

        BTN = Button(root,text="SAVE",activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32),command = execute)
        BTN.pack(padx=10,pady=10)

        root.resizable(False,False)
        root.mainloop()

    def mup():
        mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM census_info ORDER BY First_Name')
        root=customtkinter.CTk()
        root.title("Update Complete Record.")
        root.geometry("400x600")
        root.config(bg="#D586FF")
        SAadhar = Label(root, text="Enter Aadhar Number to search for record.",bd=2,width=40,height=2,font=(18),bg="#3c1361")
        SAadhar.pack(padx=10,pady=10)
        SAadharEntry = Entry(root,bd=2,width=40,font=(18))
        SAadharEntry.pack(padx=10,pady=10)
        MName = Label(root,text="Enter your Mother's Name",bd=2,width=40,height=2,font=(18),bg="#3c1361")
        MName.pack(padx=10,pady=10)
        MNameEnt = Entry(root,bd=2,width=40,font=(18))
        MNameEnt.pack(padx=10,pady=10)

        def mvals():
            global umname,ufsearch
            ufsearch = SAadharEntry.get()
            umname = MNameEnt.get()

        def execute():
            mvals()
            mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
            mycursor = mydb.cursor()
            mycursor.execute("UPDATE census_info SET Mother_Name='{}' WHERE Aadhar_Number='{}'".format(umname,ufsearch))
            mydb.commit()
            root.destroy()
            messagebox.showinfo("Successful","Updated Mother's Name in database.")

        BTN = Button(root,text="SAVE",activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32),command = execute)
        BTN.pack(padx=10,pady=10)

        root.resizable(False,False)
        root.mainloop()

    def csup():
        mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM census_info ORDER BY First_Name')
        root=customtkinter.CTk()
        root.title("Update Complete Record.")
        root.geometry("400x600")
        root.config(bg="#D586FF")
        SAadhar = Label(root, text="Enter Aadhar Number to search for record.",bd=2,width=40,height=2,font=(18),bg="#3c1361")
        SAadhar.pack(padx=10,pady=10)
        SAadharEntry = Entry(root,bd=2,width=40,font=(18))
        SAadharEntry.pack(padx=10,pady=10)
        CAS = Label(root,text="Enter your City and State(City/State)",bd=2,width=40,height=2,font=(18),bg="#3c1361")
        CAS.pack(padx=10,pady=10)
        CASEnt = Entry(root,bd=2,width=40,font=(18))
        CASEnt.pack(padx=10,pady=10)
        def csvals():
            global ucsname,ufsearch
            ufsearch = SAadharEntry.get()
            ucsname = CASEnt.get()

        def execute():
            csvals()
            mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
            mycursor = mydb.cursor()
            mycursor.execute("UPDATE census_info SET City_And_State='{}' WHERE Aadhar_Number='{}'".format(ucsname,ufsearch))
            mydb.commit()
            root.destroy()
            messagebox.showinfo("Successful","Updated City & State in database.")

        BTN = Button(root,text="SAVE",activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32),command = execute)
        BTN.pack(padx=10,pady=10)

        root.resizable(False,False)
        root.mainloop()

    def crup():
        mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM census_info ORDER BY First_Name')
        root=customtkinter.CTk()
        root.title("Update Complete Record.")
        root.geometry("400x800")
        root.config(bg="#D586FF")

        SAadhar = Label(root, text="Enter Aadhar Number to search for record.",bd=2,width=40,height=1,font=(18),bg="#3c1361")
        SAadhar.pack(padx=10,pady=10)
        SAadharEntry = Entry(root,bd=2,width=40,font=(18))
        SAadharEntry.pack(padx=10,pady=10)
        FName = Label(root,text="Enter your First Name",bd=2,width=40,height=1,font=(18),bg="#3c1361")
        FName.pack(padx=10,pady=10)
        FNameEnt = Entry(root,bd=2,width=40,font=(18))
        FNameEnt.pack(padx=10,pady=10)
        LName = Label(root,text="Enter your Last Name",bd=2,width=40,height=1,font=(18),bg="#3c1361")
        LName.pack(padx=10,pady=10)
        LNameEnt = Entry(root,bd=2,width=40,font=(18))
        LNameEnt.pack(padx=10,pady=10)
        DOB = Label(root,text="Enter your Date Of Birth(YYYY-MM-DD)",bd=2,width=40,height=1,font=(18),bg="#3c1361")
        DOB.pack(padx=10,pady=10)
        DOBEnt = Entry(root,bd=2,width=40,font=(18))
        DOBEnt.pack(padx=10,pady=10)
        EID = Label(root,text="Enter your Email ID",bd=2,width=40,height=1,font=(18),bg="#3c1361")
        EID.pack(padx=10,pady=10)
        EIDEnt = Entry(root,bd=2,width=40,font=(18))
        EIDEnt.pack(padx=10,pady=10)
        ANumber = Label(root,text="Enter your Aadhar Number",bd=2,width=40,height=1,font=(18),bg="#3c1361")
        ANumber.pack(padx=10,pady=10)
        ANumberEnt = Entry(root,bd=2,width=40,font=(18))
        ANumberEnt.pack(padx=10,pady=10)
        FatherName = Label(root,text="Enter your Father's Name",bd=2,width=40,height=1,font=(18),bg="#3c1361")
        FatherName.pack(padx=10,pady=10)
        FatherNameEnt = Entry(root,bd=2,width=40,font=(18))
        FatherNameEnt.pack(padx=10,pady=10)
        MName = Label(root,text="Enter your Mother's Name",bd=2,width=40,height=1,font=(18),bg="#3c1361")
        MName.pack(padx=10,pady=10)
        MNameEnt = Entry(root,bd=2,width=40,font=(18))
        MNameEnt.pack(padx=10,pady=10)
        CAS = Label(root,text="Enter your City and State(City/State)",bd=2,width=40,height=1,font=(18),bg="#3c1361")
        CAS.pack(padx=10,pady=10)
        CASEnt = Entry(root,bd=2,width=40,font=(18))
        CASEnt.pack(padx=10,pady=10)

        def ucvals():
            global ufsearch,ufname,ulname,udob,uemail,uadhaar,uf1name,umname,ucsname
        ufsearch = SAadharEntry.get()
        ufname = FNameEnt.get()
        ulname = LNameEnt.get()
        udob = DOBEnt.get()
        uemail = EIDEnt.get()
        uadhaar = ANumberEnt.get()
        uf1name = FatherNameEnt.get()
        umname = MNameEnt.get()
        ucsname = CASEnt.get()

        def execute():
            ucvals()
            mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
            mycursor = mydb.cursor()
            mycursor.execute("UPDATE census_info SET First_Name='{}',Last_Name='{}',Date_Of_Birth='{}',Email_ID='{}',Aadhar_Number='{}',Father_Name='{}',Mother_Name='{}',City_And_State='{}' WHERE Aadhar_Number='{}'".format(ufname,ulname,udob,uemail,uadhaar,uf1name,umname,ucsname,ufsearch))
            mydb.commit()
            root.destroy()
            messagebox.showinfo("Successful","Updated complete Record in database.")

        BTN = Button(root,text="SAVE",activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=1,font=(32),command= execute)
        BTN.pack(padx=10,pady=10)

        root.resizable(False,False)
        root.mainloop()

    bt1 = Button(root,text="Update First Name.",activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32),command = fup).pack()
    bt2 = Button(root,text="Update Last Name.",activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32),command = lup).pack()
    bt3 = Button(root,text="Update Date of Birth.",activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32),command = dobup).pack()
    bt4 = Button(root,text="Update Email ID.",activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32),command=eidup).pack()
    bt5 = Button(root,text="Update Aadhar Number.",activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32),command = aadharup).pack()
    bt6 = Button(root,text="Update Father's Name.",activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32),command = fatherup).pack()
    bt7 = Button(root,text="Update Mother's Name.",activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32),command = mup).pack()
    bt8 = Button(root,text="Update City & State.",activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32),command = csup).pack()
    bt9 = Button(root,text="Update Complete Entry.",activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32),command = crup).pack()

    root.resizable(False,False)
    root.mainloop()
    root.destroy()

def setupcensus():#SETUP TABLE IN A PRE-MADE DATABASE #COMPLETE
    mydb = mysql.connector.connect(host="localhost",user=entT1,passwd=entT2,database=entT3)
    mycursor = mydb.cursor()
    mycursor.execute("create table if not exists census_info(First_Name varchar(64) not null,Last_Name varchar(64) null,Date_Of_Birth date not null,Email_ID varchar(255) not null unique,Aadhar_Number varchar(16) not null primary key,Father_Name varchar(64) not null,Mother_Name varchar(64)  not null,City_And_State varchar(100) not null);")
    messagebox.showinfo("Successful","Created table.Don't repeat this command again.")

#Frontend

def rfilename():
    file1 = simpledialog.askstring("File Input","Enter File Name with .CSV in the end.")
    if len(file1) == 0:
        messagebox.showerror('Error', 'Error: No file provided.')
    else:
        rcensus(file1)

def wfilename():
    file1 = simpledialog.askstring("File Input","Enter File Name with .CSV in the end.")
    if len(file1) == 0:
        messagebox.showerror('Error', 'Error: No file provided.')
    else:
        wcensus(file1)

def table2():
    Tlabel = Label(text="Main Menu : ",bg="#bca0dc",font=("Arial Rounded MT Bold",56,"bold")).pack()
    button1 = Button(text="Show Database Records.",command=lcensus,activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32)).pack(padx=10,pady=10)
    button2 = Button(text="Add A New Record in Database.",command=icensus,activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32)).pack(padx=10,pady=10)
    button3 = Button(text="Update A Record in Database.",command=ucensus,activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32)).pack(padx=10,pady=10)
    button4 = Button(text="Delete A Record from Database.",command=dcensus,activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32)).pack(padx=10,pady=10)
    button5 = Button(text="Search for A Record in Database.",command=scensus,activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32)).pack(padx=10,pady=10)
    button6 = Button(text="Import Data from CSV.",command=rfilename,activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32)).pack(padx=10,pady=10)
    button7 = Button(text="Export Records from Database to CSV.",command=wfilename,activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32)).pack(padx=10,pady=10)
    button8 = Button(text="Setup Table(from premade database only.).",command=setupcensus,activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32)).pack(padx=10,pady=10)
    button9 = Button(text="Quit Program.",command=quit,activebackground="#800080",bg = "#7c5295",bd=2,width=40,height=2,font=(32)).pack(padx=10,pady=10)

root.resizable(False,False)

root.mainloop()
