import PySimpleGUI as gui
from CsvManager import readCsv, getHeader, getValues

def make_window(csvPath):
    input_path_layout=[[gui.Text("Insert Your CSV Path")], [gui.Input(key='-INPUT-'), gui.Button('Insert', size=(5,1))]]
    output_path_layout = [[gui.Text(size=(100,1), key='-OUTPUT-', text=csvPath, auto_size_text=True)]]
    values = ['No Data']
    header = ['Error']
    is_visible = False
    if csvPath != "":
        data = readCsv(csvPath)
        header = getHeader(data)
        values = getValues(data)
        is_visible = True
        
    
    table_layout = [[gui.Table(values, headings=header, visible=is_visible, num_rows=30, auto_size_columns=True, header_background_color='green')]]
    layout = [[gui.Column(input_path_layout)],
          [gui.Column(output_path_layout)],
          [gui.Column(table_layout)]]
    return gui.Window('Csv Viewer', layout)


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