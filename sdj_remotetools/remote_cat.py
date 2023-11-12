import paramiko
import sys
from getpass import getpass


def get_remote_file_content(remote_host: str, username: str, password: bool or None, path_to_file: str, encoding: str = 'utf8'):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        if password:
            try:
                ssh.connect(hostname=remote_host, username=username)
            except paramiko.SSHException as e:
                user_password = getpass(f'({remote_host}) Password: ')
                ssh.connect(hostname=remote_host, username=username, password=user_password)
        else:
            ssh.connect(hostname=remote_host, username=username)

        ftp = ssh.open_sftp()
        content = ftp.open(path_to_file).read().decode(encoding)
        ssh.close()
        return content

    except paramiko.SSHException as e:
        print(e)
        sys.exit(1)
    except FileNotFoundError as e:
        print(f'{e}: {username}@{remote_host}:{path_to_file}')
        sys.exit(1)
