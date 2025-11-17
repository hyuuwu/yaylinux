import subprocess as sub
import os
# import time
import platform

def install(app):
    if platform.system() == 'Windows' :
        look4choco = sub.run(["where", "choco"])
        if look4choco.returncode == 0:
            installation = sub.run(["choco", "install", app, "-y"])
            if installation.returncode == 0:
                print("app installed")
            else:
                print("install failed with error")
        else:
            print("choco not installed")
            chocoinstaller = "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"
            chocoinstaller2 = sub.run(["powershell", "-Command", chocoinstaller])
            if chocoinstaller2.returncode == 0:
                print("restart the application,please")
            else:
                print("choco didnt install. quiting")
    else:
        if platform.system() == 'Linux':
            linux = sub.run(["sudo", "-S", "pacman", "-S", app], stdout=sub.PIPE)
            if linux.returncode == 0:
                print("app(or cli command,nerd) installed")
            else:
                print("u prob use debian. btw,error")
        else:
            if os.uname == "Darwin":
                print("uhh idk how to install things on mac")
            else:
                print("what os are you even using anyway?")
