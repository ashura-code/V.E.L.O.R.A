import pyautogui


def qucik_settings():
         pyautogui.hotkey('super','a')


def widgets():
    pyautogui.hotkey('super', 'w')

def notifications():
    pyautogui.hotkey('super', 'n')

def calendar():
    pyautogui.hotkey('super', 'n')

# desktop movements
def new_desktop():
    pyautogui.hotkey('super','ctrl','d')

def shift_next_desktop():
    pyautogui.hotkey('super','ctrl','right')

def shift_pervious_desktop():
    pyautogui.hotkey('super','ctrl','left')

def delete_desktop(): # it delete the current desktop
    pyautogui.hotkey('super','ctrl','f4')

def playpause():
    pyautogui.hotkey('playpause')

def volumemute():
    pyautogui.hotkey('volumemute')


def pageup():
    pyautogui.hotkey('pageup')

def pagedown():
    pyautogui.hotkey('pagedown')

def print():
    pyautogui.hotkey('print')

import subprocess

def open_command_prompt():
    # Open command prompt
    subprocess.run(["cmd"])

def backspace():  #useless
    pyautogui.hotkey('backspace')

def modechange(): #useless
    pyautogui.hotkey('modechange')
modechange()


    #only half done
def snap_layouts():
    pyautogui.hotkey('super', 'z')
