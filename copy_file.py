from shutil import copy
import os

to_dir = '/home/dowwl/Documents/practical-sql-master/psql_csv_files'
from_dir = '/home/dowwl/Documents/practical-sql-master/Chapter_15'

''' Copy files without conditions '''
for root, subdirs, files in os.walk(from_dir):
    for file in files:
        path = os.path.join(root, file)
        copy(path, to_dir)
