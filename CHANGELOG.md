# CHANGELOG

## v0.4.0

### New features
- Added `rlist` which allows to list the content of a remote directory through SSH.
```
usage: rlist [-h] [-a] [-l] [-p] ssh_url

Works almost liks 'ls' but through SSH

positional arguments:
  ssh_url         SSH path to a remote file or directory, space separate, ie: joe@remote.host:/remote/path

options:
  -h, --help      show this help message and exit
  -a, --all       Show hidden and 'dot' files. Default: False
  -l, --long      Display extended file metadata as a table
  -p, --password  Ask user for password. Default: False
```

### Breaking changes
- None

### Improvements
- Moved `rcat` to its own file.
- Removed unused import statements.
- Generalized the command line parser configuration

### Bugfixes
- `rcat` now properly handles error when targeting a directory.