"""
Data preparation script that prepares the wage regression.

This module contains two functions:

- Loading the CPS 2009 dataset and extracting the key sample.
- Running the desired OLS regression.
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.regression.linear_model import OLS

DATA_PATH = ("https://github.com/pegeorge/Econ521_Datasets/"
             "raw/refs/heads/main/cps09mar.csv")


def load_and_prepare_data() -> pd.DataFrame:
    """Load and prepare the data for analysis."""
    cps_data = pd.read_csv(DATA_PATH)

    # Generate variables
    cps_data["experience"] = cps_data["age"] - cps_data["education"] - 6
    cps_data["experience_sq_div"] = cps_data["experience"] ** 2 / 100
    cps_data["wage"] = (
        cps_data["earnings"] / (cps_data["week"] * cps_data["hours"])
    )
    cps_data["log_wage"] = np.log(cps_data["wage"])

    # Filter data
    select_data = cps_data.loc[
        (cps_data["marital"] <= 2) &
        (cps_data["race"] == 1) &
        (cps_data["female"] == 1),
        :
    ]

    return select_data


def run_ols_regression(data: pd.DataFrame) -> OLS:
    """Run OLS regression on the prepared data."""
    exog = data.loc[:, ["education", "experience", "experience_sq_div"]]
    exog = sm.add_constant(exog)
    endog = data.loc[:, "log_wage"]

    results = OLS(endog, exog).fit(cov_type="HC0")
    return results
