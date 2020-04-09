#!/usr/bin/env python
import paramiko
REMOTE_HOST = '172.16.29.251'
REMOTE_USER = 'wombat'
REMOTE_PASSWORD = 'm@rsup1al'

class RemoteConnection():
    def __init__(self, host, user, password):
        self._host = host
        self._user = user
        self._password = password
        self._connect()

    def _connect(self):
        self._ssh = paramiko.SSHClient()
        self._ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._ssh.connect(self._host, username=self._user, password=self._password)

    def run_command(self, command_line):
        stdin, stdout, stderr = self._ssh.exec_command(command_line)
        stdout_text = stdout.read()
        stderr_text = stderr.read()
        return stdout_text, stderr_text

    def __del__(self):
        self._ssh.close()

if __name__ == '__main__':
    rc = RemoteConnection(REMOTE_HOST, REMOTE_USER, REMOTE_PASSWORD)

    stdout, stderr = rc.run_command('whoami')
    print(stdout, '\n')

    stdout, stderr = rc.run_command('grep root /etc/pizza')
    print("STDOUT:", stdout)
    print("STDERR:", stderr)
