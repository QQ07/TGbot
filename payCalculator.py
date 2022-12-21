import mysql.connector as c
con= c.connect(host="localhost", user="root", passwd="Rohan@1234", database="payroll")
cursor = con.cursor()

def percent(p,x):
    p=p/100
    return int(x*p)

def Payroll(msg):
    reply = '--Payroll of Employee--\n'
    id = msg[-1]
    cursor.execute(f"select * from emp where id ={id}")
    record = cursor.fetchall()[0]
    print(record)
    name = record[1]
    bSalary = record[2]
    reply += f'ID: {record[0]}\nName:{record[1]}\nBase Salary = ₹{record[2]}\n\n'
    cursor.execute("select * from taxes")
    taxes = cursor.fetchall()
    tt = 0             #total tax in %
    for tax in taxes:
        deduc = tax[1]
        reply += f"{tax[0]} tax: ₹{percent(deduc,bSalary)}\n"
        tt += int(tax[1])
    Csalary = bSalary - percent(tt, bSalary)
    reply+='\n'
    # print(salary)
    # print(reply)
    cursor.execute("select * from allowances")
    allowances = cursor.fetchall()
    ta = 0             #total allowance in %
    for a in allowances:
        addi = a[1]
        reply += f"{a[0]} allowance: ₹{percent(addi,bSalary)}\n"
        ta += int(a[1])
    salary = Csalary + percent(ta, bSalary)
    
    reply+=f'\n\nSalary of {name} after all deductions and allowances is: \n{salary}'
    print(reply)
    return reply
# Payroll("payroll of emp 1")