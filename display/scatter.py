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

def MyFunc(FILE, COLUMN_X, COLUMN_Y, label_X, label_Y):
    all_data = pd.read_csv(FILE)
    plt.scatter(all_data[f'{COLUMN_X}'], all_data[f'{COLUMN_Y}'])
    plt.xlabel(label_X)
    plt.ylabel(label_Y)
    plt.show()

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

    df = pd.read_csv(FILE)
    for i in df.columns:
        time.sleep(0.1)
        print(f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} {i}")

    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type Column-X Name(Input)")
        USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")

        if USER in df.columns:
            COLUMN_X = USER
            break
        else:
            print(f"{Fore.RED}[ ! ] Invaild, Try again")

    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type Column-Y Name(Input)")
        USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")

        if USER in df.columns:
            COLUMN_Y = USER
            break
        else:
            print(f"{Fore.RED}[ ! ] Invaild, Try again")            

    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type label-X Name(Input)")
        label_X = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        break

    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type label-Y Name(Input)")
        label_Y = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        break

    return FILE, COLUMN_X, COLUMN_Y, label_X, label_Y

def Easy_Option():
    FILE, COLUMN_X, COLUMN_Y, label_X, label_Y = USER_INPUT()
    MyFunc(FILE, COLUMN_X, COLUMN_Y, label_X, label_Y)