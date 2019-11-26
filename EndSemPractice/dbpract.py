import sqlite3
conn=sqlite3.connect('endsem7.db')
conn.execute("CREATE TABLE SEM4(SUBID INT PRIMARY KEY,SUBNM VARCHAR,CREDIT INT,GRADE VARCHAR);")
for i in range(5):
    a=input("Enter Subject ID,Subject Name, Credit and Grade")
    a=int(a)
    b=input()
    c=input()
    c=int(c)
    d=input()
    conn.execute("INSERT INTO SEM4 VALUES("+str(a)+",'"+b+"',"+str(c)+",'"+d+"');")
#conn.execute("INSERT INTO SEM4 VALUES(2,'COMP',4,'A');")
#conn.execute("INSERT INTO SEM4 VALUES(3,'SE',3,'A+');")
#conn.execute("INSERT INTO SEM4 VALUES(4,'DS',4,'A');")

cursor=conn.execute("SELECT * FROM SEM4;")
print("\nAfter insertion\n")
for row in cursor:
    print("The subject: ",row[1],"\tGrade: ",row[3])

conn.execute("UPDATE SEM4 SET GRADE='A' WHERE SUBID=3;")

cursor=conn.execute("SELECT * FROM SEM4;")
print("\nAfter updation\n")
for row in cursor:
    print("The subject: ",row[1],"\tGrade: ",row[3])

conn.execute("DELETE FROM SEM4 WHERE SUBID=4;")

cursor=conn.execute("SELECT * FROM SEM4;")
print("\nAfter deletion\n")
for row in cursor:
    print("The subject: ",row[1],"\tGrade: ",row[3])
