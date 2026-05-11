import numpy as np

def simulate_system(T, C0, lambda_k):
    # Time array
    t = np.arange(1, T+1)
    
    # Constant deviation
    D = np.ones(T)
    
    # Accumulated pressure
    phi_A = np.cumsum(D)
    
    # Static capacity (naive application)
    C_static = np.full(T, C0)
    
    # Adaptive capacity (capacity grows twice as fast as pressure)
    # e.g., institutional learning
    C_adaptive = C0 + 2 * phi_A
    
    # Calculate risk using the bounded Weibull-like function proposed earlier
    def calc_risk(phi, C):
        ratio = phi / C
        return 1 - np.exp(-(ratio**lambda_k))
    
    risk_static = calc_risk(phi_A, C_static)
    risk_adaptive = calc_risk(phi_A, C_adaptive)
    
    print(f"--- Stress Test: Adaptive Capacity vs Static Model ---")
    print(f"Time T={T}, Initial Capacity C0={C0}, Threshold Sharpness={lambda_k}")
    print(f"Accumulated Pressure at T: {phi_A[-1]}")
    print(f"Static Capacity at T: {C_static[-1]}")
    print(f"Adaptive Capacity at T: {C_adaptive[-1]}")
    print("-" * 50)
    print(f"Transition Risk (Static Capacity):   {risk_static[-1]*100:.2f}%")
    print(f"Transition Risk (Adaptive Capacity): {risk_adaptive[-1]*100:.2f}%")
    
    if risk_adaptive[-1] < 0.1 and risk_static[-1] > 0.9:
        print("\nResult: The model FAILS if capacity is assumed static,")
        print("but correctly predicts SURVIVAL if capacity dynamics are explicitly coupled.")
        print("Conclusion: The critique is valid. Formal coupled dynamics are required.")

simulate_system(T=1000, C0=100, lambda_k=10)
