import os
import webbrowser as wb
import time
import subprocess as sub
import sys
import platform
import threading
import littu as lil
import pyfiglet
import argparse
import install

parser = argparse.ArgumentParser(
    description="Deletes all the old config files. its like a factory reset"
)
parser.add_argument("--facreset", "-f", action="store_true", help="factory resets")
args = parser.parse_args()
if args.facreset:
    os.remove("password")
    os.remove("hostname")
    os.remove("dontdeletethis.file")
    os.remove("user")
    print("facresetted")

try:
    from playsound3 import playsound
except ImportError:
    print("Warning: playsound not installed. Audio will be disabled.")
    playsound = None


def play_audio(filename):
    if playsound and os.path.exists(filename):
        # Run in a separate thread so it doesn't block execution
        threading.Thread(target=playsound, args=(filename,), daemon=True).start()


chime = ""


def run(app):
    sub.run([app])


CONFIG_FILE = "dontdeletethis.file"


def is_first_run():
    if not os.path.exists(CONFIG_FILE):
        # This is the first run
        with open(CONFIG_FILE, "w") as f:
            f.write(
                "hi,this is a file to check if the user ran this file. ever. if you want to delete it,its yo choice,but you gon redo the setup"
            )
        return True
    else:
        # Not the first run
        return False


def list_files():
    directory_path = os.getcwd()  # Default to current directory
    try:
        contents = os.listdir(directory_path)
        print(directory_path)
        for item in contents:
            print(item)
    except OSError as error:
        print("Error listing directory:", error)


def audi0(filx):
    # im kms today fahhhhhh
    pyfiglet.figlet_format("SUPER AUDIO PLAYER 2000", font="slant")
    time.sleep(5)
    blyat = playsound(filx, block=False)
    while True:
        asap = input("say stop to exit")
        if asap == "stop":
            blyat.stop()
            break
        else:
            print("bet")


def cd(new_path):
    try:
        os.chdir(new_path)
        print(f"Directory changed to: {os.getcwd()}")
    except OSError as error:
        print("Error changing directory:", error)


def run_subprocess(shell_cmd):
    try:
        # prefer shell=False style when possible; allow shell-like string for convenience
        if platform.system() == "Windows":
            completed = sub.run(
                ["powershell", "-Command", shell_cmd], capture_output=True, text=True
            )
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
    command = command.strip()
    if not command:
        return

    if command == "kanye":
        wb.open("https://www.youtube.com/watch?v=wuO4_P_8p-Q")
        print("peak")
    elif command == "spaghetto":
        wb.open("https://www.youtube.com/watch?v=DgxPNW2iPQM")
        print("spaghetto smosh")
    elif command == "ytb":
        print("YouTube downloader placeholder")
    elif command == "ls":
        list_files()
    elif command.startswith("cd"):
        parts = command.split(" ", 1)
        if len(parts) > 1:
            directory = parts[1].strip()
        else:
            directory = input("Enter the directory path: ").strip()
        cd(directory)
    elif command == "exit":
        print("Exiting YAYLinux...")
        play_audio("qq.wav")
        time.sleep(4)
        sys.exit(0)
    elif command == "launcher":
        app = input("What app do you want to install?\n:")
        install.install(app)
    elif command == "help":
        print(
            "LIST OF COMMANDS:\nhelp: Show this help.\nkanye: Play Kanye song\nspaghetto: Secret video\nexit: Exit YAYLinux\ncd: Change directory\nls: List files\nvim: Text editor (Joke)\nytb: YouTube downloader placeholder\nopnytb: Opens YouTube\nlauncher: Install apps\ncalc: Calculator\nsource: View source code\nwhoamiyay: Show current user\n audioplayer: plays audio files"
        )
    elif command == "vim":
        print("imagine vim in the big 26 😭")
    elif command == "source":
        print("you can view our source code here!")
        wb.open("https://github.com/hyuuwu/yaylinux")
    elif command == "whoamiyay":
        print(ihateicks)
    elif command == "calc":
        try:
            firstn = float(input("first number: "))
            secondn = float(input("second number: "))
            print(firstn + secondn)
            print("thanks 4 using")
        except ValueError:
            print("why u using letters instead of numbers?")
            sys.exit("dont repeat that again >:( ")
    elif command == "opnytb":
        wb.open("https://www.youtube.com")
    elif command == "dfjk":
        print("OSU Player be like")

    elif command == "audioplayer":
        graduation = input(
            "whats the audio file you want to play?\n(insert the full path,or, if its in the same folder,just use the file name)\n>"
        )
        audi0(graduation)
    else:
        run_subprocess(command)


play_audio("q.wav")

print(
    "IBH (c)2010-2025 \nAll rights reserved ;)\n256 mb RAM : ok \n1.66ghz CPU: ok \n1000mb HDD : ok"
)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")

input("press Enter to continue...")

print("welcome to YAY pyth-linux.\nY = yolo\nA= autism\nY = yeet")

ihateicks = "User"
hostnameeee = "localhost"

if is_first_run():
    # Clear/Create files
    open("user", "w").close()
    open("hostname", "w").close()
    open("password", "w").close()

    ihateicks = input(
        "Hello user, we will kindly ask you to say your username \nInsert here: "
    )
    with open("user", "w") as f:
        f.write(ihateicks)

    print("HEYYYY", ihateicks, "WE MISSED YOU SO MUCH")
    ikendrick = input("create a password: ")
    lil.crypt(ikendrick, "password")

    heyhelp = input("confirm password: ")
    if heyhelp == ikendrick:
        print("Password confirmed.")
    else:
        print("Passoprd wrong fam")
        print(f"FYI, the password you set is {ikendrick}.")

    hostnameeee = input("what hostname you want to use \n")
    with open("hostname", "w") as f:
        f.write(hostnameeee)
else:
    if os.path.exists("hostname"):
        with open("hostname", "r") as h_file:
            hostnameeee = h_file.read().strip()

    if os.path.exists("user"):
        with open("user", "r") as u_file:
            ihateicks = u_file.read().strip()

    if os.path.exists("password"):
        with open("password", "r") as p_file:
            verify = lil.decrypt("password")

        verifypass = input(
            f"Hello {ihateicks}, Welcome back to YAYLinux! whats your password?\n"
        )
        if verifypass == verify:
            print("Welcome back!")
        else:
            print("Wrong password.")
            sys.exit("lmao imagine forgetting the pass")

while True:
    try:
        terminal = input(f"{ihateicks}@{hostnameeee} $ ~/")
        execute_command(terminal)
    except KeyboardInterrupt:
        print("\nUse 'exit' to quit.")
    except EOFError:
        sys.exit(0)
