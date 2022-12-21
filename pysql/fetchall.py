import mysql.connector as c
con= c.connect(host="localhost", user="root", passwd="Rohan@1234", database="payroll ")

cursor = con.cursor()
# msg = input("ejflkj: ")
# id = msg[-1]
# cursor.execute(f"select * from emp where id={id};")
# salary = cursor.fetchone()[-1]
# print(salary)
cursor.execute("select * from emp")
record = cursor.fetchall()
for i in record:
    print(i)
print("total number of records =", cursor.rowcount)