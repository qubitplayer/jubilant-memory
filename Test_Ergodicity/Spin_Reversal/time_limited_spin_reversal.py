from dwave.system import DWaveSampler, EmbeddingComposite
import numpy as np

h = np.loadtxt('h.txt')
J = np.loadtxt('J.txt')

sampler = EmbeddingComposite(DWaveSampler(solver={'qpu': True}))

outputname = "Outputs_2000_spin_reversal.txt"
for i in range(1000):
    out = open(outputname, 'a')

    results = sampler.sample_ising(h,J, annealing_time=2000, num_reads=1, num_spin_reversal_transforms=1)

    print("Energy = ", results.record[0][1])
    print(results.info)
    out.write(str(results.info)+"\n")
    out.write(str(list(results.record[0][0]))+"\t"+str(results.record[0][1])+"\n")
    print(results)
    out.close()
