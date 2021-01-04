# FASTRAL

## Description
FASTRAL is a novel approach for running [ASTRAL](https://github.com/smirarab/ASTRAL), a widely used and popular species tree reconstruction method. FASTRAL runs up to ~800 times faster than ASTRAL but with a similar (or sometimes better) accuracy.

## Getting Started
To download FASTRAL, use the following command:

```pip install FASTRAL```

Alternatively, you can clone this repo and run fastral_infer.py (see the bottom of this page).

## Usage
To get a quick help on the required flags for running ASTRAL, run:

```fastral -h```

The required flags for running FASTRAL are described below:

* --ns: Number of sub-samples to be created. To specify multiple samples (containing different number of gene trees) use comma separated values
* --nt: Number of trees per sample, if there are multiple samples use comma separated values
* --k: Total number of input gene trees.
* --it: Path to input gene trees
* --os: Path for writing sampled trees
* --aggregate: Path for writing aggregated species trees
* --o: Path for writing FASTRAL output species tree
* --time: Path for writing running times

The following flags are optional:
* --rep: If specified, samples are created with replacement | Default (if not specified): Samples are created without replacement
* --path_ASTRID: path to ASTRID's runtime | Default: linux runtime of ASTRID-2 ([version untagged-fdc5326080d364b87c5a](https://github.com/pranjalv123/ASTRID/releases/tag/untagged-fdc5326080d364b87c5a)) is used
* --path_ASTRAL: Path to ASTRAL's runtime | Default: modified ASTRAL 5.7.3 is used
* --heuristics: Heuristics level of ASTRAL (See ASTRAL's manual) | Default: 0
* --multi: Required if input gene trees contain multiple individuals. Specify the path to the mapping file
* --incomp_id: (In multi-individual mode; optional) Path to a file containing the IDs of incomplete gene trees (zero-based). If specified, sampling step makes sure that each sub-sample contains at least one complete gene trees.
