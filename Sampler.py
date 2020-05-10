import numpy as np
import pandas as pd
from collections import defaultdict
import os


class gtSampler (object):

    def __init__(self, nTree, nSample, replacement = True):
        self.nTree = nTree
        self.nSample = nSample
        self.replacement = replacement

    def create_samples (self, path_read, path_write):
        """
        path_read: path to the input gene tree to create samples from
        path_write: path to the ouput directory were sampled trees will be written
        """

        self._readInputGT(path_read)
        self._buildSamples()
        self._writeSamples(path_write)


    def _readInputGT (self, path_read):
        self.allGTs = []
        with open(path_read) as f:
            for l in f:
                self.allGTs.append(l.strip())

        self.k = len(self.allGTs) # holds the number of input gene trees

    def _buildSamples(self):
        self.samplesDict = {}

        for s in range(self.nSample):
            gtIDs = np.random.choice(self.k, size = self.nTree, replace = self.replacement)
            self.samplesDict[s] = np.take(self.allGTs, gtIDs, axis = 0)

    def _writeSamples(self, path_write):
        for s in range(self.nSample):
            currTrees = self.samplesDict[s]

            os.makedirs(path_write + '/Sample_' + str(s))
            with open(path_write + '/Sample_' + str(s) + '/sampledGeneTrees', 'w') as f:
                for t in currTrees:
                    f.write(t)
                    f.write('\n')
