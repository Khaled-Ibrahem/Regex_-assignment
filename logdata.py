import re

log_entries = []
pattern = r'''
    ^
    (\d+\.\d+\.\d+\.\d+)   # Host (IP address)
    \s+-\s+                 # Separator
    (\S+)                   # User name
    \s+\[([^\]]+)\]         # Time (inside brackets)
    \s+"([^"]+)"           # Full Request (inside quotes)
    \s+\d+                 # Status (ignored)
    \s+\d+                 # Bytes (ignored)
    $
'''


def logs():
    with open("logdata.txt", "r") as file:
        for line in file:
            match = re.search(pattern, line.strip(), re.VERBOSE)
            if match:
                host, username, time, request = match.groups()
                log_entries.append({
                    "host": host,
                    "user name": username,
                    "time": time,
                    "request": request
                })
    return log_entries


# Validation function written by the course instructor to validate the above code
assert len(logs()) == 979

one_item = {'host': '146.204.224.152',
            'user_name': 'feest6811',
            'time': '21/Jun/2019:15:45:24 -0700',
            'request': 'POST /incentivize HTTP/1.1'}
assert one_item in logs()
