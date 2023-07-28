import PySimpleGUI as sg
from window_close import *

WINDOW_SIZE = 500,250


layout = [
    [sg.Text("Choose an option below")], 
    [sg.Button(button_text="Edit Profile",tooltip="Change height, weight, or diet model")], 
    [sg.Button(button_text="Make an Entry",tooltip="Add food or drink")], 
    [sg.Button(button_text="Daily Dashboard", tooltip="See how today is progressing")], 
    [sg.Button(button_text="Historical Data",tooltip="Discover trends in your eating habits")], 
    [sg.Button(button_text="End Day",tooltip="Mark eating and drinking as done for today")],
    [sg.Button("Exit")]
    ]

# Create the window
window = sg.Window("FoodTracker", layout, finalize=True, 
                    relative_location=(0,0), size=WINDOW_SIZE)


# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the Exit button
    if event == "Exit" or event == sg.WIN_CLOSED:
        close_window(window)
        break
    """
    elif event == "Edit Profile":
        # take user to profile screen
    elif event == "Make an Entry":
        # take user to entry menu 
    elif event == "Daily Dashboard": 
        # take user to summary menu
    elif event == "Historical Data":
        # take user to historical data menu
    elif event == "End Day"
        # take user to confirmation screen
    """

