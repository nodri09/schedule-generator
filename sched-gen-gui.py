import PySimpleGUI as sg
from schedule import main

sg.theme('Dark Blue 17')    # Keep things interesting for your users

layout = [
    [sg.Text('Schedule Generator', font=("Helvetica", 20))],
    [sg.Text('='*65)],
    [sg.Text('Choose Managers Excel File')],
    [sg.In(key='-MANAGER_FILE-'), sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),))],
    [sg.Text('Choose Teams File')],
    [sg.In(key='-TEAMS_FILE-'), sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),))],
    [sg.Text('-'*50)],
    [sg.Text('Choose Year', size=(15, 1), font=('Courier', 14)), sg.Input(key='-YEAR-', size=(4, 1))],
    [sg.Text('Choose Month', size=(15, 1), font=('Courier', 14)), sg.Input(key='-MONTH-', size=(4, 1))],
    [sg.Button('Calculate', key="-CALCULATE-"), sg.Exit()]
]

window = sg.Window('Window that stays open', layout)

while True: # The Event Loop
    event, values = window.read()

    managerFile = values['-MANAGER_FILE-']
    teamsFile = values['-TEAMS_FILE-']
    yearInput = int(values['-YEAR-'])
    monthInput = int(values['-MONTH-'])

    if event == '-CALCULATE-':
        main(managerFile, yearInput, monthInput, teamsFile)

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
