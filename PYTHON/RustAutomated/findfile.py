import os

import subprocess

driveStr = subprocess.check_output("fsutil fsinfo drives")
driveStr = driveStr.strip().lstrip('Drives: ')
drives = driveStr.split()
def find_file(target, folder):
    for f in os.listdir(folder):
        path = os.path.join(folder, f)
        if os.path.isdir(path):
            result = find_file(target, path)
            print(result)
            if result is not None:
                return result
            continue
        if f == target:
            return path


target = "steamapps"
drives = ['{}:\\' for letter in 'CDEFGHIJKLMNOPQRSTUVWXYZ']
for drive in drives:
    if os.path.isdir(drive):
        filepath = find_file(target, drive)
        
        if filepath is not None:
            break
