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
    x=[]
    a = ""
    with open(file1, "r") as f:
        reader = csv.reader(f)
        test = f.readline()
        if len(test) == 0:
            print("Error : No Data Available in CSV file.")
        else:
            x=[]
            for i in reader:
                j = (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
                x.append(j)
            sqlform = "INSERT INTO census_info(First_Name,Last_Name,Date_Of_Birth,Email_ID,Aadhar_Number,Father_Name,Mother_Name,City_And_State) VALUES (%s, %s, %s, %s,%s, %s, %s, %s)"
            mycursor.executemany(sqlform,x)
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

#main

while True:
    print("Welcome to the database.")
    print("Choice 1 : Show All The Records.")
    print("Choice 2 : Add a new Record.")
    print("Choice 3 : Delete the Record.")
    print("Choice 4 : Search for a Record.")
    print("Choice 5 : Add records from a CSV file.")
    print("Choice 6 : Fetch all records to a CSV file.")
    print("Choice 7 : Quit Program")

    Ochoice = int(input("Enter the choice to do operation : "))

    if Ochoice == 1:
        lcensus()
    elif Ochoice == 2:
        icensus()
    elif Ochoice == 3:
        dcensus()
    elif Ochoice == 4:
        scensus()
    elif Ochoice == 5:
        x1 = input("Enter file name(must add .csv in end) : ")
        rcensus(x1)
    elif Ochoice == 6:
        x1 = input("Enter file name(must add .csv in end) : ")
        wcensus(x1)
    elif Ochoice == 7:
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