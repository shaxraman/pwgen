# PWGEN

[![flake8 test](https://github.com/shaxraman/pwgen/actions/workflows/flake8.yaml/badge.svg)](https://github.com/shaxraman/pwgen/actions/workflows/flake8.yaml)

## Requirements

- python 3.6 or later

## Install

1. Copy `pwgen.py` to `/usr/local/bin/`

```bash
sudo cp pwgen.py /usr/local/bin/pwgen
```

```bash
sudo chmod +x /usr/local/bin/pwgen
```

## Usage

```bash
$ pwgen
4@T=nkv5wbLZR8Sz
```

```bash
$ pwgen -l 32
tsaO0NJArNJuVseyBukMXgl4jJMLs7SH
```

```bash
$ pwgen -l 32 --hard
S2Kp-n:Qd}zP&^6@xQNeI\"ufB?|g:34
```

```bash
$ pwgen --exclude-symbols "123[]'/?.~"
8(f=kozh94)@N$WN
```

## TODO

Add arguments and options:

- Number of passwords: 32
- `include-symbols` must be present in the password
