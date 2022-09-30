import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
from colorama import Fore
import getpass
import time
import os

def MyFunc(FILE, COLUMN_X, COLUMN_Y, OUTPUT):

    df = pd.read_csv(FILE, parse_dates=False)
    x = df[f'{COLUMN_X}']
    y = df[f'{COLUMN_Y}']

    x = x.dropna(how="all")
    y = y.dropna(how="all")

    slope, intercept, r, p, std_err = stats.linregress(x, y)

    def myfunc(x):
        return slope * x + intercept

    mymodel = list(map(myfunc, x))

    json = {
        "x":x.to_string(),
        "y":y.to_string()
    }

    f = open(OUTPUT, "a")
    f.write(str(json))


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

    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type filename(Output)")
        USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")

        try:
            f = open(f"{os.getcwd()}/{USER}", "a")
            f.close()
            OUTPUT = USER
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

    return FILE, COLUMN_X, COLUMN_Y, OUTPUT

def Easy_Option():
    FILE, COLUMN_X, COLUMN_Y, OUTPUT = USER_INPUT()
    MyFunc(FILE, COLUMN_X, COLUMN_Y, OUTPUT)