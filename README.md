# PASSWD

## Requirements

- python 3.6 or later

## Install

1. Move `pwgen.py` to `/usr/local/bin/`

```bash
sudo mv pwgen.py /usr/local/bin/pwgen
```

```bash
sudo chmod +x /usr/local/bin/pwgen
```

## Usage

```bash
$ pwgen
VF6wNRT55FC6
```

```bash
$ pwgen 32
tsaO0NJArNJuVseyBukMXgl4jJMLs7SH
```

```bash
$ pwgen 32 hard
S2Kp-n:Qd}zP&^6@xQNeI\"ufB?|g:34
```

## TODO

Add arguments and options:

- Password Length: 16
- Include Symbols:( e.g. @#$% )
- Include Numbers:( e.g. 123456 )
- Include Lowercase Characters:( e.g. abcdefgh )
- Include Uppercase Characters:( e.g. ABCDEFGH )
- Exclude Similar Characters:( e.g. i, l, 1, L, o, 0, O )
- Exclude Ambiguous Characters:( { } [ ] ( ) / \ ' " ` ~ , ; : . < > )
- Number of passwords: 32
