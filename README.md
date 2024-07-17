# GTseq scripts

Main scripts used to design GTseq panels for three salmonid species

## Overall pipeline

Click on the following schema of the pipeline to see a larger version

![Schema of the pipeline](pipeline.png)

## Description of scripts

### `00_pre_filter_snps_based_on_pairwise_afds.py`

Keep only SNPs for which at least 1 population pair has a high enough AFD

### `01_compute_pairwise_AFDs.py`

Compute and report all pairwise AFDs based on MAFs

### `02_select_best_snps_pairwise.py`

Choose the best SNPs for all pairs of populations

For each pair of populations:

- sort the AFDs by decreasing order
- Pick the top ones (if they are not too close to previously picked SNPs)
- Go down the list until you have reached `target_sum` <float>
- Continue for following populations

### `03_score_snps_for_gtseq.py`

Score subset of SNPs chosen by Raphael according to the presence of neighbouring SNPs.

- Less or no SNPs in the surrounding region is best
- SNPs with low MAFs are not as bad

### `filters.R`

Keep only SNPs that pass certain criteria:

- Maximum number of flanking SNPs
- Maximum sum of MAF for flancking SNPs
- Minimum sequence complexity
- Minimum and maximum GC content
