#!/usr/bin/python
from colorama import Fore
import getpass

def DEFAULT():

    print(
        Fore.LIGHTGREEN_EX+
    " ____        _        ____                      \n"+
    "|  _ \  __ _| |_ __ _|  _ \ __ _ _ __ ___  ___ \n"+
    "| | | |/ _` | __/ _` | |_) / _` | '__/ __|/ _ \\\n"+
    "| |_| | (_| | || (_| |  __/ (_| | |  \__ \  __/\n"+
    "|____/ \__,_|\__\__,_|_|   \__,_|_|  |___/\___|\n"
    )

    while True:
        # Options
        print(
            Fore.WHITE+
            f"-----------------------------\n"+
            f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Functions    -->  1\n"+
            f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} MathMatics   -->  2\n"+
            f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Display      -->  3\n"+
            f"\n"+
            f"-----------------------------"+
            f"\n"
        )
        USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")

        if USER == "1":

            # Options
            while True:
            
                print(
                    "\n"
                    f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} ConCat             -->  1\n"+
                    f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} DropNA             -->  2\n"+
                    f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} DropColumn         -->  3\n"+
                    f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} DropRow            -->  4\n"+
                    f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} DropDuplicates     -->  5\n"+
                    f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} ConvertToDateTime  -->  6\n"+
                    f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} ConvertToInt       -->  7\n"+
                    f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} ExtractDate        -->  8\n"+
                    f"\n"+
                    f"-----------------------------"+
                    f"\n"
                )
                USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")                

                if USER == '1':
                    import functions.concat as CONCAT
                    print(f"{Fore.WHITE}[ OK ] ConCat Selected")
                    CONCAT.Easy_Option()
                    break
                elif USER == '2':
                    import functions.dropna as DROPNA
                    print(f"{Fore.WHITE}[ OK ] DropNA Selected")
                    DROPNA.Easy_Option()
                    break
                elif USER == '3':
                    import functions.dropgroup as DROPCOLUMN
                    print(f"{Fore.WHITE}[ OK ] DropColumn Selected")
                    DROPCOLUMN.Easy_Option()
                    break
                elif USER == '4':
                    import functions.droprow as DROPROW
                    print(f"{Fore.WHITE}[ OK ] DropRow Selected")
                    DROPROW.Easy_Option()
                    break
                elif USER == '5':
                    import functions.dropduplicates as DROPDUPLICATES
                    print(f"{Fore.WHITE}[ OK ] DropDuplicates Selected")
                    DROPDUPLICATES.Easy_Option()
                    break
                elif USER == '6':
                    import functions.datetime as DATETIME
                    print(f"{Fore.WHITE}[ OK ] ConvertToDateTime")
                    DATETIME.Easy_Option()
                    break
                elif USER == '7':
                    import functions.int as INT
                    print(f"{Fore.WHITE}[ OK ] ConvertToInt")
                    INT.Easy_Option()
                    break
                elif USER == '8':
                    import functions.datetime_sep as DATETIME_SEP
                    print(f"{Fore.WHITE}[ OK ] ExtractDate")
                    DATETIME_SEP.Easy_Option()
                    break
                else:
                    print(f"{Fore.RED}[ ! ] Invaild Option, Try again")

        elif USER == "2":
            # Options
            while True:
                print(
                    "\n"
                    f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Statics     -->  1\n"+
                    f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Operations  -->  2\n"+
                    f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} equations   -->  3\n"+
                    f"\n"+
                    f"-----------------------------"+
                    f"\n"
                )            
                USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")

                if USER == '1':
                    import mathmatics_functions.statics as STATICS
                    print(f"{Fore.WHITE}[ OK ] Statics Selected")
                    STATICS.Easy_Option()
                    break    
                
                elif USER == '2':
                    while True:
                        # Options
                        print(
                        "\n"
                        f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Sum        -->  1\n"+
                        f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Minus      -->  2\n"+
                        f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Multiply   -->  3\n"+
                        f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Divide     -->  4\n"+
                        f"\n"+
                        f"-----------------------------"+
                        f"\n"
                    )
                        USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")

                        if USER == "1":     
                            import mathmatics_functions.sum as SUM
                            print(f"{Fore.WHITE}[ OK ] Sum Selected")
                            SUM.Easy_Option()
                            break
                        elif USER == "2":
                            import mathmatics_functions.minus as MINUS
                            print(f"{Fore.WHITE}[ OK ] Minus Selected")
                            MINUS.Easy_Option()
                            break
                        elif USER == "3":
                            import mathmatics_functions.multiply as MULTIPLY
                            print(f"{Fore.WHITE}[ OK ] Multiply Selected")
                            MULTIPLY.Easy_Option()
                            break
                        elif USER == "4":
                            import mathmatics_functions.divide as DIVIDE
                            print(f"{Fore.WHITE}[ OK ] Divide Selected")
                            DIVIDE.Easy_Option()
                            break
                        else:
                            print(f"{Fore.RED}[ ! ] Invaild Option, Try again")
                    break

                elif USER == "3":
                    import equations.linear as LINEAR
                    print(f"{Fore.WHITE}[ OK ] linear Selected")
                    LINEAR.Easy_Option()
                    break

                else:
                    print(f"{Fore.RED}[ ! ] Invaild Option, Try again")

        elif USER == "3":

            # Options
            print(
                f"-----------------------------\n"+
                f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Histogram    -->  1\n"+
                f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Bar          -->  2\n"+
                f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Plot         -->  3\n"+
                f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Scatter      -->  4\n"+
                "\n"+
                f"-----------------------------"+
                "\n"
            )
            USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")

            if USER == "1":
                import display.hist as HIST
                print(f"{Fore.WHITE}[ OK ] Histogram Selected")
                HIST.Easy_Option()
            elif USER == "2":
                import display.bar as BAR
                print(f"{Fore.WHITE}[ OK ] bar Selected")
                BAR.Easy_Option()
            elif USER == "3":
                import display.plot as PLOT
                print(f"{Fore.WHITE}[ OK ] Plot Selected")
                PLOT.Easy_Option()
            elif USER == "4":
                import display.scatter as SCATTER
                print(f"{Fore.WHITE}[ OK ] Scatter Selected")
                SCATTER.Easy_Option()
            else:
                print(f"{Fore.RED}[ ! ] Invaild Option, Try again")

        else:
            print(f"{Fore.RED}[ ! ] Invaild Option, Try again")

DEFAULT()
