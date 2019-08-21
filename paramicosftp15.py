#!/usr/bin/python3

import paramiko

reqfiledefault = "requirements.txt"



def commandissue(sshsession, command_to_issue):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()

def gettargets():
    # Container list of lists: Odd items are users, Even are IPs
    targetlist = []

    targetip = input("Enter IP for connection:  ")
    targetlist.append(targetip)
    targetuser = input("Enter UserName for connection:  ")
    targetlist.append(targetuser)
    return targetlist

def main():
    connectionlist = []
    while True:
        connectionlist.append(gettargets())
        zvarquit = input("Continue (y/N)?  ")
        if zvarquit.lower() == 'n' or zvarquit == '':
            break

    # A requirements file can be used to set dependencies to run your required commands.
    # If errors, maybe edit requirements file to remove version num from line causing issues.
    #     python3 -m pip freeze > requirements2.txt
    #     python3 -m pip install -r  requirements2.txt
    # 
    reqfile = input(f"Requirements file pathname?  (Dflt: {reqfiledefault})  ")
    if reqfile == "":
        reqfile = reqfiledefault
    
    # range(num) gives list of numbers 0..(num -1)
    for conn_id in range(len(connectionlist)):
        sshsession = paramiko.SSHClient()
        mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        sshsession.connect( hostname=connectionlist[conn_id][0],
                           username=connectionlist[conn_id][1],
                           pkey=mykey )
        print( commandissue(sshsession, "ls -l").decode('utf--8') )
        ftp_client = sshsession.open_sftp()
        ftp_client.put(reqfile, reqfile)
        print( commandissue(sshsession, "ls -l").decode('utf--8') )
        ftp_client.close()

        #commandissue(sshsession, "sudo apt-get update -y")
        cmd = "sudo apt install python3-pip -y"
        print(cmd)
        commandissue(sshsession, cmd)

        cmd = "python3 -m pip install -r " + reqfile
        print(cmd)
        commandissue(sshsession, cmd)

        #print( commandissue(sshsession, "python3 -m pip freeze | egrep 'scrapy|ansible|requests'") )
        print( "python3 -m pip freeze:\n", commandissue(sshsession, "python3 -m pip freeze | egrep 'scrapy|ansible|requests'").decode('utf--8') )



if __name__ == "__main__":
    main()

