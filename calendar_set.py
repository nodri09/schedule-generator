import calendar as cl

year_day = [] # List of all days in a year

set_days = [] # The beginning of each set

set_1 = []
set_2 = []

# Set new calendar
cal= cl.Calendar()

# Iterate through every month
# Save every day in the list "year_day"
for i in range(1, 13):
    for x in cal.itermonthdates(2021, i):
    	year_day.append(x)

# With interval of 3 insert days into set_days list
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

# Create dictionary of month, with two key's only
# Key 1 will be "set 1", the list of the month days that are in set 1
# key 2 will be "set 2", the list of the month days that are in set 2
january = {
    "set 1": [],
    "set 2": []
}
february = {
    "set 1": [],
    "set 2": []
}
march = {
    "set 1": [],
    "set 2": []
}
april = {
    "set 1": [],
    "set 2": []
}
may = {
    "set 1": [],
    "set 2": []
}
june = {
    "set 1": [],
    "set 2": []
}
july = {
    "set 1": [],
    "set 2": []
}
august = {
    "set 1": [],
    "set 2": []
}
september = {
    "set 1": [],
    "set 2": []
}
october = {
    "set 1": [],
    "set 2": []
}
november = {
    "set 1": [],
    "set 2": []
}
december = {
    "set 1": [],
    "set 2": []
}

# For each set of the spesific month update the list of days
# Update set 1 of every month
for i in set_1:
    if "2021-01" in str(i):
        january["set 1"].append(i)
    elif "2021-02" in str(i):
        february["set 1"].append(i)
    elif "2021-03" in str(i):
        march["set 1"].append(i)
    elif "2021-04" in str(i):
        april["set 1"].append(i)
    elif "2021-05" in str(i):
        may["set 1"].append(i)
    elif "2021-06" in str(i):
        june["set 1"].append(i)
    elif "2021-07" in str(i):
        july["set 1"].append(i)
    elif "2021-08" in str(i):
        august["set 1"].append(i)
    elif "2021-09" in str(i):
        september["set 1"].append(i)
    elif "2021-10" in str(i):
        october["set 1"].append(i)
    elif "2021-11" in str(i):
        november["set 1"].append(i)
    elif "2021-12" in str(i):
        december["set 1"].append(i)

# Update the set 2 of every month
for i in set_2:
    if "2021-01" in str(i):
        january["set 2"].append(i)
    elif "2021-02" in str(i):
        february["set 2"].append(i)
    elif "2021-03" in str(i):
        march["set 2"].append(i)
    elif "2021-04" in str(i):
        april["set 2"].append(i)
    elif "2021-05" in str(i):
        may["set 2"].append(i)
    elif "2021-06" in str(i):
        june["set 2"].append(i)
    elif "2021-07" in str(i):
        july["set 2"].append(i)
    elif "2021-08" in str(i):
        august["set 2"].append(i)
    elif "2021-09" in str(i):
        september["set 2"].append(i)
    elif "2021-10" in str(i):
        october["set 2"].append(i)
    elif "2021-11" in str(i):
        november["set 2"].append(i)
    elif "2021-12" in str(i):
        december["set 2"].append(i)

