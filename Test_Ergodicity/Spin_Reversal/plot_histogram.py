import numpy as np
import matplotlib.pyplot as plt


unique_strings=['011110111001000010110101100001010000', '011111000111000011001110010000000011', '101011110110010100001000011110100000', '101101101011011000010010001001000101', '110011011101100101000000100100011010', '110100111110101000100001000010101100', '011110110110000010101101010010100000', '101011111001010100010000101101010000', '110101001111101001000010000000001111']
color1="#66c2a6"
color2="#fc8e62"
color3="#8ea0cb"

data = open("degeneracies_loop.txt", "r")
tmp = {}
for row in data:
    row = row.split(" ")
    tmp[row[5].replace("\n","")] = int(row[4])

degeneracy_states = []
degeneracy_states_err = []
for state in unique_strings:
    degeneracy_states.append(tmp[state])
    degeneracy_states_err.append(np.sqrt(tmp[state]))
data.close()
degeneracy_states = np.array(degeneracy_states)
degeneracy_states_err = np.array(degeneracy_states_err)

total_degeneracy = len(degeneracy_states)
N = np.sum(degeneracy_states)
print("Total number of samples")
print(N)
print("Total unique states")
print(len(degeneracy_states))

xplot = np.zeros(len(degeneracy_states))
uniform_samples = np.zeros(len(degeneracy_states))
uniform_samples_err_p = np.zeros(len(degeneracy_states))
uniform_samples_err_m = np.zeros(len(degeneracy_states))
for i in range(len(degeneracy_states)):
    xplot[i] = i
    uniform_samples[i] = N/len(degeneracy_states)
    uniform_samples_err_p[i] = N/len(degeneracy_states) + np.sqrt(N/len(degeneracy_states))
    uniform_samples_err_m[i] = N/len(degeneracy_states) - np.sqrt(N/len(degeneracy_states))

print("Mean QUBO = ", np.mean(degeneracy_states), " Std: ", np.std(degeneracy_states))

bins = [-0.5+i for i in range(total_degeneracy +1)]
ticks = [i for i in range(total_degeneracy)]
plt.figure(figsize=(5,2.5))
plt.hist(ticks[:6], bins=bins,histtype='bar', color=color3, ec='black', weights=degeneracy_states[:6])
plt.hist(ticks[6:], bins=bins,histtype='bar', color=color1, ec='black', weights=degeneracy_states[6:])
plt.fill_between([bins[0], bins[total_degeneracy ]], [uniform_samples_err_p[0],uniform_samples_err_p[0]], [uniform_samples_err_m[0],uniform_samples_err_m[0]], color=color2, alpha=0.5)
plt.plot([bins[0], bins[total_degeneracy ]], [uniform_samples[0],uniform_samples[0]], color=color2, alpha=0.75)
plt.xlabel("Microstate", fontsize=9)
plt.ylabel("Counts", fontsize=9)
plt.xticks([i for i in range(total_degeneracy)], [str(i+1) for i in range(total_degeneracy)], fontsize=8)
plt.yticks(fontsize=8)
plt.title("2x2x2 Lattice", fontsize=10)
plt.savefig('Histogram_ergodicity_L2x2x2.png',dpi=300, bbox_inches = "tight")

