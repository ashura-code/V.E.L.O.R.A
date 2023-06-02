# XQg01EqN8xd0kKl3o08XFvSXvXs0yfXdRFj_9XhXJNt6i2Y7jjOz2GVxoNogBiLmVsFgmw

from bardapi import Bard
import os

os.environ['_BARD_API_KEY']="XQg01EqN8xd0kKl3o08XFvSXvXs0yfXdRFj_9XhXJNt6i2Y7jjOz2GVxoNogBiLmVsFgmw."

answer = Bard().get_answer("what is weather in vellore")['content']
print(answer)