import re
from argparse import ArgumentTypeError as ArgparseArgumentError


def ssh_url_type(ssh_url: str) -> dict[str]:
    url_regex = '^(?P<username>\S+)@(?P<remote_host>\S+):(?P<path_to_file>/\S+)'
    result = re.search(url_regex, ssh_url)

    if result is None:
        raise ArgparseArgumentError(f'{ssh_url!r} is not a valid SSH url')

    return result.groupdict()
