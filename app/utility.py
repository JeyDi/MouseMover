import pyautogui

def setupAutoGui():
    pyautogui.PAUSE = 1
    pyautogui.FAILSAFE = False
    return True

def keyboard_movements(exec_program):
    pass

def mouse_movements(exec_program):
    #get the size of the pc
    width, height = pyautogui.size()
    print(f'Screen Width: {width}')
    print(f'Screen Height: {height}')

    #move the mouse in circle
    movements = 0

    try:
        while exec_program:
            pyautogui.moveTo(100, 100, duration=0.25)
            pyautogui.moveTo(200, 100, duration=0.25)
            pyautogui.moveTo(200, 200, duration=0.25)
            pyautogui.moveTo(100, 200, duration=0.25)
            pyautogui.click(button='right')
            pyautogui.click(button='left')
            pyautogui.click(button='left', clicks=2, interval=1)
            
            movements += 1
            print(movements)
    except KeyboardInterrupt:
        print("Mouse movements terminated")
        print(f"Moves done: {movements}")
        pass
        
    return True