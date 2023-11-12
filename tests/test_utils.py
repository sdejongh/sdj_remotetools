import pytest
from sdj_remotetools.utils import ssh_url_type


def test_ssh_url_type():
    url = 'joe@some.host.local:/path/to/file john@example.lan:/path/to/otherfile'
    result = [
        {
            'username': 'joe',
            'remote_host': 'some.host.local',
            'path_to_file': '/path/to/file'
        },
        {
            'username': 'john',
            'remote_host': 'example.lan',
            'path_to_file': '/path/to/otherfile'
        }
    ]
    assert ssh_url_type(url) == result
