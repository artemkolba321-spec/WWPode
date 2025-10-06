import os
import sys
import json
import math
import utils
from time import sleep
from colorama import init, Fore



init()
class WWPode:
    def __init__(self, title):
        self.COLORS = {
            "info": Fore.CYAN,
            "error": Fore.RED,
            "processes": Fore.YELLOW,
            "prompt": Fore.GREEN,
        }
        self.commands = [
            "help - помощь по WWPode",
            "exit - выход",
            "VScode - открыть VSCode",
            "PI - число π",
            f"E - число {utils.italic('e')}",
            "source code - исходный код",
            "ceil - округление числа вверх",
            "floor - округление числа вниз",
            "round - округление числа",
            "cwd - текущая директория",
        ]
        self.set_title(title)
        self.init_command()


    @staticmethod
    def set_title(title):
        if os.name == "nt":  # Windows
            os.system(f"title {title}")
        else:  # другие (Linux, macOS)
            sys.stdout.write(f"\033]0;{title}\007")
            sys.stdout.flush()
    @staticmethod
    def clear_screen():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    def show_welcome(self):
        print(self.COLORS["info"] + "добро пожаловать в терминал для прогроммистов")

    def textarea(self, prompt="~ ", end="END"):
        print(self.COLORS["processes"] + f"многострочный режим включён. Напишите {end} на новой строке, чтобы выйти.")
        lines = []
        while True:
            line = input(Fore.RESET + prompt)
            if line.strip().upper() == end.upper():
                break
            lines.append(line)
        return "\n".join(lines)
    def init_command(self):
        desktop = sys.platform
        self.run = True # основная переменная в методе
        self.show_welcome()
        while self.run:
            self.command = input(self.COLORS["prompt"] + f"{desktop}@> ")
            self.handle_command()

    def handle_command(self):
        match self.command:
            case "WWP --help" | "WWP -?":
                print(self.COLORS["info"] + "самые популярные флаги: ")
                print("--help или -? => помощь исполнителя")
                print("--version => версия WWPode")
            case "WWP --version":
                with open("../project.json", "r") as f:
                    data = json.load(f)
                    print(self.COLORS["info"], data["version"])
            case "help":
                print(self.COLORS["info"] + "самые популярные команды: ")
                for el in self.commands:
                    print(self.COLORS["info"] + el)


            case "exit" | "quit":
                print(self.COLORS["processes"])
                print("идет выход...")
                sleep(2)
                self.run = False
            case "VScode":
                try:
                    os.system("code")
                except Exception:
                    print(self.COLORS["error"] + "[WWP]: VScode не добавлен в PATH")
            case "PI":
                print(self.COLORS["info"], math.pi)
            case "E":
                print(self.COLORS["info"], math.e)
            case "source code":
                print(self.COLORS["info"] + "Исходный код пока не опубликован")
            case "clear":
                self.clear_screen()
            case "ceil":
                x = utils.enter(cast=float)
                print(self.COLORS["info"], math.ceil(x))
            case "floor":
                x = utils.enter(cast=float)
                print(self.COLORS["info"], math.floor(x))
            case "round-C2":
                x = utils.enter(cast=float)
                print(self.COLORS["info"], round(x, 2))
            case "round-C1":
                x = utils.enter(cast=float)
                print(self.COLORS["info"], round(x, 1))
            case "round":
                x = utils.enter(cast=float)
                print(self.COLORS["info"], round(x))
            case "edd": # TODO: реализовать команду edd
                print(self.COLORS["processes"])
                print("[i]: install")
                print("[d]: delete")
                print("[dd]: delete all")
                print("[e]: exit")

                what = input(">>> ")
            case "cwd":
                pach = os.getcwd()
                print(pach)


            case "?dev hash":
                data = input(Fore.RESET + ">>> ")
                print(utils.md5(data))

            case "":
                print(self.COLORS["error"] + "[WWP]: вы нечего не вели")
                print("попробуйте вести 'help' это выведет список команд")
            case _:
                print(self.COLORS["error"] + f"[WWP]: команды '{self.command}' не существует")
                print("попробуйте вести 'help' это выведет список команд")

if __name__ == '__main__':
    WWPode("WWPode")