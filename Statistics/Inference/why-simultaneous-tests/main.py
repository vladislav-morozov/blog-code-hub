"""
main.py
========

Runs simulations comparing the power of the Wald test vs. two multiple t-test
approaches in a simple linear regression with normality.

Blog Post:
-----------
- Post Link: https://vladislav-morozov.github.io/blog/statistics/inference/2025-02-01-why-joint-test/
- Author: Vladislav Morozov

Steps:
------
1. Load parameters and set up simulation configurations.
2. Run Monte Carlo simulations in parallel for multiple sample sizes.
3. Save and combine simulation results into a single output file.

Outputs:
--------
- `simulation_results/combined_results.csv`: Aggregated simulation results.

Usage:
------
Run the script using:
    py main.py
or
    python main.py

"""


import os

from concurrent.futures import ProcessPoolExecutor

from data_generation.parameters import (
    C_RANGE,
    NUM_OBSERVATIONS,
    NUM_REPLICATIONS,
    OUTPUT_DIR,
    RHO_RANGE,
    SEEDS,
)
from simulation.run_simulation import run_simulation_for_seed
from utils.combine_results import combine_results

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)


# Run simulations in parallel
def main():
    """Main function to run the simulation and combine results"""
    with ProcessPoolExecutor() as executor:
        [
            executor.submit(
                run_simulation_for_seed,
                seed,
                NUM_REPLICATIONS,
                NUM_OBSERVATIONS,
                C_RANGE,
                RHO_RANGE,
                OUTPUT_DIR,
            )
            for seed in SEEDS
        ]

    # Combine results
    combine_results(OUTPUT_DIR, SEEDS)
    print("All results combined and saved to combined_results.csv")


if __name__ == "__main__":
    main()
