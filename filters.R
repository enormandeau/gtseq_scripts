# Cleanup
rm(list=ls())

# Modules
#library(tidyverse)
library(data.table)

# Load data
d = fread("selected_loci.scored.tsv")

# Plot columns of interest to explore filter thresholds
dsub = d
dsub = dsub[, -c("Position", "Chrom", "Position2", "Chrom2", "Major", "Minor", "Ancestral", "SequenceMod", "Sequence", "NumSamples")]
plot(dsub[1:10000, ], pch=19, col="#00000004", cex=0.5)
    
# Filtres
d = d[d$SumMAFs <= 2 & d$NumSNPs <= 5 & d$Complexity >= 100 & GCcontent > 0.2 & GCcontent < 0.5, ]

# Plot after filters
dsub = d[, -c("Position", "Chrom", "Position2", "Chrom2", "Major", "Minor", "Ancestral", "SequenceMod", "Sequence", "NumSamples")]
plot(dsub, pch=19, col="#00000004", cex=0.5)

# Write file
write.table(d, "selected_loci.scored.good.tsv", quote=F, row.names=F, sep="\t")
