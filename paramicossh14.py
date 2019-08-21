#!/usr/bin/python3

from getpass import getpass
import paramiko

def cmdtoissue(sshsession, command_to_issue):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read().decode('utf--8')

def main():
    sshsession = paramiko.SSHClient()

    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    mypass = getpass("Password:  ")
    sshsession.connect(hostname="10.10.2.3", username="bender", password=mypass)

    mycommands = [
            "touch sshworked.txt",
            "uptime",
            "whoami",
            "hostname"
            ]

    for cmd in mycommands:
        print("###################\n", cmd, "\n-------------------")
        print(cmdtoissue(sshsession, cmd))

    sshsession.close()

if __name__ == "__main__":
    main()
