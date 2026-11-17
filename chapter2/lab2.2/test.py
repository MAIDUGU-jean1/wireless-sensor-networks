
import numpy as np
import matplotlib.pyplot as plt

# Random number generator
rng = np.random.default_rng(1)

# ADC configuration
N_BITS = 12
VREF = 3.3

# Calculate ADC voltage step
LSB = VREF / (2 ** N_BITS)

# Simulated ADC function
def adc(v):
    return np.clip(
        np.floor(v / LSB),
        0,
        2 ** N_BITS - 1
    ).astype(int)

# Actual input voltage and noise
v_true = 1.234
# noise = 0.002 Thsi was for task 2.2
noise = 0.0001  #new value for task 2.2

# Different averaging sizes
sample_sizes = (1, 4, 16, 64)

results = []

for k in sample_sizes:

    # Generate 1000 groups of k noisy samples
    readings = v_true + rng.normal(
        0,
        noise,
        (1000, k)
    )

    # Convert samples to ADC codes
    codes = adc(readings)

    # Average ADC codes and convert back to voltage
    avg = codes.mean(axis=1) * LSB

    # Calculate standard deviation in mV
    std_mv = avg.std() * 1000

    results.append(std_mv)

    print(
        f"{k:3d} samples -> std = {std_mv:.3f} mV"
    )

# Plot the results
plt.figure()
plt.plot(
    sample_sizes,
    results,
    marker="o"
)

plt.xscale("log", base=2)
plt.yscale("log")
plt.xlabel("Number of samples (K)")
plt.ylabel("Standard deviation (mV)")
plt.title("Noise reduction through averaging")
plt.grid(True)
plt.show()
