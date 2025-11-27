#╔═════════════════════════════════════════════════════════╗
#║                                                         ║
from pywinauto.application import Application
from pywinauto import timings as t
import time
import os
#║                                                         ║
#╚═════════════════════════════════════════════════════════╝
#╔═════════════════════════════════════════════════════════╗
#║                                                         ║
PATH = r"S\CADe_SIMU_V4.2_4962.exe"
#║                                                         ║
#╚═════════════════════════════════════════════════════════╝
#╔═════════════════════════════════════════════════════════╗
#║                                                         ║
def EXECUTE():
    #╔═════════════════════════════════════════════════════════╗
    #║                                                         ║
    print(f"\033[92m[CADeSIMU-MOD]: 1\033[0m")
    APP = Application(backend="win32").start(PATH)
    time.sleep(1)
    APP = Application(backend="win32").connect(path=PATH)
    KEY = None
    #║                                                         ║
    #╚═════════════════════════════════════════════════════════╝
    #╔═════════════════════════════════════════════════════════╗
    #║                                                         ║
    for _ in range(40):
        try:
            KEY = APP.window(title="CLAVE DE ACCESO")
            if KEY.exists(timeout=0.2):
                break
        except:
            pass
    time.sleep(0.5)

    if not KEY:
        print(f"\033[91m[Access window not found]\033[0m")
        return
    print("")
    #║                                                         ║
    #╚═════════════════════════════════════════════════════════╝
    #╔═════════════════════════════════════════════════════════╗
    #║                                                         ║
    try:
        KEY.set_focus()
    except:
        try:
            KEY.set_focus()
        except:
            rect = KEY.rectangle()
            KEY.click_input(coords=(10, 10))

    time.sleep(0.3)

    CLAVE = "4962"
    print(f"[Inserting: {CLAVE} in access window]")

    KEY.type_keys(CLAVE, with_spaces=True, pause=0.1)
    KEY.type_keys("{ENTER}")

    print(f"\033[92m[CLAVE send]\033[0m")
    #║                                                         ║
    #╚═════════════════════════════════════════════════════════╝
#║                                                         ║
#╚═════════════════════════════════════════════════════════╝
#╔═════════════════════════════════════════════════════════╗
#║                                                         ║
if __name__ == "__main__":
    EXECUTE()
#║                                                         ║
#╚═════════════════════════════════════════════════════════╝