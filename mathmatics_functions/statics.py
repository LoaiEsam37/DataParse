import re
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from itertools import combinations
from collections import Counter
from colorama import Fore
import sys
import getpass
import time

def MyFunc(FILE):
    DATA = pd.read_csv(FILE)
    print("\n")
    
    print(f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} MIN")
    print("-----------------------------\n")
    print(DATA.min(numeric_only=True))
    print("-----------------------------\n\n")
    print(f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} MAX")
    print("-----------------------------\n")
    print(DATA.max(numeric_only=True))
    print("-----------------------------\n\n")

    print("\n")

    print(f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} MODE")
    print("-----------------------------\n")
    print(DATA.mode(numeric_only=True))
    print("-----------------------------\n\n")

    print("\n")

    print(f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} MEDIAN")
    print("-----------------------------\n")
    print(DATA.median(numeric_only=True))
    print("-----------------------------\n\n")    

    print("\n")

    print(f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} MEAN")
    print("-----------------------------\n")
    print(DATA.mean(numeric_only=True))
    print("-----------------------------\n\n")    



def USER_INPUT():
    # FILE
    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type filename(Input)")
        USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")

        try:
            try:
                f = open(f"{os.getcwd()}/{USER}", "r")
                f.close()
                FILE = USER
                break
            except:
                f = open(f"{os.getcwd()}/{USER}.csv", "r")
                f.close()
                FILE = USER + ".csv"
                break
        except:
            print(f"{Fore.RED}[ ! ] invaild, Try again")

    return FILE

def Easy_Option():
    FILE = USER_INPUT()
    MyFunc(FILE)