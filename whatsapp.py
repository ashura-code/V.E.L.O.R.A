import webbrowser as web
import pyautogui as pg
import time
import pyinputplus as pyip

#no = pyip.inputNum('enter phone no: ', greaterThan=9,lessThan=10)
no=input('Enter the number: ')
phone_no = "+91 ", no
message = input("enter the message: ")
web.open(f"https://web.whatsapp.com/send?phone={phone_no}&text={message}")
time.sleep(10)
pg.hotkey('enter')
