
"""
@author: Payam Dibaeinia
"""

import numpy as np
import shutil
from FASTRAL.Sampler import gtSampler
import time
import pandas as pd
import os


class FASTRAL (object):

    def __init__(self, flags):

        nt = [int(i) for i in flags.nt.split(',')]
        ns = [int(i) for i in flags.ns.split(',')]

        self.flags_ = flags
        if flags.incomp_id != None:
            incomp_id = pd.read_csv(flags.incomp_id, header = None, index_col = None)
            incomp_id = incomp_id.values.flatten()
        else:
            incomp_id = None

        print("START BUILDING SAMPLES ... ", flush=True)
        sampler = gtSampler(nTree = nt, nSample = ns, k = flags.k, replacement = flags.rep, missingID = incomp_id)
        sampler.create_samples(path_read = flags.it, path_write = flags.os)

        self.path_samples = self.flags_.os + '/Sample_'
        self.nTotalS_ = np.sum(ns)

        self.multi = None
        if self.flags_.multi:
            self.multi = ' -a {}'.format(self.flags_.multi)

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
        header = ['ASTRID_time', 'ASTRAL_time', 'total_time']
        df = pd.DataFrame([[t2-t1, t4-t3, t2-t1 + t4-t3]])
        df.to_csv(self.flags_.time, header = header, sep = '\t', index = False)


    def _run_ASTRID(self):

        print("START RUNNING ASTRID ... ", flush=True)
        cline = self.flags_.path_ASTRID + ' -i ' + self.path_samples




        for s in range(self.nTotalS_):
            curr_cline = cline + str(s) + '/sampledGeneTrees'
            if self.multi:
                curr_cline += self.multi + ' -o ' + self.path_samples + str(s) + '/ASTRID_species_tree_' + str(s)
            else:
                curr_cline += ' -o ' + self.path_samples + str(s) + '/ASTRID_species_tree_' + str(s)

            print("     Running ASTRID on sample " + str(s), flush=True)
            status = os.system(curr_cline)
            if status < 0:
                raise ValueError('ASTRID was not run successfully')

    def _aggregate_ASTRID_trees(self):

        print("START AGGREGATING ASTRID's OUTPUTS ... ", flush=True)

        with open(self.flags_.aggregate,'wb') as wf:
            for s in range(self.nTotalS_):
                path = self.path_samples + str(s) +'/ASTRID_species_tree_' + str(s)
                with open(path,'rb') as rf:
                    shutil.copyfileobj(rf, wf)

    def _run_ASTRAL(self):

        cline = 'java -jar ' + self.flags_.path_ASTRAL + ' -i ' + self.flags_.it + ' -f ' + self.flags_.aggregate + ' -p ' + str(self.flags_.heuristics) + ' -o ' + self.flags_.o
        if self.multi:
            cline += self.multi
        print("START RUNNING ASTRAL ... ", flush=True)
        status = os.system(cline)
        if status < 0:
            raise ValueError('ASTRID was not run successfully')
