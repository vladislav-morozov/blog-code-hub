"""
main.py

Runs simulations comparing the pooled OLS estimator and FE estimator with unit effects.

Blog post: "Why Fixed Effects Are Not a Silver Bullet"
Post Link: https://vladislav-morozov.github.io/blog/statistics/heterogeneity/2025-02-01-fixed_effects_danger/

Author: Vladislav Morozov 

Steps:
1. Load parameters and set up simulation configurations.
2. Run Monte Carlo simulations in parallel for multiple sample sizes.
3. Save and combine simulation results into a single output file.

Outputs:
- `simulation_results/combined_results.csv`: Aggregated simulation results.

Usage:
Run the script using:
    python main.py
"""

import os
import numpy as np
import pandas as pd
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from data_generation.moment_conditions import (
    constraints,
    param_initial_guess,
    process_mu_sigma_params, 
    sim_moment_conditions, 
)
from data_generation.parameters import (
    BETA_MEAN,  
    OUTPUT_DIR,
    N_REPLICATIONS, 
    N_VALUES, 
    SEEDS, 
)
from gmm_solver.solver import GMMSolver
from simulation.run_simulation import run_simulation_for_seed
from utils.combine_results import combine_results

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def main() -> None:
    """Main function to run simulations in parallel and combine results."""
    
    # Compute simulation parameters using GMM solver
    solver_dgp_params = GMMSolver(
        sim_moment_conditions,
        param_initial_guess,
        constraints, 
        process_func=process_mu_sigma_params,
    )
    solver_dgp_params.minimize()
    mu_sigma_params = solver_dgp_params.process_solution()

    # Run simulations in parallel
    with ProcessPoolExecutor() as executor:
        futures = [
            executor.submit(
                run_simulation_for_seed, 
                seed, 
                N_REPLICATIONS,
                N_VALUES, 
                BETA_MEAN, 
                mu_sigma_params,
                OUTPUT_DIR,
            )
            for seed in SEEDS
        ]

    # Combine results
    combine_results(OUTPUT_DIR, SEEDS)
    print("All results combined and saved to combined_results.csv")

if __name__ == "__main__":
    main()