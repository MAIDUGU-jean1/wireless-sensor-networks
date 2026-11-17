
import numpy as np

# Random generator
rng = np.random.default_rng(7)

# Simulation configuration
DAYS = 60
DT_H = 0.25

# Node power consumption
P_NODE_MW = 0.5

# Solar panel parameters
PEAK_MW_PER_CM2 = 10.0
SYS_EFF = 0.4


def simulate(area_cm2, batt_mWh, soc0=0.5):

    # Initial stored energy
    soc = soc0 * batt_mWh

    # Total time without power
    outage_h = 0.0

    # Random daily sunlight conditions
    clouds = rng.uniform(0.1, 1.0, DAYS)

    # Simulate each day
    for d in range(DAYS):

        # Simulate each 15-minute period
        for step in range(int(24 / DT_H)):

            h = step * DT_H

            # Solar availability between 6 AM and 6 PM
            sun = (
                np.sin(np.pi * (h - 6) / 12)
                if 6 <= h <= 18
                else 0.0
            )

            # Power collected from the panel
            p_in = (
                area_cm2
                * PEAK_MW_PER_CM2
                * SYS_EFF
                * sun
                * clouds[d]
            )

            # Update stored energy
            soc = min(
                soc + (p_in - P_NODE_MW) * DT_H,
                batt_mWh
            )

            # Check for battery depletion
            if soc <= 0:
                soc = 0.0
                outage_h += DT_H

    return outage_h


# Test all panel and battery combinations
for area in (0.5, 1, 2, 3):

    for cap in (10, 20, 40):

        outage = simulate(area, cap)

        print(
            f"area={area} cm2 "
            f"battery={cap} mWh "
            f"outage={outage:.1f} h"
        )
