import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

ages = [13, 15, 16, 16, 19, 20, 20, 21, 22,
        22, 25, 25, 25, 25, 30, 33, 33, 35,
        35, 35, 35, 36, 40, 45, 46, 52, 70]

ages_max = max(ages)
ages_min = min(ages)
ages_mean = np.mean(ages)
ages_median = np.median(ages)
ages_mode = sp.stats.mode(ages)
ages_midrange = (ages_max + ages_min) / 2
ages_first_quartile = np.percentile(ages, 25)
ages_third_quartile = np.percentile(ages, 75)
ages_five_number_summary = [ages_min, ages_first_quartile, ages_median, ages_third_quartile, ages_max]

plt.title('Ages')
plt.boxplot(ages)
for name, val in zip(["ages_min", "ages_first_quartile", "ages_median", "ages_third_quartile", "ages_max"],
                     ages_five_number_summary):
    plt.text(1, val, f"{name}:{val:.2f}", ha='center', va='bottom', fontsize=8)
plt.show()
