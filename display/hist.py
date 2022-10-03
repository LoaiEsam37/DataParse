import pandas as pd
import os
import matplotlib.pyplot as plt
from colorama import Fore
import getpass
import time

def MyFunc(FILE, COLUMN, label_X, label_Y, Title):
    all_data = pd.read_csv(FILE)
    plt.hist(all_data[f'{COLUMN}'])
    plt.title(Title)
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
    # filename(Input)
    df = pd.read_csv(FILE)
    for i in df.columns:
        time.sleep(0.1)
        print(f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} {i}")
    # COLUMN
    while True: 
        print(f"{Fore.LIGHTGREEN_EX}Type Column Name(Input)")
        USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        if USER in df.columns:
            COLUMN = USER
            break
        else:
            print(f"{Fore.RED}[ ! ] Invaild, Try again")
    # label-X
    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type label-X Name(Input)")
        label_X = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        break
    # label-Y
    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type label-Y Name(Input)")
        label_Y = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        break
    # Title
    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type Title Name(Input)")
        Title = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        break

    return FILE, COLUMN, label_X, label_Y, Title

def Easy_Option():
    FILE, COLUMN, label_X, label_Y, Title = USER_INPUT()
    MyFunc(FILE, COLUMN, label_X, label_Y, Title)