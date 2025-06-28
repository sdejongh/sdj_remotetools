import pytest
from sdj_remotetools.utils import ssh_url_type, ArgparseArgumentError


def test_ssh_url_type():
    url = 'joe@some.host.local:/path/to/file'
    result = {
            'username': 'joe',
            'remote_host': 'some.host.local',
            'path_to_file': '/path/to/file'
        }

    assert ssh_url_type(url) == result


def test_ssh_url_type_invalid():
    with pytest.raises(ArgparseArgumentError):
        ssh_url_type('invalid')
