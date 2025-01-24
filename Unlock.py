from os import remove,path,system
from shutil import rmtree
import psutil
dir_path = r"C:\Windows\System32\Turk"
if path.exists(dir_path):
    rmtree(dir_path)
    remove("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\lol.lnk")
    # system("shutdown /r /f /t 0")
def terminate_process_by_name(process_name):
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        try:
            if process_name.lower() in proc.info['name'].lower():
                print(f"Terminating process: {proc.info['name']} (PID: {proc.info['pid']})")
                proc.terminate()
                proc.wait()
                print(f"Process {proc.info['name']} terminated successfully.")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
try:        
    terminate_process_by_name('Turk Ransowm.exe')
    terminate_process_by_name('Turk Ransowm.exe')
except:
    terminate_process_by_name('Turk Ransowm.exe')

