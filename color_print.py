import datetime as dt
import time
import random
from termcolor import colored

def random_color_print(text='hello world'):
    color_str = 'red, green, yellow, blue, magenta, cyan, white'
    color_lis = color_str.split(', ')
    color_dic = {i:color_lis[i] for i in range(len(color_lis))}

    seed = int(dt.datetime.now().strftime('%s'))
    random.seed(seed)
    num = random.randint(0, len(color_dic)-1)
    print colored(text, color_dic.get(num, 0))

for i in range(10):
    random_color_print()
    time.sleep(1)
