import mysql.connector as c
con= c.connect(host="localhost", user="root", passwd="Rohan@1234", database="payroll ")

cursor = con.cursor()
empid = int(input("enter ID: "))
name = input("enter name: ")
salary = int(input("enter salary: "))

query = f"insert into emp values({empid},'{name}','{salary}')"
# print(query)
cursor.execute(query)
con.commit()
print("data inserted")