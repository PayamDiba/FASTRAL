"""
@author: Payam Dibaeinia
"""

import numpy as np
import pandas as pd
from collections import defaultdict
import os


class gtSampler (object):

    def __init__(self, nTree, nSample, k, replacement = True):
        """
        nTree and nSample are assumed to be a python list
        """
        self.nTree = nTree
        self.nSample = nSample
        self.replacement = replacement
        self.k = k

    def create_samples(self, path_read, path_write):
        """
        path_read: path to the input gene tree to create samples from
        path_write: path to the ouput directory were sampled trees will be written
        """
        last_ID = 0
        for curr_nSample, curr_nTree in zip (self.nSample, self.nTree):
            self._sample(curr_nSample, curr_nTree, last_ID, path_read, path_write)
            last_ID += curr_nSample



    def _sample (self, num_samples, tree_per_sample, last_sample_ID, path_read, path_write):
        """
        path_read: path to the input gene tree to create samples from
        path_write: path to the ouput directory were sampled trees will be written
        """

        for s in range(num_samples):
            os.mkdir(path_write + '/Sample_' + str(s + last_sample_ID))
            gtIDs = np.random.choice(self.k, size = tree_per_sample, replace = self.replacement)
            with open(path_write + '/Sample_' + str(s + last_sample_ID) + '/sampledGeneTrees', 'w') as fw:
                with open(path_read) as fr:
                    for lID, l in enumerate(fr):
                        if lID in gtIDs:
                            fw.write(l.strip())
                            fw.write('\n')
