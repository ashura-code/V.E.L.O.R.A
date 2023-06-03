from bard import prompt
# print(prompt("what is today's weather?"))
# import insta
from functions import *

while True:
    q = input("type.. ")

    if q == "exit" or q == "quit" or q == "bye":
        break

    if "minimize all" in q:
        min_all()

    if "minimize" in q:
        min_top()

    if "increase volume" in q or "volume increase" in q or "volume up" in q:
        vol_up()

    if "decrease volume" in q or "volume decrease" in q or "volume down" in q:
        vol_down()

    if "restore windows" in q:
        restore_min()



    else:
        print(prompt(q))


