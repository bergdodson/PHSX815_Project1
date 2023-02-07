#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt
#import Random as ran

# import our Random class from python/Random.py file
# Wasn't finding the working dir, so included that in the append command
sys.path.append("C:\\Users\\bergd\\Desktop\\github\\PHSX815_Week2") #For running on Windows
sys.path.append('/mnt/c/Users/bergd/Desktop/github/PHSX815_Week2')  #For running on terminal in Linux 
#print(sys.path)
from HW3.Random import Random

# main function for our coin toss Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print
        sys.exit(1)

    # default seed
    seed = 5555

    # default single coin-toss probability for "1"
    prob = 0.5

    # default number of coin tosses (per experiment)
    Ntoss = 1

    # default number of experiments
    Nexp = 1

    # output file defaults
    doOutputFile = False

    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-prob' in sys.argv:
        p = sys.argv.index('-prob')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            prob = ptemp
    if '-Ntoss' in sys.argv:
        p = sys.argv.index('-Ntoss')
        Nt = int(sys.argv[p+1])
        if Nt > 0:
            Ntoss = Nt
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            Nexp = Ne
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True

    # class instance of our Random class using seed
    random = Random(seed)

    
    #Generating the random number distribution
    if doOutputFile:
        outfile = open(OutputFileName, 'w')
        for e in range(0,Nexp):
            numsgend = []
            for t in range(0,Ntoss):
                numsgend.append(random.LevyFlight(prob))
                outfile.write(str(numsgend[t]) + " ")
            outfile.write(" \n")
        outfile.close()
    else:
        for e in range(0,Nexp):
            numsgend = []
            for t in range(0,Ntoss):
                numsgend.append(random.LevyFlight(prob))
                print(numsgend[t], end = ' ')
            print(" ")
   
    
     #Plotting the random number distribution for each experiment
    n, bins, patches = plt.hist(numsgend, 50, density=True, facecolor='g', alpha=0.75)
 
 
    # plot formating options
    plt.xlabel('step size value')
    plt.ylabel('Occurances')
    plt.title('Levy Flight random number distribution')
    plt.grid(True)
    
    # show figure (program only ends once closed
    plt.show()
