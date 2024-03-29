# Disk Audit

`./disk_audit.py directory`

## usage

```
usage: disk_audit.py [-h] [--min-days MIN_DAYS] [--min-size MIN_SIZE]
                     [--output-dir OUTPUT_DIR] [--user USER]
                     directory

positional arguments:
  directory             The directory to audit

optional arguments:
  -h, --help            show this help message and exit
  --min-days MIN_DAYS, --days MIN_DAYS
                        Only show files older than this many days old. Default 0 days.
  --min-size MIN_SIZE, --size MIN_SIZE
                        Only show files larger than this many bytes. Default 0 bytes.
  --output-dir OUTPUT_DIR, -o OUTPUT_DIR
                        Filepath of output directory. Default 'outputs'
  --user USER, -u USER  Include only files owned by this user
```

## outputs
`disk_audit_DATETIME-NOW.csv` in the user specified working directory.
```
size,filepath,owner,created,modified,accessed
514.4MB,/full/path/to/file.txt,user001,2023-05-18,2023-05-18,2024-01-09
```