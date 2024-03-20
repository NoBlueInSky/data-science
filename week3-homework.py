import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp

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
ages_five_number_summary = [ages_min, ages_first_quartile, ages_median,
                            ages_third_quartile, ages_max]

plt.rc('font', size=8)
plt.subplot(2, 3, 1)
plt.title('Ages')
plt.boxplot(ages)
for name, val in zip(["min", "q1", "med", "q3", "max"],
                     ages_five_number_summary):
    plt.text(1, val, f"{name}= {val:.2f}",
             ha='center', va='bottom', fontsize=8, color='blue', fontweight='bold')

birth = pd.read_csv('birth-th.csv')
death = pd.read_csv('death-th.csv')

xyears = list(birth.iloc[1][3:])
ybirth_all = list(birth.iloc[2][3:].str.replace(',', '').astype(int))
ybirth_nakornpathom = list(birth.iloc[71][3:].str.replace(',', '').astype(int))
ydeath_all = list(death.iloc[2][3:].str.replace(',', '').astype(int))
ydeath_nakornpathom = list(death.iloc[71][3:].str.replace(',', '').astype(int))

plt.subplot(2, 3, 2)
plt.title('Birth of all people in Thailand')
plt.xlabel('Year')
plt.ylabel('Number of people')
plt.plot(xyears, ybirth_all, color='blue')

plt.subplot(2, 3, 3)
plt.title('Death of all people in Thailand')
plt.xlabel('Year')
plt.ylabel('Number of people')
plt.plot(xyears, ydeath_all, color='red')

plt.subplot(2, 3, 4)
plt.title('Birth of all people in Nakornpathom')
plt.plot(xyears, ybirth_all, color='blue')
plt.xlabel('Year')
plt.ylabel('Number of people')

plt.subplot(2, 3, 5)
plt.title('Death of all people in Nakornpathom')
plt.plot(xyears, ydeath_all, color='red')
plt.xlabel('Year')
plt.ylabel('Number of people')

plt.subplot(2, 3, 6)
plt.title('Birth and Death of all people in Thailand')
plt.plot(xyears, ybirth_all, color='blue')
plt.plot(xyears, ydeath_all, color='red')
plt.xlabel('Year')
plt.ylabel('Number of people')

plt.show()
