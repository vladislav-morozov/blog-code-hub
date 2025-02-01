"""
solver.py

Implements a simple generic Generalized Method of Moments (GMM) class.

Classes:
    - GMMSolver: Estimates parameters by minimizing squared moment conditions. 
"""

import numpy as np

from scipy.optimize import minimize
from typing import Callable, List, Dict, Any, Optional

class GMMSolver:
    """
    A Generalized Method of Moments (GMM) solver that estimates parameters by 
    minimizing the weighted squared distance of moment conditions from zero.

    Attributes:
        moment_conditions (Callable[[np.ndarray], np.ndarray]):
            Function returning moment conditions given parameter values.
        constraints (Optional[List[Dict[str, Any]]]):
            List of constraints for parameter optimization.
        initial_guess (np.ndarray):
            Initial parameter values for the optimization.
        weighting_matrix (np.ndarray):
            Weighting matrix for the GMM objective function. Defaults to identity.
        process_func (Callable[[np.ndarray], Dict[str, Any]]):
            Function that processes the optimized parameters into a meaningful format.
    """

    def __init__(
        self,
        moment_conditions: Callable[[np.ndarray], np.ndarray],
        initial_guess: np.ndarray,
        constraints: Optional[List[Dict[str, Any]]] = None,
        weighting_matrix: Optional[np.ndarray] = None,
        process_func: Optional[Callable[[np.ndarray], Dict[str, Any]]] = None
    ) -> None:
        """
        Initializes the GMM solver with the moment conditions and optimization settings.

        Args:
            moment_conditions (Callable[[np.ndarray], np.ndarray]):
                A function that takes a parameter vector and returns moment conditions.
            initial_guess (np.ndarray):
                Initial parameter values for optimization.
            constraints (Optional[List[Dict[str, Any]]], optional):
                Constraints for optimization. Defaults to None.
            weighting_matrix (Optional[np.ndarray], optional):
                Weighting matrix for GMM. Defaults to identity matrix.
            process_func (Optional[Callable[[np.ndarray], Dict[str, Any]]], optional):
                Function to format the final parameter estimates. Defaults to None.
        """
        self.moment_conditions = moment_conditions
        self.initial_guess = np.array(initial_guess)
        self.constraints = constraints if constraints else []
        self.weighting_matrix = (
            np.eye(len(moment_conditions(initial_guess))) if weighting_matrix is None else weighting_matrix
        )
        self.process_func = process_func
        self.estimated_params = None

    def _gmm_objective(self, params: np.ndarray) -> float:
        """
        Computes the GMM objective function: 
        m(θ)ᵀ W m(θ), where m(θ) are the moment conditions.

        Args:
            params (np.ndarray): Current parameter estimates.

        Returns:
            float: The GMM loss function value.
        """
        moments = self.moment_conditions(params) 
        return moments.T @ self.weighting_matrix @ moments

    def minimize(self) -> None:
        """
        Runs the GMM estimation by minimizing the GMM objective function.

        Returns:
            np.ndarray: The estimated parameters.
        """
        result = minimize(self._gmm_objective, self.initial_guess, constraints=self.constraints)

        if not result.success:
            raise ValueError(f"Optimization failed: {result.message}")

        self.estimated_params = result.x

    def process_solution(self) -> Dict[str, Any]:
        """
        Processes the estimated parameters into a meaningful format.

        Returns:
            Dict[str, Any]: Processed output, depends on user-supplied processing function.
        """
        if self.process_func is None:
            return {"parameters": self.estimated_params}
        return self.process_func(self.estimated_params)