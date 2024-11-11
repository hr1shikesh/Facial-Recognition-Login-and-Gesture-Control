import pyautogui

def adjust_brightness(level):
    pyautogui.press("brightnessup" if level > 0 else "brightnessdown")

def adjust_volume(level):
    pyautogui.press("volumeup" if level > 0 else "volumedown")
