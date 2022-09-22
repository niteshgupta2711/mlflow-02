import os
import numpy as np

p1s = np.linspace(0,1,0.5)
p2s = np.linspace(0,1,0.5)

if __name__=='__main__':

    for p1 in p1s:
        for p2 in p2s:
            print(f"logging experiment for p1:{p1}, p2: {p2}")
            os.system(f"python demo.py -a {p1} -l1 {p2}")