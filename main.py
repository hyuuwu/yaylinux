import os 
import webbrowser as wb
import time
from pytube import YouTube
import random as uwu
import install
import subprocess as sub
import sys
import platform
from playsound import playsound

chime = "chime.mp3"
signoff = "signoff.mp3"

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






def apt():
     smthsmth = input("wut app u want")
     print("list: \nprint: print smth\ngoogle: opens googles ")



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


























playsound(chime, True)
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
     
     if terminal == "help":
      print("we aint helpin- jk. LIST OF COMMANDS:\nhelp: help.\nkanye: kanye song\nspaghetto: sekreti\nexit: exit\ncd: cd\nls: ls\nvim: rip ur pc\nytb: YOUTUBE DOWNLOADER YAHOO!\nopnytb: opens an url,but we want u to open yt tho\nhydra: opens its github page\nlauncher:wip\ncalc:wip")
      if terminal == "kanye":
          wb.open("https:/ /youtube.com/watch?v=wuO4_P_8p-Q&si=1j47jLi9GMSNRFsI")
          print("fire")
     if terminal == "spaghetto":
          print("spaghetto smosh")
          wb.open("https://www.youtube.com/watch?v=DgxPNW2iPQM")
          print("orochinho")
          print("hidden command lmaoooooooooooooooooooo")
     if terminal == "exit":
          print("Thanks For Using!")
          playsound(signoff, True)
          break




     if terminal == "ls":  # Use a common 'ls' command for listing
          list_files()
     
     if terminal == "cd":
          j = input("wut dir?: ")
          cd(j)
          #this shit crashed python
     if terminal == "vim":
          print("how to crash ur pc")
          owo = uwu.randint(1,5)
          if owo == 4:
              while True:
                  wb.open("open.spotify.com")
          else:
              break

     if terminal == "ytb":
          video_url = input("input ur video url (VALID PLZ)") # Your video URL
          yt = YouTube(video_url)

          stream = yt.streams.get_highest_resolution()  # Or choose a specific format
          stream.download() 
          print("Video downloaded!")

     if terminal == "opnytb":
          sex = input("url here: ")
          wb.open(sex)

     if terminal == "hydra":
          wb.open("https://github.com/hydralauncher/hydra")

     if terminal == "launcher":
         abcd = input(f" hey user {ihateicks}, do you wanna install an app? (Y/n)")
         if abcd == "n":
             print("bet")
         else:
             efgh = input("what app do you want to install? \n:")
             install.install(efgh)

     if terminal == "calc":
         firstn = input("first number")
         secondn = input("second number")
         print(int(firstn) + int(secondn))
         print("thanks 4 using")



     if terminal == "smth":
          print("gangsta")


          
     else:
         if platform.system == "Linux":
             klmn = sub.run(["sh", "-c", terminal])
         else:
            j = sub.run(["powershell", "-Command", terminal])
            if j.returncode == 0:
                print("app run")
            else:
                print("oops")
