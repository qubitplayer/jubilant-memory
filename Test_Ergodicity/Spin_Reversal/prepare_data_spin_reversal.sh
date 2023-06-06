grep "]	-31.0" Outputs_2000_spin_reversal.txt | sed 's/, //g' | awk '{print $1}' | sed 's/-1/0/g' | sed 's/\[//g' | sed 's/\]//g' > configurations_spin_reversal.txt
sort configurations_spin_reversal.txt | uniq -c > degeneracies_spin_reversal.txt
python plot_histogram_spin_reversal.py
