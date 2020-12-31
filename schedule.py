"""
Schedule Generating file
Created by Gelovani Nodar
"""


import openpyxl as xl
from openpyxl.utils import get_column_letter, column_index_from_string
from set_calc import yeardays, get_shiftset, Manager
from sys import argv, exit

if len(argv) == 2:
    if argv[1].endswith('xlsx'):
        print(f"Opening the file: {argv[1]}")
    else:
        print("Incorrect file extention")
        exit()
else:
    print("Something went wrong. Cannot open the file.")
    exit()

# Transfer data from Excel file
# Open Excel Workbook
wb = xl.load_workbook(argv[1]) # data_only=True

# Open Active worksheet
sheet = wb.active

managers = []

max_row = sheet.max_row

for row in range(2, max_row + 1):
    name = sheet['A' + str(row)].value
    shift_type = sheet['B' + str(row)].value
    mset = sheet['C' + str(row)].value
    email = sheet['D' + str(row)].value

    manager = Manager(name, shift_type, mset, email)

    managers.append(manager)


year = 2021
month = 2

# print("\nJan.'21, Set 1")
# print([str(day) for day in yeardays(year) if day.month == month and get_shiftset(day)=="Set 1"])
# print("Jan.'21, Set 2")
# print([str(day) for day in yeardays(year) if day.month == month and get_shiftset(day)=="Set 2"])

for manager in managers:
    for day in yeardays(year):
        if day.month == month and get_shiftset(day) == "Set 1" and manager.mset == 1:
            manager.shifts.append(day)
        elif day.month == month and get_shiftset(day) == "Set 2" and manager.mset == 2:
            manager.shifts.append(day)

counter = 0
for manager in managers:
    for i in manager.shifts:
        counter += 1

for manager in managers:
    for shift in manager.shifts:
        x = str(shift)
        shift = x.replace("-", "/")

for manager in managers:
    for i in range(len(manager.shifts)):
        manager.shifts[i] = str(manager.shifts[i]).replace("-", "/")

wb1 = xl.load_workbook('team_file.xlsx')
print(f"Opening file: {str(wb1)}")

tsheet = wb1['Shifts']

# TODO
# Write data to cells. What data?
# Managers info, for each date they work; each date should be on a new line
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


wb1.save('team_file.xlsx')
