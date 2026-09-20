# Author: Ndeye Anta Mbaye
# Date: 19 September 2026
# simulation.py

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulate 1,000 scenarios.
scenarios = []

# For each scenario:
for i in range(1000):
    # Generate the arrival rate, lambda, randomly between 8 and 12 customers/hour.
    arrival_rate = np.random.uniform(low=8, high=12)
    # Generate the current service rate, mu, randomly between 13 and 17 customers/hour.
    service_rate = np.random.uniform(low=13, high=17)

    # For each scenario, calculate rho, Ls, Lq, Ws, Wq
    rho = arrival_rate / service_rate
    ls = rho / (1-rho)
    lq = ls-rho
    ws=ls/arrival_rate
    wq=lq/arrival_rate

    # Append the scenarios to the array
    scenarios.append({
        'arrival_rate': arrival_rate,
        'service_rate': service_rate,
        'rho': rho,
        'ls': ls,
        'lq': lq,
        'ws': ws,
        'wq': wq
    })

# Create histograms showing the distributions of ρ, Ls, Lq, Ws, and Wq
keys = ["rho", "ls", "lq", "ws", "wq"]
for key in keys:
    values = [scenario[key] for scenario in scenarios]
    plt.hist(values, bins=30)
    plt.title(f"Distribution of {key} with 30 bins")
    plt.xlabel(key)
    plt.ylabel("Frequency")
    plt.show()

# Save the simulation results as a CSV file
pd.DataFrame(scenarios).to_csv("results/scenarios.csv", index=False)

# Find the descriptive stats
stats = []
labels = ["arrival_rate", "service_rate", "rho", "ls", "lq", "ws", "wq"]

for label in labels:
    values = [scenario[label] for scenario in scenarios]

    # Find the stats for each metric and append to array
    stats.append({
        "variable": label,
        "mean": round(np.mean(values),3),
        "median": round(np.median(values),3),
        "mode": pd.Series(values).mode().iloc[0],
        "standard deviation": np.std(values),
        "min": np.min(values),
        "max": np.max(values)
    })

# Save descriptive statistics as csv
pd.DataFrame(stats).round(3).to_csv("results/descriptive_statistics.csv", index=False)


# Assume management wants at least 95% of customers to wait no more than 15 minutes.
# Use the M/M/1 relationship, P(Wq > t) = ρ * exp[−(μ−λ)t]  where t = 15/60 hours.
results = []
percentiles = [50, 75, 90, 95, 97.5]

# Use the 97.5th percentile of λ as the design demand level.
# Repeat the capacity calculation using the 50th, 75th, 90th, 95th, and 97.5th percentiles of demand.
for percentile in percentiles:
    lambda_p = np.percentile([scenario["arrival_rate"] for scenario in scenarios], percentile)
    # Determine the minimum service rate μ required to achieve the 95% target.
    min_rate = lambda_p

    while (lambda_p / min_rate) * np.exp(-(min_rate - lambda_p) * (15 / 60)) > 0.05:
        min_rate += 0.01

    rho = lambda_p / min_rate
    p= rho * np.exp(-(min_rate - lambda_p) * (15 / 60))
    results.append({
        "lambda": lambda_p,
        "min_rate": min_rate,
        "rho": rho,
        "probability": p,
    })

# Sensitivity table
sensitivity_table = pd.DataFrame(results, index=[f"{p}th percentile" for p in percentiles], columns=["lambda", "min_rate", "rho", "probability"])
print(sensitivity_table)

# Service capacity decision table
design = sensitivity_table.loc["97.5th percentile"]

capacity_decision = pd.DataFrame({
    "Metric": [
        "Design Demand Level",
        "Arrival rate",
        "Minimum service rate",
        "P(Wq > 15 minutes)",
        "Target probability",
        "95% target achieved?"
    ],
    "Value": [
        "97.5th percentile",
        design["lambda"],
        design["min_rate"],
        design["probability"],
        0.05,
        design["probability"] <= 0.05
    ]
})

print("\nService Capacity Decision Table")
print(capacity_decision)