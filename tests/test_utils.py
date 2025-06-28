import copy
import pytest
from sdj_remotetools.utils import ssh_url_type, get_parser


def test_ssh_url_type():
    url = 'joe@some.host.local:/path/to/file'
    result = {
            'username': 'joe',
            'remote_host': 'some.host.local',
            'path_to_file': '/path/to/file'
        }

    assert ssh_url_type(url) == result


def test_get_parser_preserves_config():
    parser_config = {
        'header': {'prog': 'dummy'},
        'args': [
            {
                'name_or_flags': ['-f', '--flag'],
                'action': 'store_true',
                'help': 'dummy flag',
            }
        ]
    }
    original = copy.deepcopy(parser_config)
    parser1 = get_parser(parser_config)
    parser2 = get_parser(parser_config)

    assert parser_config == original
    assert parser1.parse_args([]).flag is False
    assert parser2.parse_args(['--flag']).flag is True
