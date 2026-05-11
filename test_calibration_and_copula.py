import numpy as np
from scipy.optimize import minimize

def test_aggregation():
    print("==================================================")
    print("TEST 1: MAX AGGREGATION VS PROBABILISTIC COPULAS")
    print("==================================================")
    # If p1 and p2 are both 0.4
    p1 = 0.4
    p2 = 0.4
    
    # The heuristic in the framework
    heuristic_risk = max(p1, p2)
    
    # True risk if the modes are statistically independent
    independent_risk = 1 - (1 - p1) * (1 - p2)
    
    # Fréchet-Hoeffding bounds for joint probability
    # If perfectly positively correlated, risk = max(p1, p2)
    # If mutually exclusive (perfectly negatively correlated), risk = min(1, p1 + p2)
    
    print(f"Given Pressure Mode 1 Risk = {p1*100}%")
    print(f"Given Pressure Mode 2 Risk = {p2*100}%")
    print(f"-> Framework Heuristic (max): {heuristic_risk*100}%")
    print(f"-> True Risk if Independent:  {independent_risk*100}%")
    print(f"-> True Risk if Mutually Exclusive: {min(1, p1 + p2)*100}%")
    print("\nResult: The max() function mathematically assumes perfect positive correlation.")
    print("If the pressure modes are independent, the max() function UNDERESTIMATES the true risk.")
    print("Validation: The user's critique is mathematically correct. A true copula is needed.\n")

def negative_log_likelihood(params, phi, y):
    # params = [C, lambda]
    C, lam = params
    # Bound parameters to prevent math errors
    if C <= 0 or lam <= 0:
        return np.inf
        
    ratio = phi / C
    # Calculate probability of transition
    p = 1.0 - np.exp(-(ratio**lam))
    # Clamp probabilities to avoid log(0)
    p = np.clip(p, 1e-7, 1 - 1e-7)
    
    # Log likelihood: sum of y*log(p) + (1-y)*log(1-p)
    nll = -np.sum(y * np.log(p) + (1 - y) * np.log(1 - p))
    return nll

def test_calibration():
    print("==================================================")
    print("TEST 2: MAXIMUM LIKELIHOOD ESTIMATION (MLE) CALIBRATION")
    print("==================================================")
    
    # True parameters of a hidden system
    true_C = 15.0
    true_lam = 3.0
    N = 1000
    
    # Generate 1000 random pressure observations
    np.random.seed(42)
    phi_data = np.random.uniform(0, 30, N)
    
    # Generate actual transition outcomes based on the true model
    true_p = 1.0 - np.exp(-(phi_data / true_C)**true_lam)
    y_data = np.random.binomial(1, true_p)
    
    print(f"Simulated {N} historical observations.")
    print(f"Hidden System Truth: C = {true_C}, lambda = {true_lam}")
    
    # Try to fit the parameters using only the data (phi_data, y_data)
    initial_guess = [10.0, 1.0] # Blind guess
    result = minimize(negative_log_likelihood, initial_guess, args=(phi_data, y_data), method='Nelder-Mead')
    
    est_C, est_lam = result.x
    
    print(f"-> MLE Recovered Capacity (C): {est_C:.2f}")
    print(f"-> MLE Recovered Sharpness (lambda): {est_lam:.2f}")
    
    error_C = abs(true_C - est_C) / true_C
    error_lam = abs(true_lam - est_lam) / true_lam
    
    if error_C < 0.1 and error_lam < 0.1:
        print("\nResult: PASS. The parameters C and lambda CAN be accurately calibrated")
        print("from historical data using Maximum Likelihood Estimation.")
        print("Validation: The framework becomes predictive ONLY AFTER this calibration step.")
    else:
        print("\nResult: FAIL. The parameters could not be recovered.")

if __name__ == "__main__":
    test_aggregation()
    test_calibration()
