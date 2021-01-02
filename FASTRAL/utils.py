"""
@author: Payam Dibaeinia
"""

import os


def make_dir(path, writable = False):
    """
    writable: determines if the given path points to a readable/writable file, if
    so, only the intermidiate folders are made
    """
    if os.path.exists(path):
        print("directory " + path + " already exists", flush = True)

    if writable:
        path_list = path.split('/')[:-1]

        if path[0] == '/':
            path = '/' + '/'.join(path_list)
        else:
            path = '/'.join(path_list)

    if not os.path.exists(path):
        os.makedirs(path)
