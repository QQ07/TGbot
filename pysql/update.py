import mysql.connector as c
con= c.connect(host="localhost", user="root", passwd="Rohan@1234", database="payroll ")

cursor = con.cursor()
empid = int(input("enter ID: "))
salary = int(input("Enter new salary: " ))
query = f"update emp set salary = {salary} where id ={empid}"
cursor.execute(query)
con.commit()
if cursor.rowcount>0:   #to check whether the ID exists or not (or to see whether anything is updated or not)
    print("Success")
else:
    print("No data found")