import tkinter as tk
import random


# definition of the functions to call
def test_1():
    print("test 1")
    # value = int(lbl_value["text"])
    # lbl_value["text"] = f"{value + 1}"


def test_2():
    print("test 2")
    # value = int(lbl_value["text"])
    # lbl_value["text"] = f"{value - 1}"

def roll():
    lbl_result["text"] = str(random.randint(1, 6))

# definition of the window
window = tk.Tk()
window.title("AFK Remover")
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=500, weight=1)

# definition of object
# txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_mouse = tk.Button(fr_buttons, text="Launch the mouse util", command=test_1)
btn_keyboard = tk.Button(fr_buttons, text="Launch the keyboard util", command=test_2)
btn_mix = tk.Button(fr_buttons, text="Launch the mix", command=roll)
lbl_result = tk.Label()


# definition of the grid 
btn_mouse.grid(row=0, column=1, sticky="nsew")
btn_keyboard.grid(row=1, column=1, sticky="nsew")
btn_mix.grid(row=2, column=1, sticky="nsew")

fr_buttons.grid(row=0, column=1, sticky="nsew")
lbl_result.grid(row=3, column=1)
# txt_edit.grid(row=0, column=1, sticky="nsew")




window.mainloop()


# Create an event handler
# def handle_keypress(event):
#     """Print the character associated to the key pressed"""
#     print(event.char)

# def handle_click(event):
#     print("The button was clicked!")

# Bind keypress event to handle_keypress()
# window.bind("<Key>", handle_keypress)
# button_mouse.bind("<Button-1>", handle_click)
# button_keyboard.bind("<Button-1>", handle_click)
# button_mix.bind("<Button-1>", handle_click)


# window.mainloop()
# # Run the event loop
# while True:
#     # If events_list is empty, then no events have occurred and you
#     # can skip to the next iteration of the loop
#     if events_list == []:
#         continue

#     # If execution reaches this point, then there is at least one
#     # event object in events_list
#     event = events_list[0]
    
#     # If event is a keypress event object
#     if event.type == "keypress":
#         # Call the keypress event handler
#         handle_keypress(event)