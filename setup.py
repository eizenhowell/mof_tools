import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "mof_tools",
        version = "0.0.1",
        description = "Master of Fantasy Tools",
        options = {"build_exe": build_exe_options},
        executables = [Executable("extractor.py", base="console")])