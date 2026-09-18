# Author: Ndeye Anta Mbaye
# Date: 18 September 2026
# simulation.py

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulate 1,000 scenarios.
scenarios = []

# For each scenario:
for i in range(1000):
    # Generate the arrival rate, λ, randomly between 8 and 12 customers/hour.
    arrival_rate = np.random.uniform(low=8, high=12)
    # Generate the current service rate, μ, randomly between 13 and 17 customers/hour.
    service_rate = np.random.uniform(low=13, high=17)

    # For each scenario, calculate ρ, Ls, Lq, Ws, Wq.
    rho = arrival_rate / service_rate
    ls = rho / (1-rho)
    lq = ls-rho
    ws=ls/arrival_rate
    wq=lq/arrival_rate
    scenarios.append({
        'arrival_rate': arrival_rate,
        'service_rate': service_rate,
        'rho': rho,
        'ls': ls,
        'lq': lq,
        'ws': ws,
        'wq': wq
    })

#Verify that we have 1000 elements
print(len(scenarios))

# Create histograms showing the distributions of ρ, Ls, Lq, Ws, and Wq.
keys = ["rho", "ls", "lq", "ws", "wq"]
for key in keys:
    values = [scenario[key] for scenario in scenarios]
    plt.hist(values, bins=30)
    plt.title(f"Distribution of {key} with 30 bins")
    plt.xlabel(key)
    plt.ylabel("Frequency")
    plt.show()

# Save the simulation results and descriptive statistics as CSV files.
pd.DataFrame(scenarios).to_csv("results/scenarios.csv", index=False)

# Assume management wants at least 95% of customers to wait no more than 15 minutes.
# Use the M/M/1 relationship, P(Wq > t) = ρ * exp[−(μ−λ)t]  where t = 15/60 hours.

# Use the 97.5th percentile of λ as the design demand level.

# Determine the minimum service rate μ required to achieve the 95% target.

# Repeat the capacity calculation using the 50th, 75th, 90th, 95th, and 97.5th percentiles of demand and create a sensitivity table.