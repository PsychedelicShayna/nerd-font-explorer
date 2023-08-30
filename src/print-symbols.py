import json, sys, os
from os import system as excmd


from ctypes import (
    c_short,    c_ushort,    c_long, c_ulong, 
    c_longlong, c_ulonglong, c_int,  Structure
)

import ctypes

from typing import Union, Optional, Any
from pathlib import Path 


import itertools
import functools



# -----------------------------------------------------------------------------

# # Handle number to stdout/std::cout
# STD_OUTPUT_HANDLE = -11
# 
# def nf_from_file(path: str) -> Optional[dict[str, str]]:
#     if not os.path.isfile(path):
#         return 
# 
#     with open('./nerd-fonts.json', 'rb') as ifile:
#         return json.load(ifile)
# 
# class COORDS(Structure):
#     _fields_: list[Any] = [
#         ("X", c_short),
#         ("Y", c_short),
#     ]
#     
# class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
#     _fields: list[Any] = [
#         ("dwSize", c_ulong),
#         ("dwCursorPosition", c_ulong),
#         ("wAttributes", c_ushort),
#         ("srWindow", c_short * 4),
#         ("dwMaximumWindowSize", c_ulong),
#     ]
# 
# def get_buffer_size():
#     kernel32 = ctypes.windll.kernel32
# 
#     h_console = kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
# 
#     csbi = CONSOLE_SCREEN_BUFFER_INFO()
#     kernel32.GetConsoleScreenBufferInfo(h_console, ctypes.byref(csbi))
# 
#     buffer_size = csbi.dwSize.X * csbi.dwSize.Y
#     print(buffer_size)
# 
# ------------------- WinAPI Stuff --------------------------------------------


if __name__ != "__main__":
    print("No interactive mode; not initializing;")
    raise SystemExit


# ----------------- Actual Main Logic ---------------------------------------

from sys import argv

symbols_file: Optional[str] = "data/nerd-fonts.json"

for argument, next_argument in zip(argv, argv[1:]):

    print('Evaluating argument')

    if (
            argument.lower() in ("--file", "-f", "--path", "-p")
        and os.path.isfile(next_argument)
    ):
        symbols_file = next_argument
   
if symbols_file is None:
    print('Please give a path to the .json containing the ')
    raise SystemExit

if not os.path.isfile(symbols_file):
    print(f'The file {symbols_file} does not exist.');

with open(symbols_file, 'rb') as io:
    data: dict[str, str] = json.load(io)


failed_decode = 0
unique_exceptions = []

for (icon_name, icon_id) in data.items():
    try:
        icon = bytes(int(icon_id, 16)).decode('utf-16')
        print(f'{icon_name}: {icon_id} {icon}')
    except UnicodeDecodeError as e:
        failed_decode += 1
        
        if type(e) not in unique_exceptions:
            unique_exceptions.append(type(e))


print(f'Failed to decode {failed_decode} icons.')
print(f'Unique exceptions: {unique_exceptions}')
    
