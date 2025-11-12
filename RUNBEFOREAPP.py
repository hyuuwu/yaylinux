import subprocess as sub
import sys
command = 'pip install playsound@git+https://github.com/taconi/playsound'
command2 = 'pip install -r requirements.txt'
if sys.platform == "linux" or sys.platform == "linux2":
    sub.run(["sh", "-c", command])
    sub.run(["sh", "-c", command2])
else:
    sub.run(["powershell", "-Command", command])
    sub.run(["powershell", "-Command", command2])
