import sys
from cx_Freeze import setup, Executable

build_exe_options = {"excludes": ["tkinter"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "infix_eval",
        version = "0.1",
        description = "Infix expression evaluator",
        options = {"build_exe": build_exe_options},
        executables = [Executable("infix_eval/main.py", base=base, targetName="infix_eval")])
