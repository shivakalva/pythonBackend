import paramiko as paramiko
from utilties.configuration import *

# Start the connection

username = getconfig()['SSH']['username']
password = getconfig()['SSH']['password']
port = getconfig()['SSH']['port']
host = getconfig()['SSH']['host']

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,port,username,password)

# Run the commands
stdin,studout,stderr = ssh.exec_command("ls -a")
print(studout.readlines())
lines = studout.readlines()
print(lines[1])

