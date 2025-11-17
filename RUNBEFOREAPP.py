import subprocess as sub
import sys

command2 = 'pip install -r requirements.txt'
if sys.platform == "linux" or sys.platform == "linux2":
    sub.run(["sh", "-c", command2])
else:
    sub.run(["powershell", "-Command", command2])
