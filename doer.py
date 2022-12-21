import mysql.connector as c
# from prettytable import PrettyTable

con = c.connect(host="localhost", user="root", passwd="Rohan@1234", database="payroll")
cursor = con.cursor()

def perform(q):
    print("in admin")
    q = q.lower() 
    q = q.strip()
    L = q.split(" ")
    msg = 'incorrect command'
    # print(L)
    
    if "add" in L:
        if "employee" in L:
            id = L[2]
            name = L[3].capitalize()
            salary=L[4]
            print(f"data({id},'{name}','{salary}') inserting in employee table")
            query = f"insert into emp values({id},'{name}','{salary}')"
            # print(query)
            cursor.execute(query)
            con.commit()
            print(f"data({id},'{name}','{salary}') inserted")
            msg = f"data({id},'{name}','{salary}') inserted"
            
        if "tax" in L:
            name= L[2]
            percent = L[3]
            print(f"data('{name}',{percent}) inserting in taxes table")
            query = f"insert into taxes values('{name}',{percent})"
            # print(query)
            cursor.execute(query)
            con.commit()
            print(f"data('{name}',{percent}) inserted in taxes")
            msg = f"data('{name}',{percent}) inserted in taxes"
            
        if "allowance" in L:
            name= L[2]
            percent = L[3]
            print(f"data('{name}',{percent}) inserting in allowances table")
            query = f"insert into allowances values('{name}',{percent})"
            # print(query)
            cursor.execute(query)
            con.commit()
            print(f"data('{name}',{percent}) inserted in allowances")
            msg = f"data('{name}',{percent}) inserted in allowances"
    
    
    if "delete" in L:
        if "employee" in L:
            id = L[2]
            query =  f"delete from emp where id = {id}"
            cursor.execute(query)
            con.commit()
            print(f"id {id} deleted")
            msg = f"id {id} deleted"
            
        if "tax" in L:
            name = L[2]
            query =  f"delete from taxes where name = '{name}'"
            cursor.execute(query)
            con.commit()
            print(f"{name} tax deleted")
            msg = f"{name} tax deleted"
            
        if "allowance" in L:
            name = L[2]
            query =  f"delete from allowances where name = '{name}'"
            cursor.execute(query)
            con.commit()
            print(f"{name} allowance deleted")
            msg = f"{name} allowance deleted"
        

    if "show" in L:
            if("employees" in L):
                print("showing employees")
                cursor.execute("select * from emp")
                records = cursor.fetchall()
                res = 'ID  Name  Salary\n\n'
                for row in records:
                    res+=f"{row[0]}   {row[1]}  {row[2]}\n"
                return res
                # table = PrettyTable(["ID", "Name","Base Salary"])
                # for row in records:
                #     print("adding row")
                #     # res+=f"{row[0]}   {row[1]}  {row[2]}\n"
                #     table.add_row(row)
                # print(table)    
                # return str(table)
            if("taxes" in L):
                print("showing taxes")
                cursor.execute("select * from taxes")
                records = cursor.fetchall()
                res = 'Tax name (Percentage)\n\n'
                for row in records:
                    res+=f"{row[0]} Tax ({row[1]}%)\n"
                return res
                # table = PrettyTable(["Tax name", "Percentage"])
                # for row in records:
                #     print("adding row")
                #     # res+=f"{row[0]}   {row[1]}  {row[2]}\n"
                #     table.add_row(row)
                # print(table)    
                # return str(table)
            if("allowances" in L):
                print("showing allowances")
                cursor.execute("select * from allowances")
                records = cursor.fetchall()
                res = 'Allowance name (Percentage)\n\n'
                for row in records:
                    res+=f"{row[0]} Allowance ({row[1]}%)\n"
                return str(res)
                # table = PrettyTable(["Allowance name", "Percentage"])
                # for row in records:
                #     print("adding row")
                #     # res+=f"{row[0]}   {row[1]}  {row[2]}\n"
                #     table.add_row(row)
                # print(table)    
                # return str(table)

    return msg