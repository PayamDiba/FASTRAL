"""
@author: Payam Dibaeinia
"""

import numpy
import shutil
from Sampler import gtSampler
import time
import pandas as pd
import os


class ASTRALID (object):

    def __init__(self, flags):

        self.flags_ = flags

        print("START BUILDING SAMPLES ... ", flush=True)
        sampler = gtSampler(nTree = flags.nt, nSample = flags.ns, replacement = flags.rep)
        sampler.create_samples(path_read = flags.it, path_write = flags.os)

        self.path_samples = self.flags_.os + '/Sample_'

    def run(self):
        t1 = time.time()
        self._run_ASTRID()
        t2 = time.time()

        self._aggregate_ASTRID_trees()

        t3 = time.time()
        self._run_ASTRAL()
        t4 = time.time()

        """
        write running times
        """
        header = ['number_samples', 'number_tree_per_sample', 'ASTRID_time', 'ASTRAL_time', 'total_time']
        df = pd.DataFrame([[self.flags_.ns, self.flags_.nt, t2-t1, t4-t3, t2-t1 + t4-t3]])
        df.to_csv(self.flags_.time, header = header, sep = '\t', index = False)


    def _run_ASTRID(self):

        print("START RUNNING ASTRID ... ", flush=True)
        cline = self.flags_.path_ASTRID + ' -i ' + self.path_samples

        for s in range(self.flags_.ns):
            curr_cline = cline + str(s) + '/sampledGeneTrees -o ' + self.path_samples + str(s) + '/ASTRID_species_tree_' + str(s)
            print("     Running ASTRID on sample " + str(s), flush=True)
            status = os.system(curr_cline)
            if status < 0:
                raise ValueError('ASTRID was not run successfully')

    def _aggregate_ASTRID_trees(self):

        print("START AGGREGATING ASTRID's OUTPUTS ... ", flush=True)

        with open(self.flags_.aggregate,'wb') as wf:
            for s in range(self.flags_.ns):
                path = self.path_samples + str(s) +'/ASTRID_species_tree_' + str(s)
                with open(path,'rb') as rf:
                    shutil.copyfileobj(rf, wf)

    def _run_ASTRAL(self):

        cline = 'java -jar ' + self.flags_.path_ASTRAL + ' -i ' + self.flags_.it + ' -f ' + self.flags_.aggregate + ' -p ' + str(self.flags_.heuristics) + ' -o ' + self.flags_.o
        print("START RUNNING ASTRAL ... ", flush=True)
        status = os.system(cline)
        if status < 0:
            raise ValueError('ASTRID was not run successfully')
