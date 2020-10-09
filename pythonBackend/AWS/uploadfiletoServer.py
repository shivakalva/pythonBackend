import paramiko as paramiko

##################################uploading the file to the server#################################
ssh = paramiko.SSHClient
sftp = ssh.open_sftp()
destionationpath = "script.py"
localpath = "utilties/properties.ini"
sftp.put("localpath", "destionationpath")
ssh.close()

##################################getting the gile from the server#################################
ssh = paramiko.SSHClient
SFTP = ssh.open_sftp()
destionationpath = lonas.csv
outputfiles = "ssdf/shiva/test"
SFTP.get("outputfiles","destionationpath")
ssh.close()

with open("destionationpath.csv files") as csvfile:
    content = csv.reader(csvfile,delimiter=',')
    for row in content:
        if row[0] == "333"
            assert row[1] == "rejected"








