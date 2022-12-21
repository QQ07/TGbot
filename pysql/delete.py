import mysql.connector as c
con= c.connect(host="localhost", user="root", passwd="Rohan@1234", database="payroll ")

cursor = con.cursor()
id = int(input("enter ID: ")) 
query =  f"delete from emp where id={id}"
con.execute(query)
con.commit()
if cursor.rowcount>0:   #to check whether the ID exists or not (or to see whether anything is updated or not)
    print("deletion Successfull")
else:
    print("No data found")