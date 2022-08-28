from tkinter import *
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
            sqlform = "DELETE FROM census_info WHERE Aadhar_Number ={dchoice}"
            mycursor.execute(sqlform)
            mydb.commit()
            break
        else:
            print("Error : No Enteries exists with this Aadhar number in database.")


def lcensus():
    mycursor.execute('SELECT * FROM census_info ORDER BY First_Name')
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        print("No Records to show in database.")
    else:
        for i in myresult:
            print("First Name Last Name Date Of Birth Email ID Aadhar Number Father's Name Mother's Name City and State")
            for j in i:
                print(j,end=" ")

def scensus():
    schoice = input("Enter Aadhar number to search entry : ")
    mycursor.execute('SELECT * FROM census_info ORDER BY First_Name')
    myresult = mycursor.fetchall()
    for i in myresult:
        if schoice == i[4]:
            print(i)
            break
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

        for i in myresult: 

            if Aadhar_Number == i[0]:
                print("Error : Same Aadhar Number address already exists in database.")
                break
            else:
                y = (First_Name, Last_Name, Date_Of_Birth, Email,Aadhar_Number,Father_Name,Mother_Name,City_And_State)
                x.append(y)

        choice = input("Would you like to enter more entries?(Y/N) : ")
        if choice == "Y" or choice == "T" or choice == "y" or choice == "t":
            continue
        else:
            break

    sqlform = "Insert into census_info(First_Name,Last_Name,Date_Of_Birth,Email_ID,Aadhar_Number,Father_Name,Mother_Name,City_And_State) VALUES (%s, %s, %s, %s,%s, %s, %s, %s)"
    mycursor.executemany(sqlform,x)

    mydb.commit()



#main

print("Welcome to the database.")
print("Choice 1 : Show All The Records.")
print("Choice 2 : Add a new Record.")
print("Choice 3 : Delete the Record.")
print("Choice 4 : Search for a Record.")

Tchoice = int(input("Enter the choice to do operation : "))

if Tchoice == 1:
    lcensus()
elif Tchoice == 2:
    icensus()
elif Tchoice == 3:
    dcensus()
elif Tchoice == 4:
    scensus()
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