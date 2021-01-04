"""
@author: Payam Dibaeinia
"""

import argparse
from FASTRAL.fastral import FASTRAL
from FASTRAL.utils import make_dir




def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--ns', type=str, default=None, help='number of samples, input multiple sample sizes with comma separated values', required = True)
    parser.add_argument('--nt', type=str, default=None, help='number of trees per sample, if there are multiple samples use comma separated values', required = True)
    parser.add_argument('--k', type=int, default=None, help='total number of input gene trees', required = True)
    parser.add_argument('--it', type=str, default=None, help='path to input gene trees', required = True)
    parser.add_argument('--os', type=str, default=None, help='path to samples folders to write sampled trees', required = True)
    parser.add_argument('--aggregate', type=str, default=None, help='path to write aggeregated species trees', required = True)
    parser.add_argument('--o', type=str, default=None, help='path to write FASTRAL output species tree', required = True)
    parser.add_argument('--time', type=str, default=None, help='path to write running times', required = True)
    parser.add_argument('--rep', action='store_true', help='whether draw samples with replacement | Default: False', required = False)
    parser.add_argument('--path_ASTRID', type=str, default='ASTRID/ASTRID-linux', help='path to ASTRID | Default: linux runtime of ASTRID-2 (version untagged-fdc5326080d364b87c5a) is used (see: https://github.com/pranjalv123/ASTRID/releases/tag/untagged-fdc5326080d364b87c5a)', required = False)
    parser.add_argument('--path_ASTRAL', type=str, default='ASTRAL-modified/astral.5.7.3.jar', help='path to ASTRAL | Default: modified ASTRAL 5.7.3 is used', required = False)
    parser.add_argument('--heuristics', type=int, default=0, help='heuristics level of ASTRAL | Default: 0', required = False)
    parser.add_argument('--multi', type=str, default=None, help='if input gene trees contain multiple individuals, specify the path to the mapping file', required = False)
    parser.add_argument('--incomp_id', type=str, default=None, help='(Optional) Path to a file containing the IDs of incomplete gene trees. If specified, sampling step makes sure that each sub-sample contains complete gene trees.', required = False)

    FLAGS = parser.parse_args()

    make_dir(FLAGS.os)
    make_dir(FLAGS.time, writable = True)
    make_dir(FLAGS.aggregate, writable = True)
    make_dir(FLAGS.o, writable = True)

    method = FASTRAL(FLAGS)
    method.run()

if __name__ == "__main__":
    main()
