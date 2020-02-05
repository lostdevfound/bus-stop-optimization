head -n1 lda_000a16a_e.json > bc_subset_map.json #copy the first line to the new file
grep 'Colombie-Britannique' lda_000a16a_e.json >> bc_subset_map.json # Copy all features that have BC in them
sed -i '$s/,$//' bc_subset_map.json # remove comma from last line
tail -n1 lda_000a16a_e.json   >> bc_subset_map.json # copy last line to new file