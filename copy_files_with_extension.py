from shutil import copy
import os

to_dir = '/to/dir'
from_dir = '/from/dir'
extension = '.extension' # Any file extension such as .py, .csv or .gif

''' Move files with conditions '''
for root, subdirs, files in os.walk(from_dir):
    for file in files:
        path = os.path.join(root, file)
        if path.endswith(extension):
            copy(path, to_dir)
