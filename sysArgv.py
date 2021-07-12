import sys
import os

dir = sys.argv[1]   # python3 sysArgv.py items/   dir is 'items/'

if not os.path.exists(dir):
    os.makedirs(dir)

for item in os.listdir(dir):
    print(item)