from datetime import datetime

def convertData(data):
    """
    Converts the input value based on the spreadsheet selected.
    For this version, menu option 1 is treated as temperature in Fahrenheit,
    so the conversion is Fahrenheit to Celsius.
    """
    converted_value = (data - 32) * 5 / 9
    return converted_value

def getInput():
    entries = int(input("How many entries are being entered? "))

    for i in range(entries):
        entry_date = input("Enter the date: ")
        value = float(input("Enter the temperature in Fahrenheit: "))

        # convertData(data) requires a numerical value and returns the converted Celsius value.
        converted_value = convertData(value)

        print(f"The following was saved at {datetime.now()}:")
        print(f"Date: {entry_date}")
        print(f"Original Value: {value}")
        print(f"Converted Value: {converted_value:.2f}")
        print()

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

# Call getInput() only if option 1 was selected
if option == 1:
    getInput()
else:
    print("Error: The chosen functionality is not implemented yet")
