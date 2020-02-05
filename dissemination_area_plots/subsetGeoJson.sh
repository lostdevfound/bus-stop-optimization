head -n1 lda_000a16a_e.json > bc_subset_map.json
grep 'Colombie-Britannique' lda_000a16a_e.json >> bc_subset_map.json
sed '$ s/,$//g' bc_subset_map.json
tail -n1 lda_000a16a_e.json   >> bc_subset_map.json