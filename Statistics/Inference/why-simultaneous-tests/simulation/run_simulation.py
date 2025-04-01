"""
run_simulation.py

This module contains functions to run Monte Carlo simulations for different
seeds and save the results to CSV files.

Functions:
    - run_simulation_for_seed(
            seed: int,
            num_replications: int,
            num_observations: int,
            c_range: np.array,
            rho_range: np.array,
            output_dir: str,
        ) -> None
        Runs Monte Carlo for a given seed and saves the results
"""

import numpy as np
import pandas as pd

from pathlib import Path
from statsmodels.regression.linear_model import OLS
from statsmodels.stats.multitest import multipletests

from data_generation.generate_data import generate_data


def run_simulation_for_seed(
    seed: int,
    num_replications: int,
    num_observations: int,
    c_range: np.array,
    rho_range: np.array,
    output_dir: str,
):
    """Runs Monte Carlo simulations for a specific seed and saves as CSV.

    Args:
        seed (int): random seed for reproducibility.
        num_replications (int): number of replications per seed.
        num_observations (int): number of observations in each sample
        c_range (np.array): range of values for coefficients on covariates
        rho_range (np.array): range of correlations between covariates
        output_dir (str): directory to save the output CSV.
    """
    results = []
    for c in c_range:
        # Update coefficient vector
        betas = np.array([1, c, c])
        for rho in rho_range:
            # Update covariance matrix of covariates
            x_covar = np.array([[0, 0, 0], [0, 1, rho], [0, rho, 1]])

            # Run simulation
            for replication in range(num_replications):
                # Generate data
                data = generate_data(
                    num_observations,
                    betas,
                    np.array([1, 0, 0]),
                    x_covar,
                    1,
                    seed + replication,
                )

                # Perform tests
                try:
                    # Fit models
                    lin_reg = OLS(data.iloc[:, 0], data.iloc[:, 1:])
                    lin_reg_fit = lin_reg.fit()

                    # Perform Wald test
                    WALD_R_MATRIX = np.array([[0, 1, 0], [0, 0, 1]])
                    wald_test = lin_reg_fit.wald_test(
                        WALD_R_MATRIX,
                        use_f=False,
                        scalar=True,
                    )
                    decision_wald = wald_test.pvalue <= 0.05

                    # Use multiple t-tests
                    p_vals_t = lin_reg_fit.pvalues.iloc[1:]
                    t_test_corrected_bonf = multipletests(
                        p_vals_t,
                        method="bonferroni",  # Bonferroni
                    )
                    t_test_corrected_hs = multipletests(
                        p_vals_t,
                        method="hs",  # Holm-Sidak
                    )
                    decision_bonf = t_test_corrected_bonf[0].sum() > 0
                    decision_hs = t_test_corrected_hs[0].sum() > 0

                    # Collect results
                    results.append(
                        {
                            "seed": seed,
                            "replication": replication,
                            "c": c,
                            "rho": rho,
                            "Wald": decision_wald,
                            "Bonferroni": decision_bonf,
                            "Holm-Sidak": decision_hs,
                        }
                    )

                except Exception as e:
                    print(
                        f"Error during fit (seed={seed}): {e}"
                    )
    # Save results to CSV
    output_file = Path(output_dir) / f"results_seed_{seed}.csv"
    pd.DataFrame(results).to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")
