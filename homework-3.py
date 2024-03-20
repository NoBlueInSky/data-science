import numpy as np
import scipy as sp
import pandas as pd

ages = [13, 15, 16, 16, 19, 20, 20, 21, 22,
        22, 25, 25, 25, 25, 30, 33, 33, 35,
        35, 35, 35, 36, 40, 45, 46, 52, 70]

ages_mean = np.mean(ages)
ages_median = np.median(ages)
ages_mod = sp.stats.mode(ages)
ages_midrange = sp.stats.studentized_range(ages)
ages_first_quartile = np.percentile(ages, 25)
ages_third_quartile = np.percentile(ages, 75)

pd.x = ['Mean', 'Median', 'Mode', 'Midrange', 'First Quartile', 'Third Quartile']
pd.y = [ages_mean, ages_median, ages_mod, ages_midrange, ages_first_quartile, ages_third_quartile]

pd.plt.boxplot(pd.x, pd.y)
pd.plt.show()