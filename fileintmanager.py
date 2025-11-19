#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import hashlib
import time

MONITOR_FOLDER = "/Users/Owner/Desktop/MONITOR_FOLDER"  
CHECK_INTERVAL = 5 

file_hashes = {}

def hash_file(filepath):
    """Return SHA256 hash of a file."""
    sha = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(8192):
                sha.update(chunk)
        return sha.hexdigest()
    except FileNotFoundError:
        return None

def scan_folder():
    """Scan folder and detect changes."""
    global file_hashes
    current_files = {}

    for root, dirs, files in os.walk(MONITOR_FOLDER):
        for file in files:
            path = os.path.join(root, file)
            current_files[path] = hash_file(path)

    for path, hash_value in current_files.items():
        if path not in file_hashes:
            print(f"[NEW] File added: {path}")
        elif file_hashes[path] != hash_value:
            print(f"[MODIFIED] File changed: {path}")

    for path in file_hashes:
        if path not in current_files:
            print(f"[DELETED] File removed: {path}")

    file_hashes = current_files.copy()


print(f"Monitoring folder: {MONITOR_FOLDER}")
while True:
    scan_folder()
    time.sleep(CHECK_INTERVAL)

