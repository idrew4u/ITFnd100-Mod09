# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# ALi,Dec. 15, 2020,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #

if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
lstEmployeeTable = []
lstFileData = []

# Load data from file into a list of employee objects when script starts
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
for row in lstFileData:
        lstEmployeeTable.append(Emp(row[0], row[1], row[2].strip()))

# Show user a menu of options
while True:
    Eio.print_menu_item()

# Get user's menu option choice
    strChoice = Eio.input_menu_options()

    # Show user current data in the list of employee objects
    if strChoice == "1":
        Eio.print_current_list_items(lstEmployeeTable)
        continue

    # Let user add data to the list of employee objects
    elif strChoice == "2":
        lstEmployeeTable.append(Eio.input_employee_data())
        continue

    # let user save current data to file
    elif strChoice == "3":
        if("y" == str(input("Would you like to save data to file? (y/n): ")).strip().lower()):
            Fp.save_data_to_file("EmployeeData.txt", lstEmployeeTable)
            input("Data was saved to file. Press the [Enter] key to return to menu.")
        else:
            input("New data was NOT saved to file. Press the [Enter] key to return to menu.")
        continue

    # Let user exit program
    elif strChoice == "4":
        input("Press the [Enter] key to end program.")
        break
# Main Body of Script  ---------------------------------------------------- #
