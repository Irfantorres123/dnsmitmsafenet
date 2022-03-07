import subprocess
import os
ip="127.0.0.1"
if os.environ.get('IP'):
    ip=os.environ.get('IP')
    with open("file.txt","w") as file: file.write(ip)
cmd=f"python ./dnschef.py --interface 0.0.0.0 --fakeip {ip}"

subprocess.run(cmd.split(" "))
