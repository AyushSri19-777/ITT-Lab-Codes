import sqlite3
conn=sqlite3.connect('students.db')
conn.execute("CREATE TABLE student (id INT PRIMARY KEY, name VARCHAR);")
conn.execute("INSERT INTO student VALUES(1, 'Kavya');")
conn.execute("INSERT INTO student VALUES(2, 'Sankalp');")
conn.execute("INSERT INTO student VALUES(3, 'Ayush');")
conn.execute("INSERT INTO student VALUES(4, 'Raloue');")

stuList=[]
l=0

cursor=conn.execute("SELECT * FROM student")

print("The student names are:")
for i in cursor:
	print(i[1])
	stuList.append(i[1])
	l=l+1

for i in range(0, l):
	low=i
	for j in range(i+1,l):
		if (stuList[j]<stuList[low]):
			low=j
	temp=stuList[i]
	stuList[i]=stuList[low]
	stuList[low]=temp

print("\nThe list, in alphabetical order:")
for i in stuList:
	print(i)


conn.commit()
conn.close()
