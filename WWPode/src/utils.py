import hashlib
from colorama import init, Fore


init()

def italic(text: str) -> str:
    return f"\033[3m{text}\033[0m"

def md5(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()

def enter(prompt=">>> ", cast=str):
    try:
        value = globals()['input'](Fore.RESET + prompt)
        return cast(value)
    except ValueError:
        raise ValueError(f"[ERROR]: invalid data type: {cast.__name__}")