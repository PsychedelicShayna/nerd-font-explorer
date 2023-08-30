import json

from ctypes import (
    c_short,    c_ushort,    c_long, c_ulong, 
    c_longlong, c_ulonglong, c_int,  Structure
)

import ctypes

from typing import Union, Optional, Any
from pathlib import Path 

# -----------------------------------------------------------------------------

# Handle number to stdout/std::cout
STD_OUTPUT_HANDLE = -11



def read_nerd_fonts(path: Path) -> dict[str, str]:
    with open('./nerd-fonts.json', 'rb') as ifile:
        return json.load(ifile)

class COORDS(Structure):
    _fields_: list[Any] = [
        ("X", c_short),
        ("Y", c_short),
    ]
    
class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
    _fields: list[Any] = [
        ("dwSize", c_ulong),
        ("dwCursorPosition", c_ulong),
        ("wAttributes", c_ushort),
        ("srWindow", c_short * 4),
        ("dwMaximumWindowSize", c_ulong),
    ]
kernel32 = ctypes.windll.kernel32

h_console = kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


csbi = CONSOLE_SCREEN_BUFFER_INFO()
kernel32.GetConsoleScreenBufferInfo(h_console, ctypes.byref(csbi))

buffer_size = csbi.dwSize.X * csbi.dwSize.Y
print(buffer_size)

print("still works")
