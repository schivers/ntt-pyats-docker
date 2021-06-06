import subprocess
import time 

while True:
    cmd= ['pyats', 'logs', 'view', '--host', '0.0.0.0', '--port', '8005', '--no-browser', '--reuse-port']
    p=subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE)
    time.sleep(300)
    p.terminate()


