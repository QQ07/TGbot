import mysql.connector as c
con= c.connect(host="localhost", user="root", passwd="Rohan@1234", database="payroll ")

cursor = con.cursor()
cursor.execute("select * from emp where id=3")
record = cursor.fetchone()
print(record)