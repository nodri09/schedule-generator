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

# Arrange sets for each month
january = [[], []]

january[0].append("Something")

for i in set_1:

    if "2021.01" == str(i):
        january[0].append(i)

for i in january:
    print(i)