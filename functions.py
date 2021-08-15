"""
Functions that were created specifically for schedule-generator program.
"""

import datetime as dt
import time

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
        self.role = []

def yeardays(year):
    """Generate all days of the year."""
    for d in range(365):
        yield dt.date(year,1,1) + dt.timedelta(days=d)

def get_shiftset(d):
    """Determine if a day belongs to Set 1 or 2."""
    set_day = (d - dt.date(d.year,1,1)).days % 6
    return "Set 1" if set_day < 3 else "Set 2"

# show all days of 2021 and their sets
#print("Sets of 2021")
#for doy in yeardays(2021):
#    print(f"{doy}: {get_shiftset(doy)}")

# show sets for February 2021
#year = 2021
#month = 2
#print("\nFeb.'21, Set 1")
#print([str(day) for day in yeardays(year) if day.month == month and get_shiftset(day)=="Set 1"])
#print("Feb.'21, Set 2")
#print([str(day) for day in yeardays(year) if day.month == month and get_shiftset(day)=="Set 2"])
