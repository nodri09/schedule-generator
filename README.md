# schedule-generator
This is schedule generator for shift and set based employees.


## What the project does
Schedule-generator is a program written on Python that generates schedule of shift-based employees and outputs .xlsx template ready to be uploaded to Microsoft Teams shifts plug-in. 

External libraries used:
* OpenPyXL
* SimplePyGUI

It coninsts of following .py files:
* sched-gen-gui.py
* functions.py
* schedule.py

### sched-gen-gui.py
As the name of the file suggests it is a GUI file of a schedule-generator. It uses PySimpleGUI as a builder. It consists of a 4 input fields, calculate and exit buttons. 

![Window that stays open_2](https://user-images.githubusercontent.com/6499479/129483141-c467c628-f25f-4d7a-bc30-8fa2af49ed49.jpg)


2 out of 4 input fields take Excel file in, one of which should be .xlsx file that contains information about employees (see below).

![employees file - Excel](https://user-images.githubusercontent.com/6499479/129481895-3f9b8215-cd09-4404-82a4-79d33aff0fac.jpg)

Another one should be empty shifts template Excel file, which you can download from shifts plug-in itself. 

Rest two input fields are 'Year' and 'Month'. Year should be full 4 digits number, e.g.: 2021, 2001, 1997. Month should be integer, too. E.g.: 1, 4, 5, 10, 12.

### functions.py
Functions.py file stores custom functions. Basically there are two functions defined there and a class. It requires two libraries: datetime and time. 

**yeardays** function:
```
def yeardays(year):
    """Generate all days of the year."""
    for d in range(365):
        yield dt.date(year,1,1) + dt.timedelta(days=d)
```

**get_shiftset** function:
```
def get_shiftset(d):
    """Determine if a day belongs to Set 1 or 2."""
    set_day = (d - dt.date(d.year,1,1)).days % 6
    return "Set 1" if set_day < 3 else "Set 2"
```

**Managers()** class (As this was ment for Managers schedule in my company I have called this class Managers(), however, think of it as an **Employee()** class):
```
class Manager():
    """
    Class of manager (employee).
    self.name - Stores name of a manager (employee);
    self.shift_type - Stores shift type of an employee (Morning, Afternoon, or Night);
    self.mset - Stores set of an employee (should be 1 or 2);
    self.email - Stores email of an employee;
    self.shifts - Empty list upon creation of a new class. Later stores all the generated shift dates of an employee.
    self.role - Empty upon creation. Can be assigned later.
    """

    def __init__(self, name, shift_type, mset, email):
        self.name = name
        self.shift_type = shift_type
        self.mset = mset
        self.email = email
        self.shifts = []
        self.role = []m
```

### Schedule.py
This is where all the magic happens. Lets go one by one. It imports OpenPyXL library and functions.py

One **main** function is defined in this file that takes **manager_file, yearInput, monthInput, teams_file** as arguments. This function later is called in sched-gen-gui.py to generate schedule.

Main function first opens empleyees.xlsx file, creates Manager() class for each of the employees and stores them in a list `managers = []`. 

```
  # Transfer information from Managers excel

    for row in range(2, max_row + 1):
        name = sheet['A' + str(row)].value
        shift_type = sheet['B' + str(row)].value
        mset = sheet['C' + str(row)].value
        email = sheet['D' + str(row)].value

        # Put Retreived info into the Manager class
        manager = Manager(name, shift_type, mset, email)

        # Append every manager into the managers List
        managers.append(manager)
```

Then generates set days by given year and month. Each of this generated set days are assigned to the manager in manager.shift list. 

```
# Generate set days of the given month of the given year
user_year = yearInput

    while False:
      if user_year == None or type(user_year) != int():
        False
      else:
        True


    user_month = monthInput

    while False:
      if user_month == None or type(user_month) != int():
        False
      else:
        True

    year = user_year

    month = user_month
    
    
for manager in managers:
        for day in yeardays(year):
            if day.month == month and get_shiftset(day) == "Set 1" and manager.mset == 1:
                manager.shifts.append(day)
            elif day.month == month and get_shiftset(day) == "Set 2" and manager.mset == 2:
                manager.shifts.append(day)
```

Before transferring all of this data to the shifts template it transforms dates to the excel date format. 

```
# Change Python Date to Excel Date
    for manager in managers:
        for i in range(len(manager.shifts)):
            manager.shifts[i] = str(manager.shifts[i]).replace("-", "/")
```

Finally, it transfers all the managers with their shift dates into Shifts template file, which can be directly updloaded to the teams widget. 

```
# Transferring managers info to excel column

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
                tsheet['H' + str(row)] = '2. Blue'
            elif manager.shift_type.lower() == 'afternoon':
                tsheet['E' + str(row)] = '15:00'
                tsheet['G' + str(row)] = '23:00'
                tsheet['H' + str(row)] = '3. Green'
            elif manager.shift_type.lower() == 'night':
                tsheet['E' + str(row)] = '00:00'
                tsheet['G' + str(row)] = '07:00'
                tsheet['H' + str(row)] = '5. Pink'
```

### Contact. 
For more questions please contact me at: nodar.gelovani@outlook.com
