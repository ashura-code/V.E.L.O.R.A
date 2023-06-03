import pyautogui


def min_all():
    pyautogui.hotkey('super', 'm')



def vol_up(n=1):
    for i in range(0, n):
        pyautogui.hotkey('volumeup')

def vol_down(n=1):
    for i in range(0, n):
        pyautogui.hotkey('volumedown')




def restore_min():
    pyautogui.hotkey('super', 'shift', 'm')


def min_top():
    pyautogui.hotkey('super', 'down', 'down')


def os_search():
    pyautogui.hotkey('super', 's')


def task_manager():
    pyautogui.hotkey('ctrl', 'shift', 'esc')


def tab_shift():
    pyautogui.hotkey('alt', 'tab')


def display_options():
    pyautogui.hotkey('super', 'k')


def lock_screen():
    min_all()
    pyautogui.typewrite('alt', 'f4')


# lock_screen()
def fullminscr():
    pyautogui.hotkey('f11')


def hide_show_scr():
    pyautogui.hotkey('super', 'd')


def refresh():
    pyautogui.hotkey('f5')


def settings():
    pyautogui.hotkey('super', 'i')


def clipboard():
    pyautogui.hotkey('super', 'v')


def dashboard():
    pyautogui.hotkey('super', 'tab')


def magnifier():
    pyautogui.hotkey('super', '=')


# text actions

def select_all():
    pyautogui.hotkey('ctrl', 'a')


def copy():
    pyautogui.hotkey('ctrl', 'c')


def paste():
    pyautogui.hotkey('ctrl', 'v')


def cut():
    pyautogui.hotkey('ctrl', 'x')


def undo():
    pyautogui.hotkey('ctrl', 'z')


def redo():
    pyautogui.hotkey('ctrl', 'y')


def rename():
    pyautogui.hotkey('f2')


# browser tools

def browser_next():
    pyautogui.hotkey('alt', 'right')


def browser_prev():
    pyautogui.hotkey('alt', 'left')
