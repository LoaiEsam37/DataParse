import pandas as pd
import os
import matplotlib.pyplot as plt
from colorama import Fore
import numpy as np
import getpass
import time
import json

def MyFunc1(FILE, COLUMN_X, COLUMN_Y, label_X, label_Y, Title):
    # filename(Input)
    all_data = pd.read_csv(FILE)
    x = all_data[f'{COLUMN_X}']
    y = all_data[f'{COLUMN_Y}']
    # plot
    plt.plot(x, y)
    # Title
    plt.title(Title)
    # Labels
    plt.xlabel(label_X)
    plt.ylabel(label_Y)
    # show
    plt.show()

def MyFunc2(FILE, label_X, label_Y, Title, SCATTER, LINEAR, POLY, BAR):
    # filename (Input)
    with open(FILE, "r") as read_file:
        data = json.load(read_file)
    # Declare json variables
    x = data['x']
    y = data['y']
    try:
        model = data['model']
    except:
        pass
    # Scatter option
    if SCATTER:
        plt.scatter(x, y)
    elif BAR:
        plt.bar(x, y)
    # Polynomial option
    if POLY:
        try:
            model = np.poly1d(np.polyfit(x, y, 3))
            line = np.linspace(1, len(x), 100)
            plt.plot(line, model(line))
        except Exception as e:
            exit(e)
    # Linear option
    elif LINEAR:
        try:
            plt.plot(x, model)
        except Exception as e:
            exit(e)
    else:
        plt.plot(x, y)
    # Title
    plt.title(Title)
    # Labels
    plt.xlabel(label_X)
    plt.ylabel(label_Y)
    # show
    plt.show()

def USER_INPUT():

    print(
        "-----------------------------\n"+
        f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} csv   -->  1\n"+
        f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} json  -->  2\n"+
        "\n"+
        "-----------------------------\n"+
        "\n"
    )
    USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
    if USER == "1":
        func = "1"
        POLY = False
        SCATTER = False
        LINEAR = False
        BAR = False
        # filename(Input)
        while True:
            print(f"{Fore.LIGHTGREEN_EX}Type filename(Input)")
            USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
            # CSV
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
        # COLUMNS
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
    elif USER == "2":
        func = "2"
        COLUMN_X = False
        COLUMN_Y = False
        # filename(Input)
        while True:
            print(f"{Fore.LIGHTGREEN_EX}Type filename(Input)")
            USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
            # JSON
            try:
                try:
                    f = open(f"{os.getcwd()}/{USER}", "r")
                    f.close()
                    FILE = USER
                    break
                except:
                    f = open(f"{os.getcwd()}/{USER}.json", "r")
                    f.close()
                    FILE = USER + ".json"
                    break
            except:
                print(f"{Fore.RED}[ ! ] invaild, Try again")
        # Scatter option
        while True:
            print(
                "\n"+
                f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Scatter  -->  1\n"+
                f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Bar      -->  2\n"+
                f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} None     -->  3\n"+
                f"\n"+
                f"-----------------------------"+
                f"\n"
            )
            USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
            if USER == "1":
                SCATTER = True
                BAR = False
                break
            elif USER == "2":
                BAR = True
                SCATTER = False
                break
            elif USER == "3":
                BAR = False
                SCATTER = False
                break
            else:
                print(f"{Fore.RED}[ ! ] invaild, Try again")
        # options
        while True:
            print(
                "\n"+
                f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Polynomial  -->  1\n"+
                f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Linear      -->  2\n"+
                f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Other       -->  3\n"+
                f"\n"+
                f"-----------------------------"+
                f"\n"
                )
            USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
            if USER == "1":
                POLY = True
                LINEAR = False
                break
            elif USER == "2":
                POLY = False
                LINEAR = True
                break
            elif USER == "3":
                POLY = False
                LINEAR = False
                break
            else:
                print(f"{Fore.RED}[ ! ] invaild, Try again")

    else:
        print(f"{Fore.RED}[ ! ] Invaild, Try again")        

    # Label-X
    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type label-X Name(Input)")
        label_X = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        break
    # Label-Y
    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type label-Y Name(Input)")
        label_Y = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        break
    # Title
    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type Title Name(Input)")
        Title = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        break
    
    return FILE, COLUMN_X, COLUMN_Y, label_X, label_Y, Title, func, SCATTER, LINEAR, POLY, BAR

def Easy_Option():
    FILE, COLUMN_X, COLUMN_Y, label_X, label_Y, Title, func, SCATTER, LINEAR, POLY, BAR = USER_INPUT()
    if func == "1":
        MyFunc1(FILE, COLUMN_X, COLUMN_Y, label_X, label_Y, Title)
    if func == "2":
        MyFunc2(FILE, label_X, label_Y, Title, SCATTER, LINEAR, POLY, BAR)