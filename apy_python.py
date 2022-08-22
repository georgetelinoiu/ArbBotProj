import requests
import PySimpleGUI as sg

layout = [[sg.Text("Click pe butonul de mai jos pt a genera un nr")],
        [sg.Button("Genereaza")]]

window = sg.Window("Demo", layout, element_justification='c')

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()