#backend

import csv
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="census_info")
mycursor = mydb.cursor()

#setup

def dcensus(): 
    dchoice = input("Enter Aadhar number to delete entry : ")
    mycursor.execute('SELECT * FROM census_info ORDER BY First_Name')
    myresult = mycursor.fetchall()
    for i in myresult:
        if dchoice == i[4]:
            mycursor.execute("DELETE FROM census_info WHERE Aadhar_Number='{}'".format(dchoice))
            mydb.commit()
            print("Successfully Deleted")
            break
        else:
            print("Error : No Enteries exists with this Aadhar number in database.")


def lcensus():
    a = 1
    mycursor.execute('SELECT * FROM census_info ORDER BY First_Name')
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        print("Error : No Records to show in database.")
    else:
        for i in myresult:
            print("Record Number : ",a)

            print("First Name : ",i[0])
            print("Last Name : ",i[1])
            print("Date Of Birth : ",i[2])
            print("Email ID : ",i[3])
            print("Aadhar Number : ",i[4])
            print("Father's Name : ",i[5])
            print("Mother's Name : ",i[6])
            print("City & State : ",i[7])

            a = a+1

def scensus():
    a = 0
    schoice = input("Enter Aadhar number to search entry : ")
    mycursor.execute('SELECT * FROM census_info ORDER BY First_Name')
    myresult = mycursor.fetchall()
    for i in myresult:
        if schoice == i[4]:
            a = 1
            b = i
            break
    if a == 1:
        print(b)
    else:
        print("Error : No Enteries exists with this Aadhar number in database.")

def icensus():
    x = []
    mycursor.execute('SELECT Aadhar_Number,Date_Of_Birth FROM census_info ORDER BY First_Name')
    myresult = mycursor.fetchall()

    while True:
        First_Name = input("First Name : ")
        Last_Name = input("Last Name : ")
        Date_Of_Birth = input("Date Of Birth(YYYY-MM-DD) : ")
        Email = input("Email ID : ")
        Aadhar_Number = input("Aadhar Number : ")
        Father_Name = input("Father's Name : ")
        Mother_Name = input("Mother's Name : ")
        City_And_State = input("City and State : ")
        
        if len(myresult) == 0:
            y = (First_Name, Last_Name, Date_Of_Birth, Email,Aadhar_Number,Father_Name,Mother_Name,City_And_State)
            x.append(y)
            
        else:
            for i in myresult: 
                if Aadhar_Number == i[0]:
                    print("Error : Same Aadhar Number address already exists in database,Try Again.")
                    break
                else:
                    y = (First_Name, Last_Name, Date_Of_Birth, Email,Aadhar_Number,Father_Name,Mother_Name,City_And_State)
                    x.append(y)

        choice = input("Would you like to enter more entries?(Y/N) : ")
        if choice == "Y" or choice == "T" or choice == "y" or choice == "t":
            continue
        else:
            break

    sqlform = "INSERT INTO census_info(First_Name,Last_Name,Date_Of_Birth,Email_ID,Aadhar_Number,Father_Name,Mother_Name,City_And_State) VALUES (%s, %s, %s, %s,%s, %s, %s, %s)"
    mycursor.executemany(sqlform,x)
    mydb.commit()

def rcensus(file1):
    y=[]
    with open(file1, "r") as f:
        reader = csv.reader(f)
        trash = f.readline()
        for j in reader:
            if len(j) == 0:
                a = list(j)
            else:
                y.append(j)
        if len(y) == 0:
            print("Error : No Data Available in CSV file.")
        else:
            sqlform = "INSERT INTO census_info(First_Name,Last_Name,Date_Of_Birth,Email_ID,Aadhar_Number,Father_Name,Mother_Name,City_And_State) VALUES (%s, %s, %s, %s,%s, %s, %s, %s)"
            mycursor.executemany(sqlform,y)
            mydb.commit()
            print("Successfully Imported All Data.")

def wcensus(file1):
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
            print("Successfully Exported All Data to CSV file.")
        else:
            print("Error : No Records to show in database.")

def ucensus():
    print("Pick Option to Update respective field.")
    print("Choice 1 : Update First Name.")
    print("Choice 2 : Update Last Name.")
    print("Choice 3 : Update Date of Birth.")
    print("Choice 4 : Update Email ID.")
    print("Choice 5 : Update Aadhar Number.")
    print("Choice 6 : Update Father's Name.")
    print("Choice 7 : Update Mother's Name.")
    print("Choice 8 : Update City & State.")
    print("Choice 9 : Update Complete Entry.")

    Uchoice = int(input("Enter the choice to do Operation : "))

    if Uchoice == 1:
        ufseach = input("Enter the Aadhar Number(To Search the entry in database) : ")
        ufname = input("Enter the new First Name : ")
        mycursor.execute("UPDATE census_info SET First_Name='{}' WHERE Aadhar_Number='{}'".format(ufname,ufseach))
        mydb.commit()
        print("Successfully updated First Name in database.")
    elif Uchoice == 2:
        ufseach = input("Enter the Aadhar Number(To Search the entry in database) : ")
        ufname = input("Enter the new Last Name : ")
        mycursor.execute("UPDATE census_info SET Last_Name='{}' WHERE Aadhar_Number='{}'".format(ufname,ufseach))
        mydb.commit()
        print("Successfully updated Last Name in database.")
    elif Uchoice == 3:
        ufseach = input("Enter the Aadhar Number(To Search the entry in database) : ")
        ufname = input("Enter the new Date of Birth(YYYY-MM-DD) : ")
        mycursor.execute("UPDATE census_info SET Date_Of_Birth='{}' WHERE Aadhar_Number='{}'".format(ufname,ufseach))
        mydb.commit()
        print("Successfully updated Date of Birth in database.")
    elif Uchoice == 4:
        ufseach = input("Enter the Aadhar Number(To Search the entry in database) : ")
        ufname = input("Enter the new Email ID : ")
        mycursor.execute("UPDATE census_info SET Email_ID='{}' WHERE Aadhar_Number='{}'".format(ufname,ufseach))
        mydb.commit()
        print("Successfully updated Email ID in database.")
    elif Uchoice == 5:
        ufseach = input("Enter the Aadhar Number(To Search the entry in database) : ")
        ufname = input("Enter the new Aadhar Number : ")
        mycursor.execute("UPDATE census_info SET Aadhar_Number='{}' WHERE Aadhar_Number='{}'".format(ufname,ufseach))
        mydb.commit()
        print("Successfully updated Aadhar Number in database.")
    elif Uchoice == 6:
        ufseach = input("Enter the Aadhar Number(To Search the entry in database) : ")
        ufname = input("Enter the new Father's Name : ")
        mycursor.execute("UPDATE census_info SET Father_Name='{}' WHERE Aadhar_Number='{}'".format(ufname,ufseach))
        mydb.commit()
        print("Successfully updated Father's Name in database.")
    elif Uchoice == 7:
        ufseach = input("Enter the Aadhar Number(To Search the entry in database) : ")
        ufname = input("Enter the new Mother's Name : ")
        mycursor.execute("UPDATE census_info SET Mother_Name='{}' WHERE Aadhar_Number='{}'".format(ufname,ufseach))
        mydb.commit()
        print("Successfully updated Mother's Name in database.")
    elif Uchoice == 8:
        ufseach = input("Enter the Aadhar Number(To Search the entry in database) : ")
        ufname = input("Enter the new City & State : ")
        mycursor.execute("UPDATE census_info SET City_And_State='{}' WHERE Aadhar_Number='{}'".format(ufname,ufseach))
        mydb.commit()
        print("Successfully updated City & State in database.")
    elif Uchoice == 9:
        ufseach = input("Enter the Aadhar Number(To Search the entry in database) : ")
        ufname = input("Enter the new First Name : ")
        ulname = input("Enter the new Last Name : ")
        udob = input("Enter the new Date of Birth(YYYY-MM-DD) : ")
        uemail = input("Enter the new Email ID : ")
        uadhaar = input("Enter the new Aadhar Number : ")
        uf1name = input("Enter the new Father's Name : ")
        umname = input("Enter the new Mother's Name : ")
        ucsname = input("Enter the new City & State Name : ")
        mycursor.execute("UPDATE census_info SET First_Name='{}',Last_Name='{}',Date_Of_Birth='{}',Email_ID='{}',Aadhar_Number='{}',Father_Name='{}',Mother_Name='{}',City_And_State='{}' WHERE Aadhar_Number='{}'".format(ufname,ulname,udob,uemail,uadhaar,uf1name,umname,ucsname,ufseach))
        mydb.commit()
        print("Successfully updated complere entry in database.")
    else:
        print("Invalid choice.")

#main

while True:
    print("Welcome to the database.")
    print("Choice 1 : Show All The Records.")
    print("Choice 2 : Add a new Record.")
    print("Choice 3 : Update an existing Record.")
    print("Choice 4 : Delete the Record.")
    print("Choice 5 : Search for a Record.")
    print("Choice 6 : Add records from a CSV file.")
    print("Choice 7 : Fetch all records to a CSV file.")
    print("Choice 8 : Quit Program")

    Ochoice = int(input("Enter the choice to do operation : "))

    if Ochoice == 1:
        lcensus()
    elif Ochoice == 2:
        icensus()
    elif Ochoice == 3:
        ucensus()
    elif Ochoice == 4:
        dcensus()
    elif Ochoice == 5:
        scensus()
    elif Ochoice == 6:
        x1 = input("Enter file name(must add .csv in end) : ")
        rcensus(x1)
    elif Ochoice == 7:
        x1 = input("Enter file name(must add .csv in end) : ")
        wcensus(x1)
    elif Ochoice == 8:
        break
    else:
        print("Invalid choice : Try again.")







# create database census_info;





# create table census_info(
# First_Name varchar(64) not null,
# Last_Name varchar(64) null,
# Date_Of_Birth date not null,
# Email_ID varchar(255) not null unique,
# Aadhar_Number varchar(16) not null primary key,
# Father_Name varchar(64) not null,
# Mother_Name varchar(64)  not null,
# City_And_State varchar(100) not null);





#made by Aman