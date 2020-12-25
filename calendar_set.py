import calendar as cl

year_day = [] # The beginning of each set

set_days = [] # Days that set wil

set_1 = []
set_2 = []

# Set new calendar
cal= cl.Calendar()

# Iterate through every month
# Save every day in the list "year_day"
for i in range(1, 13):
    for x in cal.itermonthdates(2021, i):
    	year_day.append(x)

# With interval of 3 insert days into set calculator
for i in range(1, len(year_day), 3):
    set_days.append(year_day[i])

for i in range(len(year_day)):
    for j in range(0, len(set_days), 2):
        if set_days[j] == year_day[i]:
            set_1.append(year_day[i-2])
            set_1.append(year_day[i-1])
            set_1.append(year_day[i])
    for j in range(1, len(set_days), 2):
        if set_days[j] == year_day[i]:
            set_2.append(year_day[i-2])
            set_2.append(year_day[i-1])
            set_2.append(year_day[i])

set_1 = list(dict.fromkeys(set_1))
set_2 = list(dict.fromkeys(set_2))

# Arrange sets for each month
january = [[], []]
february = [[], []]
march = [[], []]
april = [[], []]
may = [[], []]
june = [[], []]
july = [[], []]
august = [[], []]
september = [[], []]
october = [[], []]
november = [[], []]
december = [[], []]

for i in set_1:
    if "2021-01" in str(i):
        january[0].append(i)
    elif "2021-02" in str(i):
        february[0].append(i)
    elif "2021-03" in str(i):
        march[0].append(i)
    elif "2021-04" in str(i):
        april[0].append(i)
    elif "2021-05" in str(i):
        may[0].append(i)
    elif "2021-06" in str(i):
        june.append(i)
    elif "2021-07" in str(i):
        july.append(i)
    elif "2021-08" in str(i):
        august.append(i)
    elif "2021-09" in str(i):
        september.append(i)
    elif "2021-10" in str(i):
        october.append(i)
    elif "2021-11" in str(i):
        november.append(i)
    elif "2021-12" in str(i):
        december.append(i)

for i in january:
    i = str(i)

# TODO: sort the list so that days in month follow the sequence
