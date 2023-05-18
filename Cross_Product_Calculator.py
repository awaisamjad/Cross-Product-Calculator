import PySimpleGUI as sg
sg.theme('DarkTeal')

width = 200
height = width * 9/16

layout = [
    [sg.Text("Enter Values")],
    
    [sg.Text("Enter values of Vector"), sg.Input(key='ax', size = (10,1)), sg.Text("i"), sg.Input(key='ay' , size = (10,1)), sg.Text("j"), sg.Input(key='az' , size = (10,1)), sg.Text("k")],
    
    [sg.Text("Enter values of Vector"), sg.Input(key='bx' , size = (10,1)), sg.Text("i"), sg.Input(key='by' , size = (10,1)), sg.Text("j"), sg.Input(key='bz' , size = (10,1)), sg.Text("k")],
    
    [sg.Button("Calculate")],
    
    [sg.Text("", size=(0, 1), key='i'), sg.Text("i"), sg.Text("", size=(0, 1), key='j'), sg.Text("j"), sg.Text("", size=(0, 1), key='k'), sg.Text("k")],
    
    [sg.Button("Exit")]
]

margins = (width, height)
window = sg.Window(title="Cross Product Calculator",
                   layout=layout, margins=margins)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "Calculate":
        ax = float(values["ax"])
        ay = float(values["ay"])
        az = float(values["az"])
        
        bx = float(values["bx"])
        by = float(values["by"])
        bz = float(values["bz"])
        
        i = (ay * bz) - (az * by)
        j = -((ax * bz) - (az * bx))
        k = (ax * by) - (ay * bx)
        
        window["i"].update(value = i)
        window["j"].update(value = j)
        window["k"].update(value = k)

window.close()
