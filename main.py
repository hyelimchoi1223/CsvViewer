import PySimpleGUI as gui

input_path_layout=[[gui.Text("Insert Your CSV Path")], [gui.Input(key='-INPUT-'), gui.Button('Insert', size=(5,1))]]
output_path_layout = [[gui.Text(size=(40,1), key='-OUTPUT-')]]
layout = [[gui.Column(input_path_layout)],
          [gui.Column(output_path_layout)]]

window = gui.Window('Window Title', layout) 
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == gui.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    if event == 'Insert':
        window['-OUTPUT-'].update('Path :  ' + values['-INPUT-'])    
window.close()           