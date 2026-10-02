# Queue Simulation

A simple program that simulates different scenarios to better visualize the operations of a queuing system.

---

## Overview

For this project, we simulate **1,000 different scenarios** with arrival rates between 8 and 12 customers/hour and service rates between 13 and 17 customers/hour. We then compute the utilization factor, the average number of people in the system, the average waiting time in the queue, the average number of people waiting in the queue, and the average time spent in the system.

Additionally, we create histograms for visualization, provide descriptive statistics, and create a sensitivity table and service capacity decision table based on an analysis of the different percentiles.

---

## Prerequisites

* Python 3.14.7
* Matplotlib
* NumPy
* Pandas

---

## Project Structure

```text
queue-simulation/
├── documentation/
│   └── figures/
├── results/
├── README.md
├── simulation.py
└── requirements.txt
```

---

## Results

The simulation results show that the arrival and service rates vary within their respective ranges, leading to different values of ρ, Ls, Lq, Ws, and Wq. These variations affect the performance of the queuing system across the 1,000 simulated scenarios.

The histograms illustrate the distributions of these metrics across the simulated scenarios.

The arrival rate at the **97.5th percentile** is approximately **11.9 customers/hour**. The analysis also determines the minimum service rate required to achieve the desired performance level.

The sensitivity analysis table shows that the arrival rate and minimum required service rate increase as we move from the 50th to the 97.5th percentile. This indicates that higher demand levels require higher service rates to maintain the desired performance level.


