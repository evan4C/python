import PySimpleGUI as sg
from diff_finder_functions import diff_finder

sg.theme('DarkAmber')

layout = [[sg.Text('Enter 2 files to compare')],
          [sg.Text('File 1', size=(8, 1)), sg.Input(key='-file01-'), sg.FileBrowse()],
          [sg.Text('File 2', size=(8, 1)), sg.Input(key='-file02-'), sg.FileBrowse()],
          [sg.Button('Compare'), sg.Button('Exit')]]

window = sg.Window('File Compare', layout)

while True:
    event, values = window.read()

    if event is None or event == 'Exit':
        break
    if event == 'Compare':
        diff_finder(values['-file01-'], values['-file02-'])

window.close()
