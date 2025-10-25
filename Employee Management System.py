import mysql.connector
import sqlite3

conn = sqlite3.connect('employee.db')


# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",        # replace with your MySQL username
    password="425001",# replace with your MySQL password
    database="employee_db"
)
cursor = conn.cursor()

# Functions
def add_employee():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    department = input("Enter department: ")
    position = input("Enter position: ")
    salary = float(input("Enter salary: "))
    
    cursor.execute('''
    INSERT INTO employees (name, age, department, position, salary)
    VALUES (%s, %s, %s, %s, %s)
    ''', (name, age, department, position, salary))
    conn.commit()
    print("Employee added successfully!")

def view_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def update_employee():
    emp_id = int(input("Enter employee ID to update: "))
    print("Enter new details:")
    name = input("Name: ")
    age = int(input("Age: "))
    department = input("Department: ")
    position = input("Position: ")
    salary = float(input("Salary: "))
    
    cursor.execute('''
    UPDATE employees
    SET name=%s, age=%s, department=%s, position=%s, salary=%s
    WHERE id=%s
    ''', (name, age, department, position, salary, emp_id))
    conn.commit()
    print("Employee updated successfully!")

def delete_employee():
    emp_id = int(input("Enter employee ID to delete: "))
    cursor.execute("DELETE FROM employees WHERE id=%s", (emp_id,))
    conn.commit()
    print("Employee deleted successfully!")

# Menu
def menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()
    conn.close()
