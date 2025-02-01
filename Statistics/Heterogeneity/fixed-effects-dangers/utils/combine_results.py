"""
combine_results.py

Assorted utility files for processing simulation results

Functions:
    - combine_results(output_dir: str, seeds: list[int]) -> None:
        Combines individual simulation data files into a common output file.
"""

import pandas as pd
from pathlib import Path

def combine_results(output_dir: str, seeds: list[int]) -> None:
    """
    Combines individual simulation results into a single CSV file.

    Args:
        output_dir (str): Directory containing result CSVs.
        seeds (list[int]): List of seeds used in the simulation.
    """
    result_files = [Path(output_dir) / f"results_seed_{seed}.csv" for seed in seeds]
    all_results = pd.concat([pd.read_csv(file) for file in result_files], ignore_index=True)
    all_results.to_csv(Path(output_dir) / "combined_results.csv", index=False)
