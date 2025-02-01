""" 
run_simulation.py

This module contains functions to run Monte Carlo simulations for different 
seeds and save the results to CSV files. 

Functions:
    - run_simulation_for_seed(seed: int, 
                            n_replications: int, 
                            n_values: list[int], 
                            beta_mean: float, 
                            mu_sigma_params: Dict[str, np.ndarray], 
                            output_dir: str):
        Runs Monte Carlo for a given seed and saves the results
"""


import numpy as np
import pandas as pd
import pyfixest as pf

from pathlib import Path
from typing import Dict
 
from data_generation.generate_data import generate_data

def run_simulation_for_seed(seed: int, 
                            n_replications: int, 
                            n_values: list[int], 
                            beta_mean: float, 
                            mu_sigma_params: Dict[str, np.ndarray], 
                            output_dir: str):
    """
    Runs Monte Carlo simulations for a specific seed and saves results to a CSV file.

    Parameters:
    - seed (int): Random seed for reproducibility.
    - n_replications (int): Number of replications per seed.
    - n_values (list[int]): Different values of `n_units` to simulate.
    - beta_mean (float): Average coefficient value for generating data.
    - mu_sigma_params (Dict[str, np.ndarray]): Dictionary containing:
            - "mu_plus" (np.ndarray): Mean for covariates when effect is +1.
            - "mu_minus" (np.ndarray): Mean for covariates when effect is -1.
            - "sigma_plus" (np.ndarray): Covariance for X when effect is +1.
            - "sigma_minus" (np.ndarray): Covariance for X when effect is -1.
    - output_dir (str): Directory to save the CSV file.
    """
    results = []
    
    for n_units in n_values:
        for replication in range(n_replications):
            # Generate data
            data = generate_data(n_units, 
                                 beta_mean, 
                                 mu_sigma_params, 
                                 seed=seed + replication,
                                 )

            # Fit models
            try:
                fit_no_effect = pf.feols("outcome ~ covariate", data=data, drop_intercept=True)
                fit_effect = pf.feols("outcome ~ covariate|Unit", data=data)
                
                # Collect results
                results.append({
                    "seed": seed,
                    "replication": replication,
                    "n_units": n_units,
                    "model": "no_effects",
                    "coef_est": fit_no_effect.coef().iloc[0],
                    "ci_lower": fit_no_effect.confint().iloc[0, 0]
                })
                results.append({
                    "seed": seed,
                    "replication": replication,
                    "n_units": n_units,
                    "model": "fixed_effects",
                    "coef_est": fit_effect.coef().iloc[0],
                    "ci_lower": fit_effect.confint().iloc[0, 0]
                })
            except Exception as e:
                print(f"Error during fit (seed={seed}, n_units={n_units}, replication={replication}): {e}")

    # Save results to CSV
    output_file = Path(output_dir) / f"results_seed_{seed}.csv"
    pd.DataFrame(results).to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")