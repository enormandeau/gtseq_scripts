# Cleanup
rm(list=ls())

# Modules
#library(tidyverse)
library(data.table)

# Load data
d1 = fread("../selected_loci.scored.tsv")

# Plot columns of interest
d = d1
d = d[, -c("Position", "Chrom", "Position2", "Chrom2", "Major", "Minor", "Ancestral", "SequenceMod", "Sequence", "NumSamples")]
plot(d, pch=19, col="#00000004", cex=0.5)
    
# Filtres
# SumMAF > 2
# Complexity < 90
# #SNPs >> 10

d1 = d1[d1$SumMAFs <= 2 & d1$NumSNPs <= 5 & d1$Complexity >= 100 & GCcontent > 0.2 & GCcontent < 0.5, ]
#d = d1[, -c("Position", "Chrom", "Position2", "Chrom2", "Major", "Minor", "Ancestral", "SequenceMod", "Sequence", "NumSamples")]
#plot(d, pch=19, col="#00000004", cex=0.5)

# Write files
write.table(d1, "../selected_loci.scored.good.tsv", quote=F, row.names=F, sep="\t")
