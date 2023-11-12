import argparse
from sdj_remotetools.remote_cat import get_remote_file_content
from sdj_remotetools.utils import ssh_url_type


def rcat():
    parser = argparse.ArgumentParser(
        prog='rcat',
        description='Works like \'cat\' but through SSH.',
    )
    parser.add_argument('remote_files', nargs='+', type=ssh_url_type, help='SSH path to the remote files, space seperate, ie: joe@remote.host:/path/to/file')
    parser.add_argument('-p', '--password', action='store_true', help='Ask user for password')
    parser.add_argument('-e', '--encoding', type=str, default='utf-8', help='Character encoding, ie: utf-8 (default)')
    parser.add_argument('-t', '--title', action='store_true', help='Display header before each file content')
    args = parser.parse_args()

    outputs = []

    for remote_file_args in args.remote_files:
        ssh_args = remote_file_args
        ssh_args.update({'password': args.password, 'encoding': args.encoding})
        if args.title:
            outputs.append(f'##### BEGIN: {ssh_args["remote_host"]}:{ssh_args["path_to_file"]} #####')
        outputs.append(get_remote_file_content(**ssh_args))
        if args.title:
            outputs.append(f'##### END: {ssh_args["remote_host"]}:{ssh_args["path_to_file"]} #####')
            outputs.append('\n')

    print('\n'.join(outputs))
