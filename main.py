import PySimpleGUI as gui

def make_window(csvPath):
    input_path_layout=[[gui.Text("Insert Your CSV Path")], [gui.Input(key='-INPUT-'), gui.Button('Insert', size=(5,1))]]
    output_path_layout = [[gui.Text(size=(40,1), key='-OUTPUT-', text=csvPath)]]
    layout = [[gui.Column(input_path_layout)],
          [gui.Column(output_path_layout)]]
    return gui.Window('Window Title', layout)


window = make_window("") 
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == gui.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    if event == 'Insert':
        window.close()
        window = make_window(values['-INPUT-'])        
window.close()           