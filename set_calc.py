import datetime as dt
import time

class Manager():
    """Class of each manager transferred from excel file"""

    def __init__(self, name):
        """
        The Manager has name, email, color and shifts list

        Name is a string, managers full name. Necessary for Shifts Template
        Email is a string, managers corporate email. Necessary for Shifts Template
        Color is a cell color of Manager in excel file. Needed to determine shift start time. Necessary for shifts Template
        Shifts list is a list of dictionary containing role and date of the manager's shift. Necessary for Shifts Template.
        """
        self.name = name
        self.email = ""
        self.color = ""
        self.shifts = []

def yeardays(year):
    """Generate all days of the year."""
    for d in range(365):
        yield dt.date(year,1,1) + dt.timedelta(days=d)

def get_shiftset(d):
    """Determine if a day belongs to Set 1 or 2."""
    set_day = (d - dt.date(d.year,1,1)).days % 6
    return "Set 1" if set_day < 3 else "Set 2"

def printff(text):
  for i in text:
    time.sleep(0.05)
    print(i, end='', flush=True)

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
