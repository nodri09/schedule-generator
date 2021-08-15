# schedule-generator
This is schedule generator for shift and set based employees


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
Functions.py file stores custom functions. Basically there are two functions defined there and a class.

yeardays function:
```
def yeardays(year):
    """Generate all days of the year."""
    for d in range(365):
        yield dt.date(year,1,1) + dt.timedelta(days=d)
```

get_shift_set function:
```
def get_shiftset(d):
    """Determine if a day belongs to Set 1 or 2."""
    set_day = (d - dt.date(d.year,1,1)).days % 6
    return "Set 1" if set_day < 3 else "Set 2"
```


## How can you start with thet project. 
