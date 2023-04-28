# PHSX815_Project1
My code and LaTeX file for project 1 of PHSX 815. This will answer the question of whether people go bald because of genetics and other factors, or whether it's gnomes that are stealing people's hair. Please continue reading to orient yourself.

## pdf
This file contains the LaTeX writeup for this project. 

## DataSimulations
This file contains the simulated data for the project. For convenience they will be refered to as "natural.txt" for the H0 theory and "experiement.txt." The flags used to generate them are recorded (roughly) in the filename. 

## Figures
This files contains the .png files used in the LaTeX writup. There is a file for each of the simulated theories and log-likelihood ratio plot. 

## python
This file contains all the python code that was used in this project. All dependencies and influence for this code will be explained below.

### `Proj1_Gen+Write.py`
This script generates a Poisson distribution based on the rate given to it. It does this by taking flags `-seed`, `-Nmeas`, `-Nexp`, `-output`. `-seed` sets the random seed for the random number generator. `-Nmeas` sets how many measurements to make per experiment. `-Nexp` sets how many experiments will be simulated. `-output` saves the simulated data out to the file specified by the user. It is heavily influenced by the code that Dr. Rogan shared with us in the course for HW4. 

### `Proj1_Read+Plot_v2.py` 
This contains the code that will read in the random number distributions and plot them. It also calculates the mean, median, and confidence intervals. It also calculates the log-likelihood ratio and plots the results too. The user can control this script using the following flags: `-inputH0` and `-inputH1`. `-inputH0` allows the user to specify which file contains the simulated H0 theory data and `-inputH1` allows the user to do the same for the H1 theory data. This script depends on `Random.py`, `MySort.py` and the python packages `sys`, `numpy`, `matplotlib`, and `scipy`

### `MySort.py`: Used to sort the simulated data random numbers in `Proj1_Read+Plot_v2.py`. This script is a modified version of code provided by Dr. Rogan.

### `Random.py`: Used to create random numbers and random number distributions Proj1_Gen+Write.py. This is a modified version of the code provided earlier by Dr. Rogan.

## pdf
This directory contains the latest version of the latex file writeup.
