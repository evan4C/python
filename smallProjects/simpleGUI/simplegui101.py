import PySimpleGUI as sg

sg.theme('Dark Blue 3')

layout = [
    [sg.Text('file name')],
    [sg.Input(), sg.FileBrowse()],
    [sg.OK(), sg.Cancel()]
]

window = sg.Window('window title', layout)

event, values = window.Read()
window.close()

