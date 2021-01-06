# FASTRAL

## Description
FASTRAL is a novel approach for running [ASTRAL](https://github.com/smirarab/ASTRAL), a widely used and popular species tree reconstruction method. FASTRAL runs up to ~800 times faster than ASTRAL but with a similar (or sometimes better) accuracy.

## Dependencies
FASTRAL can run on Linux or mac OS machines with Python 3 installed.

## Getting Started
To download FASTRAL, use the following command:

```pip install FASTRAL```

## Usage
To get a quick help on the required flags for running FASTRAL, run:

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
* --path_ASTRID: path to ASTRID's runtime | Default: ASTRID-2 ([version untagged-fdc5326080d364b87c5a](https://github.com/pranjalv123/ASTRID/releases/tag/untagged-fdc5326080d364b87c5a)) is used
* --path_ASTRAL: Path to ASTRAL's runtime | Default: modified ASTRAL 5.7.3 is used
* --heuristics: Heuristics level of ASTRAL (See ASTRAL's manual) | Default: 0
* --multi: Required if input gene trees contain multiple individuals. Specify the path to the mapping file
* --incomp_id: (In multi-individual mode; optional) Path to a file containing the IDs of incomplete gene trees (zero-based). If specified, sampling step makes sure that each sub-sample contains at least one complete gene trees.

## Running on multi-individual datasets
When input gene trees contain multiple individuals per species, FASTRAL requires a mapping file to be passed with ```--multi``` flag. This mapping file should have one line per species in the following format:

```
species_name: individual_1, individual_2, ...
```

An example of mapping file is provided in the ```example/data``` directory.

Also, if missing data is present and sub-samples containing at least one complete gene tree is required, the IDs of incomplete gene trees can be passed to FASTRAL using ```--incomp_id``` flag. IDs are indices (zero-based) of incomplete gene trees and this file should have one ID per line. An example of such missing_ids file is provided in the ```example/data``` directory.

## Example
We provided an example multi-individual data with 5 individuals per species in ```example/data``` directory. 1000 input gene trees (genes.gtr), mapping and missing_ids files are provided. Use the following command to run FASTRAL on this data. Here, we chose to create 51 sub-samples, one of which has all the 1000 gene trees, 10 of which each have 500 gene trees, 20 of which each have 250 gene trees and the remaining 20 samples each contain 100 gene trees:

```fastral --ns 1,10,20,20 --nt 1000,500,250,100 --k 1000 --it {PATH-TO}/example/data/genes.gtr --os {PATH-TO}/example/out/samples --aggregate {PATH-TO}/example/out/combined_trees.tre --o {PATH-TO}/example/out/final_species_tree.tre --time {PATH-TO}/out/time.log --multi {PATH-TO}/example/data/mapping```
