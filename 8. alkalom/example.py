# import test_modul
"""
Namespace - honnan érem el az objektumot
"""

from asyncio.queues import QueueEmpty

# ezt sose használjátok
# minden modult elérhetővé tesz úgy,
# hogy a modul nevére kell csak hivatkoznod
from test_modul import *
from test_modul import my_func

import test_modul

my_list = "Ricsi"

def my_func():
    return "almafa"

sol = test_modul.my_func()

print(my_func.__name__)