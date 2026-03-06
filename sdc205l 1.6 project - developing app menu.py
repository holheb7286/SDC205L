from datetime import datetime

# Display application name
student_id = input("Enter your Student ID: ")
print(f"{student_id}'s Spreadsheet Automation Menu")

# Display menu options
print("1. Input Data")
print("2. View Current Data")
print("3. Generate Report")

# The next line retrieves the inputted option
# and stores into the variable called option.
option = int(input("Select a menu option (1-3): "))

# Get current date and time
current_time = str(datetime.now())

# Display selected option
if option == 1:
    print(f"You selected menu option 1 at {current_time}")

elif option == 2:
    print(f"You selected menu option 2 at {current_time}")

elif option == 3:
    print(f"You selected menu option 3 at {current_time}")

else:
    print("Invalid option selected.")

