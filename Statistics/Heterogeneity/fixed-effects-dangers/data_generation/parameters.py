"""
parameters.py

This module contains the constants used for the simulation.

Constants:
- BETA_MEAN (float): Mean value for the slope used in the simulation. 
- N_REPLICATIONS (int): Number of replications for each seed.
- N_VALUES (numpy.ndarray): Array of values representing different sample sizes for the simulation.
- OUTPUT_DIR (str): Directory where the simulation results will be saved.
- SEEDS (list of int): List of seeds for random number generation to ensure reproducibility.
"""

import numpy as np

# Simulation parameters
BETA_MEAN = -0.25
N_REPLICATIONS = 200
N_VALUES = np.concatenate((np.arange(100, 1000, 50), [1000, 2000, 5000, 10000]))
SEEDS = [1000, 2000, 3000, 40000, 5000, 6000, 7000, 8000]


# Output directory
OUTPUT_DIR = "simulation_results"