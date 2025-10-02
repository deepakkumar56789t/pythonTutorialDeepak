# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import numpy as np

def pandas_methos():
    ser=pd.Series()
    data =np.array([1,7,8,9,10,11,12,13,14,15,2,3,4,5,6])
    ser=pd.Series(data)
    print("Pandas Series:\n", ser)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
