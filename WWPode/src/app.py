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
        self.init_command()
        self.set_title(title)
    @staticmethod
    def set_title(title):
        if os.name == "nt":  # Windows
            os.system(f"title {title}")
        else:  # другие (Linux, macOS)
            sys.stdout.write(f"\033]0;{title}\007")
            sys.stdout.flush()
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
                print("help - помощь по WWPode")
                print("exit - выход")
                print("VScode - открыть VSCode")
                print("PI - число π")
                print(f"E - число {utils.italic("e")}")

            case "exit" | "quit":
                print(self.COLORS["processes"])
                sleep(2)
                print("идет выход...")
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
                if os.name == "nt":
                    os.system("cls")
                else:
                    os.system("clear")

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
            case "":
                print(self.COLORS["error"])
                print("[WWP]: вы нечего не вели")
                print("попробуйте вести 'help' это выведет список команд")
            case _:

                print(self.COLORS["error"])
                print(f"[WWP]: команды '{self.command}' не существует")
                print("попробуйте вести 'help' это выведет список команд")


if __name__ == '__main__':
    WWPode("WWPode")