from shutil import copy
import os

to_dir = '/to/directory'
from_dir = '/from/directory'

''' Move files without conditions '''
for root, subdirs, files in os.walk(to_dir):
    for file in files:
        path = os.path.join(root, file)
        copy(path, to_dir)

''' Move files with conditions '''
for root, subdirs, files in os.walk(to_dir):
    for file in files:
        path = os.path.join(root, file)
        if path.endswith('.csv'):  # Any file such as .py or .gif
            copy(path, to_dir)