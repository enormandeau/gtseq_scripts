# Apply filters to SNPs based on flanking SNPs and sequence properties

# Cleanup
rm(list=ls())

# Modules
#library(tidyverse)
library(data.table)

# Load data
d = fread("../afds_chr1_min0.4.scored.tsv")

# Plot columns of interest to explore filter thresholds
dsub = d
dsub = dsub[, -c("Position", "Chrom", "Position2", "Chrom2", "Major", "Minor", "Ancestral", "SequenceMod", "Sequence", "NumSamples")]
plot(dsub[1:10000, ], pch=19, col="#00000011", cex=0.5)

# Set thresholds
max_SumMAFs = 2
max_NumSNPs = 5
min_complexity = 100
min_GCcontent = 0.2
max_GCcontent = 0.8

# Filter
d = d[d$SumMAFs <= max_SumMAFs &
        d$NumSNPs <= max_NumSNPs &
        d$Complexity >= min_complexity &
        GCcontent >= min_GCcontent &
        GCcontent <= max_GCcontent, ]

# Plot after filters
dsub = d[, -c("Position", "Chrom", "Position2", "Chrom2", "Major", "Minor", "Ancestral", "SequenceMod", "Sequence", "NumSamples")]
plot(dsub[1:10000], pch=19, col="#00000004", cex=0.5)

# Write file
write.table(d, "../afds_chr1_min0.4.scored.good.tsv", quote=F, row.names=F, sep="\t")
