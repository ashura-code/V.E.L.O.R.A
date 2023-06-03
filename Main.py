from bard import prompt
# print(prompt("what is today's weather?"))
# import insta
from functions import *


while True:
    q = input("Type a command: ")

    if q == "exit" or q == "quit" or q == "bye":
        break

    elif "minimize all windows" in q:
        min_all()

    elif "minimize top window" in q:
        min_top()

    elif "increase volume" in q or "turn up the volume" in q:
        vol_up()

    elif "decrease volume" in q or "turn down the volume" in q:
        vol_down()

    elif "restore minimized windows" in q:
        restore_min()

    elif "search operating system" in q:
        os_search()

    elif "open task manager" in q:
        task_manager()

    elif "switch tab" in q or "change tab" in q:
        tab_shift()

    elif "open display options" in q or "open display settings" in q:
        display_options()

    elif "lock the screen" in q:
        lock_screen()

    elif "enter full screen" in q or "maximize the window" in q:
        fullminscr()

    elif "show desktop" in q or "hide desktop" in q:
        hide_show_scr()

    elif "refresh the page" in q:
        refresh()

    elif "open settings" in q or "open system settings" in q:
        settings()

    elif "paste from clipboard" in q:
        clipboard()

    elif "open dashboard" in q or "open app switcher" in q:
        dashboard()

    elif "enable magnifier" in q or "zoom in" in q:
        magnifier()

    elif "select all text" in q:
        select_all()

    elif "copy to clipboard" in q:
        copy()

    elif "paste from clipboard" in q:
        paste()

    elif "cut selected text" in q:
        cut()

    elif "undo the last action" in q:
        undo()

    elif "redo the last action" in q:
        redo()

    elif "rename file" in q:
        rename()

    elif "go to next page" in q or "navigate to next page" in q:
        browser_next()

    elif "go to previous page" in q or "navigate to previous page" in q:
        browser_prev()
    
    else:
        print(prompt(q))

