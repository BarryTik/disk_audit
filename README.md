# Disk Audit

`./disk_audit.py directory`

## usage

```
usage: disk_audit.py [-h] [--min-days MIN_DAYS] [--min-size MIN_SIZE]
                     directory

positional arguments:
  directory             The directory to audit

optional arguments:
  -h, --help            show this help message and exit
  --min-days MIN_DAYS, --days MIN_DAYS
                        Only show files older than '--days' days old. Default 0 days.
  --min-size MIN_SIZE, --size MIN_SIZE
                        Only show files larger than this many bytes. Default 0 bytes.
```

## outputs
`disk_audit.csv` in the current working directory.
```
size,filepath,created,modified,accessed
514.4MB,/full/path/to/file.txt,2023-05-18,2023-05-18,2024-01-09
```