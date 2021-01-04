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
