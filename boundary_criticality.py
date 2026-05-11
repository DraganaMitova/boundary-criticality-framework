import numpy as np
from scipy.stats import norm
from typing import Callable, List, Any, Optional

class PressureMode:
    """
    Represents a specific pressure dimension acting against the boundary.
    It links an arbitrary state evaluator to a capacity threshold and a sharpness parameter.
    """
    def __init__(self, name: str, feature_extractor: Callable[[Any], float], capacity: float, lambda_sharpness: float):
        self.name = name
        self.feature_extractor = feature_extractor
        self.capacity = capacity
        self.lambda_sharpness = lambda_sharpness

    def evaluate_probability(self, system_state: Any) -> float:
        if self.capacity <= 0:
            return 1.0 
        if self.capacity == float('inf'):
            return 0.0 
            
        phi = self.feature_extractor(system_state)
        ratio = max(0.0, phi) / self.capacity
        return 1.0 - np.exp(-(ratio ** self.lambda_sharpness))

class BoundaryCriticalityModel:
    """
    Generic cross-domain risk evaluation engine.
    Allows dynamic registration of custom pressure modes and handles copula aggregation.
    """
    def __init__(self, q_gamma: float = 1.0):
        self.q_gamma = q_gamma
        self.modes: List[PressureMode] = []
        
        # Stochastic Boundary Params
        self.is_stochastic = False
        self.stochastic_capacity = 0.0
        self.stochastic_sigma = 0.0
        
    def add_pressure_mode(self, name: str, feature_extractor: Callable[[Any], float], capacity: float, lambda_sharpness: float):
        """
        Register a custom pressure mode.
        feature_extractor: A function that takes a system_state object and returns a scalar pressure value phi.
        """
        self.modes.append(PressureMode(name, feature_extractor, capacity, lambda_sharpness))
        
    def set_stochastic_boundary(self, capacity: float, sigma: float):
        """
        Enable and configure the analytic stochastic first-passage evaluation.
        Defaults to a zero-drift process over time T.
        """
        self.is_stochastic = True
        self.stochastic_capacity = capacity
        self.stochastic_sigma = sigma
        
    def _evaluate_first_passage(self, T: float) -> float:
        if not self.is_stochastic or self.stochastic_sigma <= 0 or T <= 0:
            return 0.0
        C_eff = self.stochastic_capacity + 0.5 * self.stochastic_sigma
        z = C_eff / (self.stochastic_sigma * np.sqrt(T))
        return 2.0 * (1.0 - norm.cdf(z))
        
    def predict_risk(self, system_state: Any, T: float = 1.0, copula_aggregation: Optional[Callable[[List[float]], float]] = None) -> float:
        """
        Evaluate the total transition risk.
        system_state: An arbitrary data object passed to the registered feature extractors.
        T: Time horizon (used for stochastic analytic calculations).
        copula_aggregation: Optional joint probability function. Defaults to the Fréchet-Hoeffding upper bound max().
        """
        probabilities = [mode.evaluate_probability(system_state) for mode in self.modes]
        
        p_fp = self._evaluate_first_passage(T)
        probabilities.append(p_fp)
        
        if copula_aggregation is None:
            aggregated_p = max(probabilities) if probabilities else 0.0
        else:
            aggregated_p = copula_aggregation(probabilities)
            
        return self.q_gamma * aggregated_p
