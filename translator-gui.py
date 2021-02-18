import PySimpleGUI as sg

from translator import *

sg.theme('Dark Blue')

layout = [
    [sg.Text('Translator App', font=("Helvetica", 20))],
    [sg.Text('Schedule File')],
    [sg.In(key='-EXCEL_FILE-'), sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),))],
    [sg.Text('Teams File')],
    [sg.In(key='-TEAM_FILE-'), sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),))],
    [sg.Button('Generate'), sg.Button('Transfer'), sg.Exit()]
]

window = sg.Window('Translator App', layout, grab_anywhere=True)

while True:
    event, values = window.read()

    excel = values['-EXCEL_FILE-']
    team_file = values['-TEAM_FILE-']


    if event == 'Generate':
        managers = main(excel)
        sg.popup_quick_message('Generated')

    managers = main(excel)

    if event == 'Transfer':
        translator(team_file, managers)
        sg.popup_quick_message('Transferred')
        break

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
