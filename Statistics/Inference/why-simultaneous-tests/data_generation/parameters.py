"""
parameters.py

This module contains the constants used for the simulation.

Constants:
- C_RANGE (np.array): range of values for coefficients on covariates
- NUM_OBSERVATIONS (int): number of observations in each sample.
- NUM_REPLICATIONS (int): number of replications per seed.
- OUTPUT_DIR (str): directory where the simulation results will be stored.
- RHO_RANGE (np.array): range of correlations between covariates.
- SEEDS (np.array): List of seeds for random number generation to
    ensure reproducibility.
"""

import numpy as np

# Simulation parameters
NUM_OBSERVATIONS = 200
NUM_REPLICATIONS = 150
SEEDS = np.linspace(1000, 16000, 16).astype(int)

# DGP parameters
C_RANGE = np.linspace(-3, 3, 401)
RHO_RANGE = np.linspace(-0.99, 0.99, 100)

# Output directory
OUTPUT_DIR = "simulation_results"
