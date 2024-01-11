#!/usr/bin/python3
import argparse
import pandas as pd
import os
from datetime import datetime, timedelta, date
from pathlib import Path

def format_bytes(size):
    # https://stackoverflow.com/a/49361727
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0 : 'B', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
    while size > power:
        size /= power
        n += 1
    return f"{round(size, 1)}{power_labels[n]}"

parser = argparse.ArgumentParser()
parser.add_argument("directory", help="The directory to audit")
parser.add_argument("--min-days", "--days", help="Only show files older than this many days old. Default 0 days.", default=0, type=int)
parser.add_argument("--min-size", "--size", help="Only show files larger than this many bytes. Default 0 bytes.", default=0, type=int)
parser.add_argument("--output-dir", "-o", help="Filepath of output directory. Default 'outputs'", default="outputs")
parser.add_argument("--user", "-u", help="Include only files owned by this user")
args = parser.parse_args()

base_path = os.path.abspath(args.directory)
now = datetime.now()
date_limit = datetime.timestamp(now - timedelta(days=args.min_days))

out_file = os.path.join(args.output_dir, f"disk_audit_{now.replace(microsecond=0).isoformat()}.csv")
err_file = os.path.join(args.output_dir, f"disk_audit_{now.replace(microsecond=0).isoformat()}.err")

data = []

for root, dirs, files in os.walk(base_path):
    for file in files:
        filepath = root + '/' + file
        try:
            size = os.path.getsize(filepath)
            creation_time = os.path.getctime(filepath)
            modification_time = os.path.getmtime(filepath)
            access_time = os.path.getatime(filepath)
            owner = Path(filepath).owner()
            data.append([size, filepath, owner, creation_time, modification_time, access_time])
        except Exception as err:
            with open(err_file, "a+") as file:
                file.write(f"{err}\n")

df = pd.DataFrame(data, columns=['size','filepath','owner','created','modified','accessed'])
df = df.sort_values(by='size', ascending=False)
df = df.loc[df['created'] <= date_limit]
df = df.loc[df['size'] >= args.min_size]
df['created'] = df['created'].apply(lambda x: date.fromtimestamp(x))
df['modified'] = df['modified'].apply(lambda x: date.fromtimestamp(x))
df['accessed'] = df['accessed'].apply(lambda x: date.fromtimestamp(x))
df['size'] = df['size'].apply(lambda x: format_bytes(x))

if args.user:
    df = df.loc[df['owner'] == args.user]

df.to_csv(out_file, index=False)
