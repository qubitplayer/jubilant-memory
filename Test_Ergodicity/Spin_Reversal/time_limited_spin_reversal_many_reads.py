from dwave.system import DWaveSampler, EmbeddingComposite
import numpy as np

h = np.loadtxt('h.txt')
J = np.loadtxt('J.txt')

sampler = EmbeddingComposite(DWaveSampler(solver={'qpu': True}))

lim=0
outputname = "Outputs_2000_spin_reversal_many_reads.txt"

results = sampler.sample_ising(h,J, annealing_time=2000, num_reads=1000, num_spin_reversal_transforms=1000)

out = open(outputname, 'a')
for j in range(len(results.record)):
    print("Energy = ", results.record[j][1])
    print(results.info)
    out.write(str(results.info)+"\t"+str(len(results.record))+"\n")
    out.write(str(list(results.record[j][0]))+"\t"+str(results.record[j][1])+"\n")
    print(results)
    
out.close()
