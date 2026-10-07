'''
Write a python program 
- read a employee details(name,age,cost) from <STDIN>
- using print() - display employee details.
- calculate emp basic salary with 18% tax and display the tax
- calculate tax + basic salary and display the total salary(including tax)
'''
elogin_status = True

ename = input("Enter employee name: ")

eage = input(f"Enter {ename} age: ")

ecost = input(f"Enter {ename} basic salary: ")

tax = float(ecost) * 0.18 
gs = tax + float(ecost)

print(f'''Employee Name:{ename}
---------------------------------------
{ename} Age is:{eage}
---------------------------------------
{ename} Basic Salary is:{ecost}
---------------------------------------
{ename} Login Status is:{elogin_status}
-----------------------------------------
Tax is:{tax}
-----------------------------------------
Total Salary is:{gs}
----------------------------------------''')