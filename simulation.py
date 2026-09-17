# Author: Ndeye Anta Mbaye
# Date: 18 September 2026
# simulation.py

# Simulate 1,000 scenarios.

# For each scenario:
# Generate the arrival rate, λ, randomly between 8 and 12 customers/hour.

# Generate the current service rate, μ, randomly between 13 and 17 customers/hour.

# For each scenario, calculate ρ, Ls, Lq, Ws, Wq.

# Create histograms showing the distributions of ρ, Ls, Lq, Ws, and Wq.

# Save the simulation results and descriptive statistics as CSV files.

# Assume management wants at least 95% of customers to wait no more than 15 minutes.

# Use the M/M/1 relationship, P(Wq > t) = ρ * exp[−(μ−λ)t]  where t = 15/60 hours.

# Use the 97.5th percentile of λ as the design demand level.

# Determine the minimum service rate μ required to achieve the 95% target.

# Repeat the capacity calculation using the 50th, 75th, 90th, 95th, and 97.5th percentiles of demand and create a sensitivity table.