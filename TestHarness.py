# ------------------------------------------------------------------------ #
# Title: Assignment 09 - Testing Harness
# Description: Testing Harness module for Assignment 09

# ChangeLog (Who,When,What):
# ALi,Dec. 15, 2020,Created started script
# ------------------------------------------------------------------------ #

# Add Person class
# Add Employee class
# Add FileProcessor class
# Add EmployeeIO class

if __name__ == "__main__":
    from DataClasses import Person as P
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Add Person class
print("Testing Person class")
lstTable = []
objP1 = P("Andrew", "Li")
objP2 = P("Randal", "Root")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))
print("End of Person class.")
print("***--------------------------------***")
print()

# Add Employee class
print("Testing Employee class")
lstTable = []
objEmp1 = Emp(1, "Andrew", "Li")
objEmp2 = Emp(2, "Randal", "Root")
lstTable = [objEmp1, objEmp2]
for row in lstTable:
    print(row.to_string(), type(row))
print("End of Employee class.")
print("***--------------------------------***")
print()

# Add FileProcessor class
print("Testing FileProcessor class")
Fp.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string(), type(row))
print("End of FileProcessor class.")
print("***--------------------------------***")
print()

# Add EmployeeIO class
print("Testing EmployeeIO class")
Eio.print_menu_item()
Eio.print_current_list_items(lstTable)
print(Eio.input_employee_data())
print(Eio.input_menu_options())
print("End of EmployeeIO class.")
print("***--------------------------------***")
print()