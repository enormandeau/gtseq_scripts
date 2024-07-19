# GTseq scripts

Scripts used in step 6 for the "SNP selection" of the Beemelman *et al.* paper
(see Reference section) to design GTseq panels for three salmonid species

# TODO

- Add command before `05_select_best_SNPs_pairwise.py` to extract just the
  wanted lines from the AFD file
- Test and add bash commands for test

## Reference

TODO: Add reference to paper once available

## Overall workflow

Click on the following schema of the workflow to see a larger version

![Schema of the workflow](02_data/workflow_figure.png)

## Description of scripts

Below, each script is described briefly in order of use with the commands that
can be used to run all the scripts on the test dataset found in `02_data`. The
Python scripts can be launched without arguments to print their documentation
strings. The R script should be run interactively, for example in RStudio, to
decide on the thresholds for the filters before applying them.

### Compute pairwise AFD values

`01_compute_pairwise_AFDs.py`: Starting from MAF values in each group, compute
all pairwise AFD values.

### Subset SNPs to keep only these with high AFDs

`02_pre_filter_SNPs_on_pairwise_AFDs.py`: Keep only SNPs for which the maximum
pairwize AFD value is above a given threshold.

### Extract information about potential SNPs

`03_score_SNPs_for_GTseq.py`: For each SNP of interest, extract information
about flanking SNPs, sequence complexity and GC content, etc.

### Filter SNPs based on extracted information

`04_filter_SNPs.R`: Apply filters to SNPs based on flanking SNPs and sequence
properties

### Select best panel to maximize group differentiation

`05_select_best_SNPs_pairwise.py`: Choose the best SNPs for all pairs of
     populations

## License

CC share-alike

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">gtseq_scripts</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Eric Normandeau</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
