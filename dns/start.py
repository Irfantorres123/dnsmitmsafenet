import subprocess
import requests

ip=requests.get('https://api.ipify.org').text
print(ip)
cmd=f"python ./dnschef.py --interface 0.0.0.0 --fakeip {ip}"
print(cmd)
subprocess.run(cmd.split(" "))
