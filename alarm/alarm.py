import datetime
import time
import winsound
import os

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up!")
            os.system('start D:\python\despair-metal-trailer-109943.mp3')
            break
        time.sleep(1)

# Get alarm time input from the user
alarm_input = input("Enter the alarm time in HH:MM:SS format: ")
try:
    alarm_time = datetime.datetime.strptime(alarm_input, "%H:%M:%S").strftime("%H:%M:%S")
    print("Alarm set for:", alarm_time)
    set_alarm(alarm_time)
except ValueError:
    print("Invalid time format. Please use HH:MM:SS format.")

