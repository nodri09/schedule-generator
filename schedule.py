"""
Schedule Generating file
Created by Gelovani Nodar
"""
import openpyxl as xl
from openpyxl.utils import get_column_letter, column_index_from_string
from set_calc import yeardays, get_shiftset, Manager, printff
from sys import argv, exit

if len(argv) == 3:
    if argv[1].endswith('xlsx') and argv[2].endswith('xlsx'):
      printff("Starting the program...")
    else:
      print("Incorrect file extention")
      exit()
else:
    print("Something went wrong. Cannot open the file.")
    exit()

# Transfer data from Excel file
# Open Excel Workbook
print(f"Opening file: {argv[1]}")
try:
  wb = xl.load_workbook(argv[1])
except OSError:
  print("Cannot open file")
  exit()


# Open Active worksheet
print("Opening active worksheet...")
sheet = wb.active

managers = []

max_row = sheet.max_row

print("Retreiving information from columns...")
for row in range(2, max_row + 1):
    name = sheet['A' + str(row)].value
    shift_type = sheet['B' + str(row)].value
    mset = sheet['C' + str(row)].value
    email = sheet['D' + str(row)].value

    manager = Manager(name, shift_type, mset, email)

    managers.append(manager)

print("Dictate the year: ")
user_year = int(input())

while False:
  if user_year == None or type(user_year) != int():
    False
  else:
    True

print("Dictate the month: ")
user_month = int(input())

while False:
  if user_month == None or type(user_month) != int():
    False
  else:
    True

year = user_year
month = user_month

# print("\nJan.'21, Set 1")
# print([str(day) for day in yeardays(year) if day.month == month and get_shiftset(day)=="Set 1"])
# print("Jan.'21, Set 2")
# print([str(day) for day in yeardays(year) if day.month == month and get_shiftset(day)=="Set 2"])

print("Generating set days for each Manager")
for manager in managers:
    for day in yeardays(year):
        if day.month == month and get_shiftset(day) == "Set 1" and manager.mset == 1:
            manager.shifts.append(day)
        elif day.month == month and get_shiftset(day) == "Set 2" and manager.mset == 2:
            manager.shifts.append(day)

print("Translating Python Date numbers to Excel Date numbers")
for manager in managers:
    for shift in manager.shifts:
        x = str(shift)
        shift = x.replace("-", "/")

for manager in managers:
    for i in range(len(manager.shifts)):
        manager.shifts[i] = str(manager.shifts[i]).replace("-", "/")


wb1 = xl.load_workbook(argv[2])
print(f"Opening file: {argv[2]}")


tsheet = wb1['Shifts']

# Translateing managers info to excel column
print("Translateing managers info to excel column")
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

print(f"Saving {argv[2]}")
wb1.save(argv[2])

print(f"Closing {argv[1]}")
wb.close()

print(f"Closing {argv[2]}")
wb1.close()