import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "excludes": [],
    "zip_include_packages": [],
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="FunE",
    version="0.1.3",
    description="My GUI application!",
    options={"build_exe": build_exe_options},
    executables=[Executable("FunE.pyw", base=base, icon="logo.ico")],
)
