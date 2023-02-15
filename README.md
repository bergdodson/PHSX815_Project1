# PHSX815_Project1
My code and LaTeX file for project 1 of PHSX 815. This will answer the question of whether people go bald because of genetics and other factors, or whether it's gnomes that are stealing people's hair. 

## PHSX815_Project1
This directory contains the python code for the project. There are two python executables and their dependancies. One executable is responsible for generating the random number distributions and writing them to file. The other executable reads in the flagged file and plots it. The directory also includes .txt files of recorded random number distributions that were used for testing the code as well as the final distributions that were used in the end. 

### Proj1_Gen+Write.py
This contains the code that will create the random numbers and random number distributions. The user flags the number of measurements per experiment (-Nmeas), the number of experiments (-Nexp), -the hypothesis rate (-rate), the random number seed (-seed), and the filename of the file they want to record the data to (-output).   It is heavily influenced by the code that Dr. Rogan shared with us in the course for HW4. 

### Proj1_Read+Plot.py 
This contains the code that will read in the random number distributions and plot them. This is run with by including the filename of the file to be analyzed as one of the system flags. This is mostly based on the work that we did for HW 4.

### Dependancies
**MySort.py**: Used to sort the random numbers in Proj1_Read+Plot.py. Modified from the code provided by Dr. Rogan.
**Random.py**: Used to create random numbers and random number distributions Proj1_Gen+Write.py. Copied from the code provided by Dr. Rogan.

### Python Packages
**sys**: Used to read in the command line flags when running the exicutables.
**numpy**: Used to calculate the standard deviation and mean of the distributions. This is also used to produce the random numbers. 
**matplotlib**: Used to produce the plots.
**scipy.stats**: Used originally to calculate the confidance intervals and like. 
**math**: Included for good measure.

## pdf
This directory contains the latest version of the latex file writeup.
