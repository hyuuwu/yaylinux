instructions

1. execute RUNBEFOREAPP.PY

2. use the app

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
        sys.exit(0)
    elif command == "launcher":
        app = input("What app do you want to install?\n:")
        install.install(app)
    elif command == help:
        print("we aint helpin- jk. LIST OF COMMANDS:\nhelp: help.\nkanye: kanye song\nspa>
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

this are most of the commands,so you dont get lost
