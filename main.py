import os 
import webbrowser as wb
import time
from pytube import YouTube
import random as uwu
import install
import subprocess as sub
import sys
import platform
import pygame

pygame.init()


chime = ""


def run(app):
    sub.run([app])
CONFIG_FILE = "dontdeletethis.file"

def is_first_run():
    if not os.path.exists(CONFIG_FILE):
        # This is the first run
        with open(CONFIG_FILE, "w") as f:
            f.write("hi,this is a file to check if the user ran this file. ever. if you want to delete it,its yo choice,but you gon redo the setup")
        return True
    else:
        # Not the first run
        return False









def list_files():
    directory_path = input("Enter directory path: ")
    try:
        contents = os.listdir(directory_path)
        print(directory_path)
        for item in contents:
            print(item)
    except OSError as error:
        print("Error listing directory:", error) 



def cd(new_path):
    try:
        os.chdir(new_path)
        print(f"Directory changed to: {os.getcwd()}")  # Optional: Show the new path
    except OSError as error:
        print("Error changing directory:", error) 




def run_subprocess(shell_cmd):

    try:
        # prefer shell=False style when possible; allow shell-like string for convenience
        if platform.system() == "Windows":
            completed = sub.run(["powershell", "-Command", shell_cmd], capture_output=True, text=True)
        else:
            completed = sub.run(shell_cmd, shell=True, capture_output=True, text=True)
        if completed.returncode == 0:
            print(completed.stdout.strip())
        else:
            print("Command returned nonzero status.")
            print(completed.stderr.strip())
        return completed.returncode
    except Exception as e:
        print("Error running command:", e)
        return -1


def execute_command(command):
    if command == "kanye":
        wb.open("https://www.youtube.com/watch?v=wuO4_P_8p-Q")
        print("peak")
    elif command == "spaghetto":
        wb.open("https://www.youtube.com/watch?v=DgxPNW2iPQM")
        print("spaghetto smosh")
    elif command == "ytb":
        print("placeholder")
    elif command == "ls":
        list_files()
    elif command == "cd":
        directory = input("Enter the directory path: ").strip()
        cd(directory)
    elif command == "exit":
        print("Exiting YAYLinux...")
        my_sound2 = pygame.mixer.Sound('signoff.mp3')
        my_sound2.play()
        time.sleep(4)
        sys.exit(0)
    elif command == "launcher":
        app = input("What app do you want to install?\n:")
        install.install(app)
    elif command == help:
        print("we aint helpin- jk. LIST OF COMMANDS:\nhelp: help.\nkanye: kanye song\nspaghetto: sekreti\nexit: exit\ncd: cd\nls: ls\nvim: rip ur pc\nytb: YOUTUBE DOWNLOADER YAHOO!\nopnytb: opens an url,but we want u to open yt tho\nhydra: opens its github page\nlauncher:wip\ncalc:wip")
    elif command == "vim":
        print("how to crash ur pc")
        owo = uwu.randint(1, 5)
        if owo == 4:
            while True:
                wb.open("open.spotify.com")
        else:
            sys.exit("fuh vim")
    elif command == "source":
        print("you can view our source code here!")
        wb.open("https://github.com/hyuuwu/yaylinux")
    elif command == "whoamiyay":
        print(ihateicks)
    elif command == "calc":
        firstn = input("first number")
        secondn = input("second number")
        print(int(firstn) + int(secondn))
        print("thanks 4 using")

    else:
        run_subprocess(command)

















my_sound = pygame.mixer.Sound('chime.mp3')


my_sound.play()
print("IBH (c)2010-2025 \nAll rights reserved ;)\n256 mb RAM : ok \n1.66ghz CPU: ok \n1000mb HDD : ok")
print(".")
time.sleep(2)
print(".")
time.sleep(2)
print(".")

input("press key.enter to contiinueeeeeee")

print("welcome to YAY pyth-linux.\nY = yolo\nA= autism\nY = yeet")
if is_first_run():
    open('user', 'w').close()
    open('hostname', 'w').close()
    ihateicks = input("Hello user,we will kindly ask you to say your username \nInsert here: ")
    with open("user", "a") as f:
        f.write(ihateicks)

    print("HEYYYY", ihateicks, "WE MISSED YOU SO MUCH")
    ikendrick = input("create an pass")
    with open("password", "a") as f:
        f.write(ikendrick)
        heyhelp = input("insert pass")
        if heyhelp == ikendrick:
             print("preciate it")
        else:
            print("wrong pass,but ok")
            print(f"if you forget,the pass is {ikendrick}.")

    hostnameeee = input("what hostname you want to use \n")
    with open("hostname", "a") as f:
        f.write(hostnameeee)
else:
    with open("hostname", "r") as h_file:
        hostnameeee = h_file.read().strip()


    with open("user", "r") as u_file:
        ihateicks = u_file.read().strip()

    with open("password", "r") as p_file:
        verify = p_file.read().strip()

    verifypass = input(f"Hello {ihateicks}, Welcome back to YAYLinux! whats your password?\n")
    if verifypass == verify:
        print("Welcome back!")
    else:
        print("Wrong password, try again at reboot")
        sys.exit("wrong pass >:(")



while True:
     terminal = input(f"{ihateicks}@{hostnameeee} $ ~/")
     execute_command(terminal)

