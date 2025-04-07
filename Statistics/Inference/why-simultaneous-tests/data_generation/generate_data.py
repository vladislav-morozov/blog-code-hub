"""
generate_data.py

Functions for the data-generation process of the post.

Functions:
    - def generate_data(
            num_observations: int,
            betas: np.ndarray,
            x_mean: np.ndarray,
            x_covar: np.ndarray,
            resid_var: np.ndarray,
            seed: int = None,
        ) -> pd.DataFrame:
        Generates a synthetic dataset according to DGP of the post.
"""

import numpy as np
import pandas as pd


def generate_data(
    num_observations: int,
    betas: np.ndarray,
    x_mean: np.ndarray,
    x_covar: np.ndarray,
    resid_var: np.ndarray,
    seed: int = None,
) -> pd.DataFrame:
    """Generates a dataset with num_observations, normal covariates and shocks.

    Args:
        num_observations (int): number of observations.
        betas (np.ndarray): vector of coefficients.
        x_mean (np.ndarray): mean of covariates
        x_covar (np.ndarray): covariance matrix of covariates
        resid_var (np.ndarray): variance of residual innovations
        seed (int, optional): random seed for reproducibility.

    Returns:
        pd.DataFrame: _description_
    """
    # Initialize RNG
    rng = np.random.default_rng(seed)

    # Draw covariates and residuals, combine into output
    covariates = rng.multivariate_normal(
        x_mean,
        x_covar,
        size=num_observations,
    )
    resids = rng.normal(0, np.sqrt(resid_var), size=num_observations)
    y = (covariates @ betas) + resids

    # Convert output into pandas dataframes with dynamic variable names for X
    covariates_df = pd.DataFrame(
        covariates,
        columns=[f"X{i}" for i in range(covariates.shape[1])],
    )
    y_df = pd.DataFrame(
        y,
        columns=["y"],
    )
    return pd.concat([y_df, covariates_df], axis=1)
