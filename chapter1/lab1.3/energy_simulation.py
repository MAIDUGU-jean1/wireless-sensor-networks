
# import numpy as np
# import matplotlib.pyplot as plt

# # 1. Battery configuration
# C_mAh = 2400
# eta = 0.7

# # 2. Current consumption
# I_act = 20.0
# I_sleep = 0.005
# t_act = 0.05

# # 3. Generate 200 reporting periods
# # From 1 second to 3600 seconds
# T = np.logspace(
#     0,
#     np.log10(3600),
#     200
# )

# # 4. Calculate average current
# I_avg = (
#     I_act * t_act +
#     I_sleep * (T - t_act)
# ) / T

# # 5. Calculate battery lifetime in days
# life_days = (
#     eta * C_mAh / I_avg
# ) / 24

# # 6. Draw the graph
# plt.loglog(T, life_days)

# plt.xlabel("Reporting period T (s)")
# plt.ylabel("Lifetime (days)")

# plt.grid(
#     True,
#     which="both",
#     alpha=0.3
# )

# plt.title("WSN Battery Lifetime Simulation")

# # 7. Display the graph
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt

# C_mAh = 2400
# eta = 0.7

# I_act = 20.0
# I_sleep = 0.005

# T = np.logspace(
#     0,
#     np.log10(3600),
#     200
# )

# # Three active durations in seconds
# active_times = [
#     0.020,
#     0.050,
#     0.200
# ]

# for t_act in active_times:

#     I_avg = (
#         I_act * t_act +
#         I_sleep * (T - t_act)
#     ) / T

#     life_days = (
#         eta * C_mAh / I_avg
#     ) / 24

#     plt.loglog(
#         T,
#         life_days,
#         label=f"Active time = {t_act*1000:.0f} ms"
#     )

# plt.xlabel("Reporting period T (s)")
# plt.ylabel("Lifetime (days)")

# plt.title("Effect of Active Time on Battery Lifetime")

# plt.legend()
# plt.grid(True, which="both", alpha=0.3)

# plt.show()



import numpy as np
import matplotlib.pyplot as plt

C_mAh = 2400
eta = 0.7

I_act = 20.0
I_sleep = 0.005
t_act = 0.05

p = 0.2

T = np.logspace(
    0,
    np.log10(3600),
    200
)

# Without retransmission
I_avg_normal = (
    I_act * t_act +
    I_sleep * (T - t_act)
) / T

life_normal = (
    eta * C_mAh / I_avg_normal
) / 24

# With retransmission
I_avg_retry = (
    I_act * t_act * (1 + p) +
    I_sleep * (T - t_act)
) / T

life_retry = (
    eta * C_mAh / I_avg_retry
) / 24

# Compare the two curves
plt.loglog(
    T,
    life_normal,
    label="Without retransmission"
)

plt.loglog(
    T,
    life_retry,
    label="With retransmission"
)

plt.xlabel("Reporting period T (s)")
plt.ylabel("Lifetime (days)")

plt.title("Effect of Retransmission on Battery Lifetime")

plt.legend()
plt.grid(True, which="both", alpha=0.3)

plt.show()
