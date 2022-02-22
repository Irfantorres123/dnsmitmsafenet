import subprocess
import requests
import sys

ip=requests.get('https://api.ipify.org').text
env=sys.argv[1]
cmd=""
if env=="DEV":
    cmd=f"python ./dnschef.py --interface 0.0.0.0 --fakeip 127.0.0.1"
else:
    cmd=f"python ./dnschef.py --interface 0.0.0.0 --fakeip {ip}"

subprocess.run(cmd.split(" "))
