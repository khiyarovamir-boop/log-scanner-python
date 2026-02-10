# log scanner

a simple python CLI tool to scan text or log files.

## features
- line by line file reading (memory safe)
- case insensitive search
- optional regex mode
- prints line numbers and total matches
- defensive error handling

## usage

normal search:
```bash
python logscanner.py error logs.txt
