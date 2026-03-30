from datetime import datetime

# This function writes comma-separated data to a CSV file.
def insertData(path, data):
    try:
        with open(path, 'a') as file:
            file.write(data + "\n")
        return True
    except:
        print("Error: Unable to write to file.")
        return False

# This function reads and displays the contents of a CSV file.
def viewData(path):
    try:
        print(f"Reading from file: {path}")
        with open(path, 'r') as file:
            for line in file:
                print(line.strip())
    except:
        print("Error: Unable to read file.")

# This function converts Fahrenheit to Celsius.
def convertData(data):
    converted_value = (data - 32) * 5 / 9
    return converted_value

# This function gets user input, converts the value, and saves the data to a CSV file.
def getInput():
    path = "C:\\PythonFiles\\ZooData.csv"
    entries = int(input("How many entries are being entered? "))

    for i in range(entries):
        entry_date = input("Enter the date: ")
        value = float(input("Enter the temperature in Fahrenheit: "))

        # convertData(data) requires a numerical value and returns the converted Celsius value.
        converted_value = convertData(value)

        data = f"{entry_date},{value},{converted_value:.2f}"

        try:
            if insertData(path, data):
                print(f"The following data was saved at {datetime.now()}: {data}.")
        except:
            print("Error: Unable to save data.")

# Display application name
student_id = input("Enter your Student ID: ")
print(f"{student_id}'s Spreadsheet Automation Menu")

# Store menu options
menu_options = [
    "1. Input Data",
    "2. View Current Data",
    "3. Generate Report"
]

# Print menu options via loop
for item in menu_options:
    print(item)

# Retrieve menu selection
option = int(input("Select a menu option (1-3): "))

# Get current date and time
current_time = str(datetime.now())

# Previous error-checking code
if option == 1:
    print(f"You selected menu option 1 at {current_time}")
elif option == 2:
    print(f"You selected menu option 2 at {current_time}")
elif option == 3:
    print(f"You selected menu option 3 at {current_time}")
else:
    print("Error: Invalid choice selected.")

# Menu flow control
if option == 1:
    getInput()
elif option == 2:
    viewData("ZooData.csv")
else:
    print("Error: The chosen functionality is not implemented yet")
