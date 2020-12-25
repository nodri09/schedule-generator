# Schedule Generating file
# Created by Gelovani Nodar for Evolution


import openpyxl as xl
from openpyxl.utils import get_column_letter, column_index_from_string
from calendar_set import set_1, set_2

# Transfer data from Excel file
# Open Excel Workbook
wb = xl.load_workbook('Managers.xlsx') # data_only=True

# Open Active worksheet
sheet = wb.active

class Manager():

    def __init__(self, name, shift_type, mset):
        self.name = name
        self.shift_type = shift_type
        self.mset = mset

managers = []

max_row = sheet.max_row

for row in range(2, max_row + 1):
    name = sheet['A' + str(row)].value
    shift_type = sheet['B' + str(row)].value
    mset = sheet['C' + str(row)].value

    manager = Manager(name, shift_type, mset)

    managers.append(manager)


"""
print("LETS SEE IF IT WORKS")
for i in managers :
    print(f"{i.name} | {i.shift_type} | {i.mset}")

"""
