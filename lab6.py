#1. Create Database
import sqlite3 
con = sqlite3.connect('mydatabase.db')

#2. Create Table
import sqlite3
from sqlite3 import Error
def sql_connection():
    try:
        con = sqlite3.connect('mydatabase.db')
        return con
    except Error:
        print(Error)

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
    cursorObj.execute("INSERT INTO employees VALUES(1, 'John', 700, 'HR', 'Manager', '2017-01-04')")
    con.commit()
con = sql_connection()
sql_table(con)

#3. Insert Data
import sqlite3
con = sqlite3.connect('mydatabase.db')
def sql_insert(con, entities):
    cursorObj = con.cursor() 
    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities) 
    con.commit()
entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
sql_insert(con, entities)

#4. Update
import sqlite3
con = sqlite3.connect('mydatabase.db')
def sql_update(con):
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')
    con.commit()
sql_update(con)

#5. Select Statement
import sqlite3
con = sqlite3.connect('mydatabase.db')
def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM employees')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)
sql_fetch(con)


#6. Create table
import sqlite3
con = sqlite3.connect('mydatabase.db')
def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('create table if not exists projects(id integer, name text)')
    con.commit()
sql_fetch(con)

#7. Create table and insert data
import sqlite3
con = sqlite3.connect('mydatabase.db')
cursorObj = con.cursor()
cursorObj.execute('create table if not exists projects(id integer, name text)')
data = [(1, "Ridesharing"), (2, "Water Purifying"), (3, "Forensics"), (4, "Botany")]
cursorObj.executemany("INSERT INTO projects VALUES(?, ?)", data)
con.commit()

#8. Display tables in database
import sqlite3
con = sqlite3.connect('mydatabase.db')
def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT name from sqlite_master where type= "table"')
    print(cursorObj.fetchall())
sql_fetch(con)

#9. Display data
import sqlite3
con = sqlite3.connect('mydatabase.db')
def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT id, name FROM employees WHERE salary >= 800.0')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)
sql_fetch(con)

#10. Using date time function
import sqlite3
import datetime
con = sqlite3.connect('mydatabase.db')
cursorObj = con.cursor()
cursorObj.execute('create table if not exists assignments(id integer, name text, date date)')
data = [(1, "Mobile Ubiquitous", datetime.date(2017, 1, 2)), (2, "Internet Programming", datetime.date(2018, 3, 4))]
cursorObj.executemany("INSERT INTO assignments VALUES(?, ?, ?)", data)
con.commit()


#11. Create Login
from tkinter import *
#import library
5
import sqlite3
#open databse
#defining login function
def login():
    #getting form data
    uname=username.get()
    pwd=password.get()
    #applying empty validation
    if uname=='' or pwd=='':
        message.set("fill the empty field!!!")
    else:
        #open database
        conn = sqlite3.connect('login.db')
        #select query
        cursor = conn.execute('SELECT * from ADMIN where USERNAME="%s" and PASSWORD="%s"'%(uname,pwd))
        #fetch data 
        if cursor.fetchone():
            message.set("Login success")
        else:
            message.set("Wrong username or password!!!")
#defining loginform function
def Loginform():
    global login_screen
    login_screen = Tk()
    #Setting title of screen
    login_screen.title("Login Screen")
    #setting height and width of screen
    login_screen.geometry("350x250")
    login_screen["bg"]="#1C2833"
    #declaring variable
    global message
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    #Creating layout of login form
    Label(login_screen,width="300", text="Login From", 
    bg="#0E6655",fg="white",font=("Arial",12,"bold")).pack()
    #Username Label
    Label(login_screen, text="Username * ",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=40)
    #Username textbox
    Entry(login_screen, 
    textvariable=username,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x
    =120,y=42)
    #Password Label
    Label(login_screen, text="Password * ",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=80)
    #Password textbox
    Entry(login_screen, textvariable=password
    ,show="*",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=82)
    #Label for displaying login status[success/failed]
    Label(login_screen, 
    text="",textvariable=message,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=95,y=120)
    #Login button
    Button(login_screen, text="Login", width=10, height=1, command=login, 
    bg="#0E6655",fg="white",font=("Arial",12,"bold")).place(x=125,y=170)
    login_screen.mainloop()
#calling function Loginform
Loginform()

#12. Student registration system
#import libraries
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3

#function to define database
def Database():
    global conn, cursor
    #creating student database
    conn = sqlite3.connect("stud.db")
    cursor = conn.cursor()
    #creating STUD_REGISTRATION table
    cursor.execute("CREATE TABLE IF NOT EXISTS STUD_REGISTRATION (STU_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, STU_NAME TEXT, STU_CONTACT TEXT, STU_EMAIL TEXT, STU_ICNO TEXT, STU_BRANCH TEXT)")
#defining function for creating GUI Layout
def DisplayForm():
    #creating window
    display_screen = Tk()
    #setting width and height for window
    display_screen.geometry("900x400")
    #setting title for window
    display_screen.title("Student Management System")
    global tree
    global SEARCH
    global name,contact,email,icno,branch
    SEARCH = StringVar()
    name = StringVar()
    contact = StringVar()
    email = StringVar()
    icno = StringVar()
    branch = StringVar()
    #creating frames for layout
    #topview frame for heading
    TopViewForm = Frame(display_screen, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    #first left frame for registration from
    LFrom = Frame(display_screen, width="350")
    LFrom.pack(side=LEFT, fill=Y)
    #seconf left frame for search form
    LeftViewForm = Frame(display_screen, width=500,bg="gray")
    LeftViewForm.pack(side=LEFT, fill=Y)
    #mid frame for displaying students record
    MidViewForm = Frame(display_screen, width=600)
    MidViewForm.pack(side=RIGHT)
    #label for heading
    lbl_text = Label(TopViewForm, text="Student Management System", 
    font=('verdana', 18), width=600,bg="#1C2833",fg="white")
    lbl_text.pack(fill=X)
    #creating registration form in first left frame
    Label(LFrom, text="Name ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom,font=("Arial",10,"bold"),textvariable=name).pack(side=TOP, 
    padx=10, fill=X)
    Label(LFrom, text="Contact ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, 
    "bold"),textvariable=contact).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Email ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, 
    "bold"),textvariable=email).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="ICNo ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, 
    "bold"),textvariable=icno).pack(side=TOP, padx=10, fill=X)
    8
    Label(LFrom, text="Branch ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, 
    "bold"),textvariable=branch).pack(side=TOP, padx=10, fill=X)
    Button(LFrom,text="Submit",font=("Arial", 10, 
    "bold"),command=register).pack(side=TOP, padx=10,pady=5, fill=X)
    #creating search label and entry in second frame
    lbl_txtsearch = Label(LeftViewForm, text="Enter name to Search", 
    font=('verdana', 10),bg="gray")
    lbl_txtsearch.pack()
    #creating search entry
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 
    15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    #creating search button
    btn_search = Button(LeftViewForm, text="Search", 
    command=SearchRecord)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating view button
    btn_view = Button(LeftViewForm, text="View All", 
    command=DisplayData)
    btn_view.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating reset button
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating delete button
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    #setting scrollbar
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm,columns=("Student Id", "Name", 
    "Contact", "Email","ICNo","Branch"),
    selectmode="extended", height=100, 
    yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    #setting headings for the columns
    tree.heading('Student Id', text="Student Id", anchor=W)
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Contact', text="Contact", anchor=W)
    tree.heading('Email', text="Email", anchor=W)
    tree.heading('ICNo', text="ICNo", anchor=W)
    tree.heading('Branch', text="Branch", anchor=W)
    #setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()

#function to insert data into database
def register():
    Database()
    #getting form data
    name1=name.get()
    con1=contact.get()
    email1=email.get()
    icn=icno.get()
    branch1=branch.get()
    #applying empty validation
    if name1=='' or con1==''or email1=='' or icn==''or branch1=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!!")
    else:
        #execute query
        conn.execute('INSERT INTO STUD_REGISTRATION (STU_NAME,STU_CONTACT,STU_EMAIL,STU_ICNO,STU_BRANCH) \VALUES (?,?,?,?,?)',(name1,con1,email1,icn,branch1))
        conn.commit()
        tkMessageBox.showinfo("Message","Stored successfully")
        #refresh table data
        DisplayData()
        conn.close()

def Reset():
    #clear current data from table
    tree.delete(*tree.get_children())
    #refresh table data
    DisplayData()
    #clear search text
    SEARCH.set("")
    name.set("")
    contact.set("")
    email.set("")
    icno.set("")
    branch.set("")

def Delete():
    #open database
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
        icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor=conn.execute("DELETE FROM STUD_REGISTRATION WHERE STU_ID = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

#function to search data
def SearchRecord():
    #open database
    Database()
    #checking search text is empty or not
    if SEARCH.get() != "":
        #clearing current display data
        tree.delete(*tree.get_children())
        #select query with where clause
        cursor=conn.execute("SELECT * FROM STUD_REGISTRATION WHERE STU_NAME LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        #fetch all matching records
        fetch = cursor.fetchall()
        #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

#defining function to access data from SQLite database
def DisplayData():
    #open database
    Database()
    #clear current data
    tree.delete(*tree.get_children())
    #select query
    cursor=conn.execute("SELECT * FROM STUD_REGISTRATION")
    11
    #fetch all data from database
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

#calling function
DisplayForm()
if __name__=='__main__':
    #Running Application
    mainloop()

#Trythis
import sqlite3
from sqlite3 import Error
def sql_connection():
    try:
        con = sqlite3.connect('mydatabase.db')
        return con
    except Error:
        print(Error)

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("DROP TABLE IF EXISTS EMP")
    cursorObj.execute("DROP TABLE IF EXISTS DEPT")
    cursorObj.execute("DROP TABLE IF EXISTS JOB")

    cursorObj.execute("DROP TABLE IF EXISTS Departments")

    cursorObj.execute("CREATE TABLE IF NOT EXISTS EMP (Emp_No INT PRIMARY KEY, Emp_Name VARCHAR(255), Job_ID INT, Age INT, Hiredate DATE, Salary INT, Dept_No INT, Mgr INT)")

    data = [
    (7369, "Salleh", 5, 35, "1990-12-17", 800, 20, 7902),
    (7499, "Alan", 4, 46, "1991-02-20", 1600, 30, 7698),
    (7521, "Wanie", 4, 43, "1991-02-22", 1250, 30, 7698),
    (7566, "Jonny", 2, 51, "1991-04-02", 2953, 20, 7839),
    (7654, "Maria", 4, 38, "1991-09-28", 1250, 30, 7698),
    (7698, "Bakar", 2, 53, "1991-05-01", 2850, 30, 7839),
    (7782, "Clark", 2, 48, "1991-06-09", 2450, 10, 7839),
    (7788, "Suria", 3, 45, "1997-07-09", 3000, 20, 7566),
    (7839, "King", 1, 57, "1991-11-17", 5000, 10, None),
    (7488, "Tina", 4, 33, "1991-09-08", 1500, 30, 7698),
    (7876, "Adam", 5, 29, "1997-07-13", 1100, 20, 7788),
    (7900, "Johan", 5, 30, "1992-12-13", 950, 30, 7698),
    (7902, "Fairuz", 3, 43, "1991-12-03", 3000, 20, 7566),
    (7934, "Mary", 5, 31, "1994-01-23", 1300, 10, 7782)
    ]
    cursorObj.executemany("INSERT INTO EMP VALUES (?, ?, ?, ?, ?, ?, ?, ?)", data)

    cursorObj.execute("CREATE TABLE IF NOT EXISTS DEPT (Dept_No INT PRIMARY KEY,Dept_Name VARCHAR(255) NOT NULL,Floor VARCHAR(255))")
    data = [
        (10, 'Accounting', 'Top'),
        (20, 'Research', 'Basement'),
        (30, 'Sales', 'Ground'),
        (40, 'Operations', 'Second')  
    ]
    cursorObj.executemany("INSERT INTO DEPT (Dept_No, Dept_Name, Floor) VALUES (?, ?, ?)", data)

    cursorObj.execute("CREATE TABLE IF NOT EXISTS JOB (Job_Id INT PRIMARY KEY,Job_Title VARCHAR(255),LowSal INT,HighSal INT)")
    data = [
        (1, 'President', 3001, 9999),
        (2, 'Manager', 2001,3000),
        (3, 'Analyst', 1401,2000),
        (4, 'Salesperson', 1201,1400),
        (5, 'Clerk', 700,1200)  
    ]
    cursorObj.executemany("INSERT INTO JOB (Job_Id, Job_Title, LowSal, HighSal) VALUES (?, ?, ?, ?)", data)

    con.commit()

def get_q1(con):
    cursorObj = con.cursor()
    cursorObj.execute("""
    SELECT 
        SUM(Salary) AS TotalSalary,
        MAX(Salary) AS MaxSalary,
        MIN(Salary) AS MinSalary,
        AVG(Salary) AS AvgSalary
    FROM EMP
    GROUP BY Emp_No
    HAVING AVG(Salary) > 1000 
    """)

    results = cursorObj.fetchall()
    print("Question 1 - Salary")
    print("-" * 90)  
    for row in results:
        print(f"Total Salary: {row[0]} | Maximum Salary: {row[1]} | Minimum Salary: {row[2]} | Average Salary: {row[3]} ")
        print("-" * 90)  

def get_q2(con):
    cursorObj = con.cursor()
    cursorObj.execute("""
    SELECT 
        EMP.Emp_Name AS EmployeeName,
        JOB.Job_Title AS JobTitle,
        DEPT.Dept_Name AS Department
    FROM EMP
    INNER JOIN JOB ON EMP.Job_ID = JOB.Job_Id
    INNER JOIN DEPT ON EMP.Dept_No = DEPT.Dept_No
    """)

    results = cursorObj.fetchall()
    print("Question 2 - Employee Details")
    print("-" * 65)  # Separator
    for row in results:
        print(f"Employee Name: {row[0]}| Job Title: {row[1]} | Department: {row[2]} ")
        print("-" * 65)  # Separator

def get_q3(con):
    cursorObj = con.cursor()
    cursorObj.execute("""
    SELECT 
        Emp_Name AS EmployeeName,
        Hiredate AS HireDate,
        Salary AS Salary
    FROM EMP
    WHERE Hiredate > '1995-12-31'
    """)

    results = cursorObj.fetchall()
    print("Question 3 - Employees Hired After 1995")
    print("-" * 65)  # Separator
    for row in results:
        print(f"Employee Name: {row[0]} | Hire Date: {row[1]} | Salary: {row[2]}")
        print("-" * 65)  # Separator

# Call the function
con = sql_connection()
sql_table(con)
get_q1(con)
print("\n")
get_q2(con)
print("\n")
get_q3(con)
