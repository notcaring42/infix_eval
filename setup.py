import sys
from cx_Freeze import setup, Executable

build_exe_options = {"excludes": ["tkinter"]}

base = None
target_name = "infix_eval"
if sys.platform == "win32":
    target_name = "InfixEval.exe"
    base = "Win32GUI"

setup(  name = "infix_eval",
        version = "0.1",
        description = "Infix expression evaluator",
        options = {"build_exe": build_exe_options},
        executables = [Executable("infix_eval/main.py", base=base, targetName=target_name)])
