from colorama import Fore, Back, Style
from enum import Enum


def print_info(out_string, fore_color=Fore.GREEN, back_color=Back.RESET, silent=False):
    if not silent:
        print(f'[INFO]{fore_color} {back_color} {out_string} {Style.RESET_ALL}')


def print_error(out_string, fore_color=Fore.RED, back_color=Back.RESET, silent=False):
    print(f'[ERROR]{fore_color} {back_color} {out_string} {Style.RESET_ALL}')


def print_result(out_string, for_color=Fore.GREEN, back_color=Back.RESET, silent=False):
    print(f'[]{for_color} {back_color} {out_string} {Style.RESET_ALL}')


class OutputType(Enum):
    INFO = 'Info'
    RESULT = 'Result'
    ERROR = 'Error'
