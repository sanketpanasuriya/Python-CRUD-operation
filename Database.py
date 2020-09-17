import sqlite3
class Queries:
    con = ""
    cursor = ""
    def __init__(self):
        try:
            self.con = sqlite3.connect('Employee.db')
            self.cursor = self.con.cursor()
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS employee(
                ID INTEGER,
                emp_no TEXT NOT NULL UNIQUE,
                first_name text,
                last_name text,
                email text,
                phone INTEGER,
                salary INTEGER,
                field text,
                year_of_enroll DATETIME NOT NULL DEFAULT (strftime('%Y-%m-%d', 'now', 'localtime')),
                PRIMARY KEY("ID" AUTOINCREMENT)
            )''')
            self.con.commit()
        except:
            pass
    
    def insert(self,emp_no,first_name,last_name,email,phone,salary,field):
        try:
            query = "insert into employee (emp_no,first_name,last_name,email,phone,salary,field) values(?,?,?,?,?,?,?)"
            Tuple = (emp_no,first_name,last_name,email,phone,salary,field)
            self.cursor.execute(query,Tuple)
            self.con.commit()
            print("Data insert successfully")
        except:
            print("Something went wrong")
    
    def DisplayAll(self):
        try:
            sqlite_select_query = """SELECT * from employee"""
            self.cursor.execute(sqlite_select_query)
        
            records = self.cursor.fetchall()
            print("Total rows are:  ", len(records))
            if(len(records)>0):
                print()
                for row in records:
                    print("No: ",row[0])
                    print("Employee no.: ", row[1])
                    print("Name: ", row[2],row[3]) 
                    print("Email: ", row[4])
                    print("phone: ", row[5])
                    print("Salary: ", row[6])
                    print("Field: ",row[7])
                    print("Date of enroll: ", row[8])
                    print("\n")
            else :
                print("Table is empty")

            self.cursor.close()

        except sqlite3.Error as error:
            print("Failed to read data from employee table", error)
        finally:
            if (self.con):
                self.con.close()

    def DisplayFirst(self):
        try:
            fname = input("Enter firstname you want to find: ")
            sqlite_select_query = """SELECT * from employee where first_name = (?)"""
            self.cursor.execute(sqlite_select_query,(fname,))
        
            records = self.cursor.fetchall()
            print("Total rows are:  ", len(records))
            if(len(records)>0):
                print()
                for row in records:
                    print("No: ", row[0])
                    print("Employee no.: ", row[1])
                    print("Name: ", row[2],row[3]) 
                    print("Email: ", row[4])
                    print("phone: ", row[5])
                    print("Salary: ", row[6])
                    print("Field: ",row[7])
                    print("Year of enroll: ", row[8])
                    print("\n")
            else :
                print("first name is not exits")

            self.cursor.close()

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if (self.con):
                self.con.close()
    
    def update_salary_by_emp_id(self):
        try:
            Id = input("Enter employee no you want to update salary: ")
            salary = input("How many percentage increase salary: ")
            
            Query = "UPDATE employee set salary=salary + salary*?/100 where emp_no=?"
            self.cursor.execute(Query,(salary,Id))
            self.con.commit()
            self.cursor.close()
            print("Data update successfully")
        except sqlite3.Error as error:
            print("Failed to update data from employee table", error)
        finally:
            if (self.con):
                self.con.close()
        
    def update_All_employee_salary(self):
        try:
            salary = input("How many percentage increase salary: ")
            Query = "UPDATE employee set salary=salary+salary*?/100"
            self.cursor.execute(Query,(salary,))
            self.con.commit()
            self.cursor.close()
            print("Data update successfully")
        except sqlite3.Error as error:
            print("Failed to update data from employee table", error)
        finally:
            if (self.con):
                self.con.close()

    def Delete(self):
        try:
            enrollment = input("Enter employee no. you want to delete data :")
            Query = "DELETE from employee where emp_no = ?"
            self.cursor.execute(Query,(enrollment,))
            self.con.commit()
            self.cursor.close()
            print("Data deleted successfully")
        except sqlite3.Error as error:
            print("Failed to delete data from employee table", error)
        finally:
            if (self.con):
                self.con.close()