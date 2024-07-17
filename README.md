# GTseq scripts

Scripts used in step 6 "SNP selection" of the Beemelman et al. paper (see
Reference section) to design GTseq panels for three salmonid species

# TODO

- Rename and reorder scripts
- Add sample file to test scripts
- Add bash commands for test
- Add reference to article (bioRxiv?)
- Add License

## Overall pipeline

Click on the following schema of the pipeline to see a larger version

![Schema of the pipeline](pipeline.png)

## Description of scripts

### `01_compute_pairwise_AFDs.py`

Compute and report all pairwise AFDs based on MAFs

### `02_pre_filter_SNPs_on_pairwise_AFDs.py`

Keep only SNPs for which at least 1 population pair has a high enough AFD

### `03_select_best_SNPs_pairwise.py`

Choose the best SNPs for all pairs of populations

For each pair of populations:

- sort the AFDs by decreasing order
- Pick the top ones (if they are not too close to previously picked SNPs)
- Go down the list until you have reached `target_sum` <float>
- Continue for following populations

### `04_score_SNPs_for_GTseq.py`

Score subset of SNPs chosen by Raphael according to the presence of neighbouring SNPs.

- Less or no SNPs in the surrounding region is best
- SNPs with low MAFs are not as bad

### `05_filter_SNPs.R`

Keep only SNPs that pass certain criteria:

- Maximum number of flanking SNPs
- Maximum sum of MAF for flancking SNPs
- Minimum sequence complexity
- Minimum and maximum GC content

## Reference

## License
