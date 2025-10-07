import mysql.connector as a   #importing mysql connector
con = a.connect(host="localhost", user="root", password="kk27", use_pure=True) 
c = con.cursor()   #creating a cursor for mysql execution
# mysql commands
c.execute("create database Library;")
c.execute("use library;")
c.execute("create table books(bookname varchar(50), total int, subject varchar(50));")
c.execute("create table issue(name varchar(50), regno varchar(50) NOT NULL PRIMARY KEY, bookname varchar(50), issue varchar(50));")
c.execute("create table submit(name varchar(50), regno varchar(50) NOT NULL PRIMARY KEY, bookname varchar(50), submit varchar(50));")

# for adding a book
def addbook():
    c = con.cursor()
    n = input("Enter Name of the BOOK you want to add: ")
    t = input("Total Books: ")
    s = input("Enter Subject:")
    sql = "insert into books values('{}', {}, '{}')".format(n, t, s)
    c.execute(sql)
    con.commit()
    print("Data entered successfully")
    input("Press ENTER to continue")
    main()

# for issue a book
def issuebook():
    c = con.cursor()
    n = input("Enter your Name:")
    r = input("Enter registration number:")
    bn = input("Enter Book Name:")
    d = input("Enter Date:")
    a = "insert into issue values('{}', '{}', '{}', '{}')".format(n, r, bn, d)
    c.execute(a)
    con.commit()
    print("Book Issued successfully to", n)
    bookup(bn, -1)

# for submitting a book
def submitbook():
    c = con.cursor()
    n = input("Enter your Name: ")
    r = input("Enter Registration number: ")
    bn = input("Enter Book name: ")
    d = input("Enter Date: ")
    a = "insert into submit values('{}', '{}', '{}', '{}')".format(n, r, bn, d)
    c.execute(a)
    con.commit()
    print("Book submitted from ", n)
    bookup(bn, 1)

# for updating when book is issued or submitted
def bookup(bn, u):
    a = "select total from books where bookname='{}'".format(bn)
    c = con.cursor()
    c.execute(a)
    myresult = c.fetchone()
    t = myresult[0] + u
    sql = "update books set total={} where bookname='{}'".format(t, bn)
    c.execute(sql)
    con.commit()
    input("Press ENTER to continue")
    main()

# for deleting a book
def deletebook():
    print("This option is only available for the LIBRARIAN")
    p = input("Enter password:")
    if p == 'KVK1':
        an = input("Enter Book name:")
        a = "delete from books where bookname='{}'".format(an)
        c = con.cursor()
        c.execute(a)
        con.commit()
        if c.rowcount > 0:
            print("Book deleted successfully")
        else:
            print("No book found of this name")
        input("Press ENTER to continue")
        main()
    else:
        print("WRONG PASSWORD ENTERED !")
        input("Press ENTER to continue")
        main()

# for displaying all books
def displaybook():
    a = "select * from books"
    c = con.cursor()
    c.execute(a)
    myresult = c.fetchall()
    for i in myresult:
        print("Book name:", i[0])
        print("Total:", i[1])
    input("Press ENTER to continue")
    main()


def main():
    print("""
                                                  ----- LIBRARY MANAGER -----

                                                  1.ADD/DONATE BOOK
                                                  2.ISSUE BOOK
                                                  3.SUBMIT BOOK
                                                  4.DELETE BOOK
                                                  5.DISPLAY BOOKS
                                                  6.EXIT
                                                  """)
    choice = input("Enter Task number:")
    if choice == '1':
        addbook()
    elif choice == '2':
        issuebook()
    elif choice == '3':
        submitbook()
    elif choice == '4':
        deletebook()
    elif choice == '5':
        displaybook()
    elif choice == '6':
        exit()
    else:
        print("Wrong Choice...")
        main()

# setting up the password so that not everyone can access
def password():
    ps = input("Enter Password: ")
    if ps == "library123":
        main()
    else:
        print("Wrong Password")
        password()

password()
