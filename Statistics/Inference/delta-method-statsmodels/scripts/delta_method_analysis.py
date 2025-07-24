"""
Example of using the delta method for nonlinear inference.

This module contains a worked example for inference on the
number of years of experience that maximizes earnings using
the statsmodels NonlinearDeltaCov class.

It showcases three methods of NonlinearDeltaCov

- A summary method;
- A confidence interval method;
- A Wald test method.
"""

import numpy as np
import pandas as pd
from statsmodels.stats._delta_method import NonlinearDeltaCov


def max_earn(beta: pd.Series) -> np.ndarray:
    """Calculate the number of years of experience that maximize earnings."""
    return np.array(
        [-50 * beta.loc["experience"] / beta.loc["experience_sq_div"]]
    )


def perform_delta_method_analysis(results):
    """Perform delta method analysis and print results."""
    # Create instance of NonlinearDeltaCov
    delta_ratio = NonlinearDeltaCov(
        max_earn,
        results.params,
        results.cov_params()
    )

    # Confidence interval: approach 1
    summary = delta_ratio.summary(alpha=0.05)
    print(
        "\n Summary for transformed parameter (note incorrect title):",
        "\n",
        summary,
        2 * "\n",
    )

    # Confidence interval: approach 2
    conf_int = delta_ratio.conf_int(alpha=0.05)
    print("Confidence Interval:\n", conf_int, 2 * "\n")

    # Wald test: checking that earnings are maximized after 15 years of work
    wald_test_result = delta_ratio.wald_test(np.array([15]))
    print("Wald Test Result: \n", wald_test_result, 2 * "\n")
