# CHANGELOG

## v0.5.0

### New features
- Added `rexec` which allows to execute commands on a list of remote hosts
```
usage: rexec [-h] [-u USERNAME] [-p PASSWORD] [-o OUTPUT] [-s] remote_hosts command

Executes command on a list of remote hosts and output result.

positional arguments:
  remote_hosts          A coma separated list of hosts. Ex: root@127.0.0.1,joe@example.org
  command               The command to execute on remote hosts

options:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Username for ssh authentication. Must be the same for all hosts
  -p PASSWORD, --password PASSWORD
                        Password for ssh authentication. Must be the same for all hosts
  -o OUTPUT, --output OUTPUT
                        Write output to this file. It not set output will print on stdout
  -s, --syntax_highlight
                        Enable console syntax highlighting
```

### Breaking changes
- None

### Improvements
- None

### Bugfixes
- None


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