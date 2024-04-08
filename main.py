import os 
import webbrowser as wb
import time
import curses
from pytube import YouTube


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






def simple_vim():
    screen = curses.initscr()  # Start curses
    curses.noecho()  # Don't show typed characters
    curses.cbreak()  # Immediate input
    screen.keypad(True)  # Capture special keys

    text = []  # List to store our text

    # Rudimentary editing loop... 
    while True:
         key = screen.getch()

         if key == curses.KEY_BACKSPACE:
             # Handle backspace...

          if key == 27:  # Escape key
              break

         else:
              text.append(chr(key))  # Add normal characters

    # ... (Add logic for saving, cursor movement, etc) 

    curses.endwin()  # End curses




















best_friend_name = "linuk"

print("IBH (c)2010-2024 \nAll rights reserved ;)\n256 mb RAM : ok \n1.66ghz CPU: ok \n1000mb HDD : ok")
print(". \n. \n.")
input("press key.enter to contiinueeeeeee")

print("welcome to YAY pyth-linux.\nY = yolo\nA= autism\nY = yeet")

ihateicks = input("Hello user,we will kindly ask you to say your temp username \nInsert here: ")
if ihateicks == "hyu":
    print("r u the real hyu?")
    a = input("what is your bff name? \n")
    if a == best_friend_name:
            print("k u hyu")
    else:
          while True:
                wb.open("hyuuwu.tech")


print("HEYYYY", ihateicks, "WE MISSED YOU SO MUCH")
kk = input("want to have an passw? Yes(y) No(n)")
if kk == "y":
      ikendrick = input("insert pass")

if kk == "y":
    heyhelp = input("insert pass")
    if heyhelp == ikendrick:
        print("preciate it")
    else:
         print("YOU SON OF A BITCH")
         while True:
              wb.open("hyuuwu.tech")

print("now we really startin")

while True:
     terminal = input("yourname_here@computah $ ~/")
     if terminal == "help":
        print("we aint helpin- jk. LIST OF COMMANDS:\nhelp: help.\nkanye: kanye song")
     if terminal == "kanye":
          wb.open("https://youtube.com/watch?v=wuO4_P_8p-Q&si=1j47jLi9GMSNRFsI")
          print("fire")
     if terminal == "spaghetto":
          print("spaghetto smosh")
          wb.open("https://www.youtube.com/watch?v=DgxPNW2iPQM")
          print("orochinho")
          print("hidden command lmaoooooooooooooooooooo")
     if terminal == "exit":
          print("end")
          wb.open("hyuuwu.tech/yaylinux")
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
          simple_vim()

     if terminal == "ytb":
          video_url = input("input ur video url (VALID PLZ)") # Your video URL
          yt = YouTube(video_url)

          stream = yt.streams.get_highest_resolution()  # Or choose a specific format
          stream.download() 
          print("Video downloaded!")

     if terminal == "opnytb":
          sex = input("url here: ")
          wb.open(sex)





