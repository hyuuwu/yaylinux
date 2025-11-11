import os 
import webbrowser as wb
import time
from pytube import YouTube
import random as uwu
import install
import subprocess as sub

def run(app):
    sub.run([app])


open('password', 'w').close()
open('hostname', 'w').close()

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



























print("IBH (c)2010-2024 \nAll rights reserved ;)\n256 mb RAM : ok \n1.66ghz CPU: ok \n1000mb HDD : ok")
print(".")
time.sleep(2)
print(".")
time.sleep(2)
print(".")

input("press key.enter to contiinueeeeeee")

print("welcome to YAY pyth-linux.\nY = yolo\nA= autism\nY = yeet")

ihateicks = input("Hello user,we will kindly ask you to say your temp username \nInsert here: ")

print("HEYYYY", ihateicks, "WE MISSED YOU SO MUCH")
kk = input("want to have an passw? Yes(y) No(n)")
if kk == "y":
      ikendrick = input("insert pass")
      with open("password", "a") as f:
          f.write(ikendrick)

if kk == "y":
    heyhelp = input("insert pass")
    if heyhelp == ikendrick:
             print("preciate it")
    else:
         print("YOU SON OF A BITCH")
         while True:
              wb.open("hyuuwu.tech")

hostnameeee = input("what hostname you want to use \n")
with open("hostname", "a") as f:
    f.write(hostnameeee)


print("now we really starting")

while True:
     terminal = input(f"{ihateicks}@{hostnameeee} $ ~/")
     
     if terminal == "help":
      print("we aint helpin- jk. LIST OF COMMANDS:\nhelp: help.\nkanye: kanye song\nspaghetto: sekreti\nexit: exit\nmkdir: makes an dir\ncd: cd\nls: ls\nvim: rip ur pc\nytb: YOUTUBE DOWNLOADER YAHOO!\nopnytb: opens an url,but we want u to open yt tho\nhydra: opens its github page\nlauncher:wip\ncalc:wip")
      if terminal == "kanye":
          wb.open("https:/ /youtube.com/watch?v=wuO4_P_8p-Q&si=1j47jLi9GMSNRFsI")
          print("fire")
     if terminal == "spaghetto":
          print("spaghetto smosh")
          wb.open("https://www.youtube.com/watch?v=DgxPNW2iPQM")
          print("orochinho")
          print("hidden command lmaoooooooooooooooooooo")
     if terminal == "exit":
          print("end")
          wb.open("hyuaae.site/yaylinux")
          break
     if terminal == "mkdir":
          dir_name = input("nam3")
          dir_path = input("pat")  # Let user provide a path
    
          try:
               os.mkdir(os.path.join(dir_path, dir_name))  # Combine path and name safely
               print("mad3!")
          except OSError as error:
               print("sowwy :( :", error)

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
          print(firstn + secondn)
          print("thanks 4 using")



     if terminal == "smth":
          print("gangsta")


          
     else:
         run(terminal)
