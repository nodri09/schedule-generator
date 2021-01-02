"""
Schedule Generating file
Created by Gelovani Nodar
"""
import openpyxl as xl
from openpyxl.utils import get_column_letter, column_index_from_string
from set_calc import yeardays, get_shiftset, Manager, printff
from sys import argv, exit

# Check if command line arguments are 3
# Check if second and third files have 'xlsx' file extention
# If not correct any of the above, exit
if len(argv) == 3:
    if argv[1].endswith('xlsx') and argv[2].endswith('xlsx'):
      printff("Starting the program...\n")
    else:
      printff("Incorrect file extention\n")
      exit()
else:
    printff("Something went wrong. Cannot open the file.\n")
    exit()

# Transfer data from Excel file
# Open Excel Workbook
printff(f"Opening file: {argv[1]}\n")
try:
  wb = xl.load_workbook(argv[1])
except OSError:
  printff("Cannot open file\n")
  exit()


# Open Active worksheet
printff("Opening active worksheet...\n")
sheet = wb.active

# List of Manager class - All the managers in one List
managers = []

# Store amount of rows in one variable
max_row = sheet.max_row

# Transfer information from Managers excel
printff("Retreiving information from columns...\n")
for row in range(2, max_row + 1):
    name = sheet['A' + str(row)].value
    shift_type = sheet['B' + str(row)].value
    mset = sheet['C' + str(row)].value
    email = sheet['D' + str(row)].value

    # Put Retreived info into the Manager class
    manager = Manager(name, shift_type, mset, email)

    # Append every manager into the managers List
    managers.append(manager)

# Ask user to provide Year and Month
# Check to be numbers only
printff("Dictate the year:\n ")
user_year = int(input())

while False:
  if user_year == None or type(user_year) != int():
    False
  else:
    True

printff("Dictate the month:\n ")
user_month = int(input())

while False:
  if user_month == None or type(user_month) != int():
    False
  else:
    True

year = user_year
printff(f"Year is: {year}\n")
month = user_month
printff(f"Month is: {month}\n")

# print("\nJan.'21, Set 1")
# print([str(day) for day in yeardays(year) if day.month == month and get_shiftset(day)=="Set 1"])
# print("Jan.'21, Set 2")
# print([str(day) for day in yeardays(year) if day.month == month and get_shiftset(day)=="Set 2"])

# Generate set days of the given month of the given year
# Assign generated set-days to managers, which have the same set
printff("Generating set days for each Manager\n")
for manager in managers:
    for day in yeardays(year):
        if day.month == month and get_shiftset(day) == "Set 1" and manager.mset == 1:
            manager.shifts.append(day)
        elif day.month == month and get_shiftset(day) == "Set 2" and manager.mset == 2:
            manager.shifts.append(day)

"""
printff("Translating Python Date numbers to Excel Date numbers\n")
for manager in managers:
    for shift in manager.shifts:
        x = str(shift)
        shift = x.replace("-", "/")
"""

for manager in managers:
    for i in range(len(manager.shifts)):
        manager.shifts[i] = str(manager.shifts[i]).replace("-", "/")


wb1 = xl.load_workbook(argv[2])
printff(f"Opening file: {argv[2]}\n")


tsheet = wb1['Shifts']

# Translateing managers info to excel column
printff("Translateing managers info to excel column\n")
for manager in managers:
    amount = len(manager.shifts)
    tsheet.insert_rows(idx=2, amount=amount + 1)
    for row in range(2, amount + 2):
        tsheet['A' + str(row)] = manager.name
        tsheet['B' + str(row)] = manager.email
        tsheet['D' + str(row)] = manager.shifts[row - 2]
        tsheet['F' + str(row)] = manager.shifts[row - 2]

        if manager.shift_type.lower() == 'morning':
            tsheet['E' + str(row)] = '07:00'
            tsheet['G' + str(row)] = '15:00'
        elif manager.shift_type.lower() == 'afternoon':
            tsheet['E' + str(row)] = '15:00'
            tsheet['G' + str(row)] = '23:00'
        elif manager.shift_type.lower() == 'night':
            tsheet['E' + str(row)] = '23:00'
            tsheet['G' + str(row)] = '07:00'

printff(f"Saving {argv[2]}\n")
wb1.save(argv[2])

printff(f"Closing {argv[1]}\n")
wb.close()

printff(f"Closing {argv[2]}\n")
wb1.close()