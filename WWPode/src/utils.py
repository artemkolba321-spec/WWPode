import colorama as color

color.init()

def italic(text):
    return f"\033[3m{text}\033[0m"