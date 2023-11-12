import argparse
from sdj_remotetools.remote_cat import get_remote_file_content
from sdj_remotetools.utils import ssh_url_type


def rcat():
    parser = argparse.ArgumentParser(
        prog='rcat',
        description='Works like \'cat\' but through SSH.',
    )
    parser.add_argument('url', type=ssh_url_type, help='SSH path to the remote file, ie: joe@remote.host:/path/to/file')
    parser.add_argument('-p', '--password', type=str, help='User password')
    parser.add_argument('-e', '--encoding', type=str, default='utf-8', help='Character encoding, ie: utf-8 (default)')
    args = parser.parse_args()

    ssh_args = args.url
    ssh_args.update({'password': args.password, 'encoding': args.encoding})

    remote_file_content = get_remote_file_content(**ssh_args)

    print(remote_file_content)
