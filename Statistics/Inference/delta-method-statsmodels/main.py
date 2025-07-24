"""
main.py
========

Runs an illustration of using the delta method in statsmodels using a wage
regression based on the CPS2009 data.

Blog Post:
-----------

Post Link: 
https://vladislav-morozov.github.io/blog/
statistics/inference/2025-07-23-delta-method-statsmodels/

Author: 
Vladislav Morozov

Steps:
------

1. Fetches the CPS data (internet connection required);
2. Extracts subsample of interest (white married women);
3. Runs the OLS regression of interest.
4. Applies the delta method to a nonlinear transformation of parameters.

The nonlinear transformation of interest is the number of years of experience
that maximizes the expected earnings.

Usage:
------
Run the script using:
    py main.py
or
    python main.py

"""

from scripts.data_preparation import load_and_prepare_data, run_ols_regression
from scripts.delta_method_analysis import perform_delta_method_analysis


def main():
    """Run the delta method example in the post"""
    # Load and prepare data
    data = load_and_prepare_data()

    # Run OLS regression
    results = run_ols_regression(data)

    # Perform delta method analysis
    perform_delta_method_analysis(results)


if __name__ == "__main__":
    main()
