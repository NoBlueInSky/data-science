import numpy as np
from ucimlrepo import fetch_ucirepo
import matplotlib.pyplot as plt

# fetch dataset
automobile = fetch_ucirepo(id=10)

# data (as pandas dataframes)
X = automobile.data.features
y = automobile.data.targets


# Create a function to calculate five number summary
def five_number_summary(data):
    data_max = max(data)
    data_min = min(data)
    data_median = np.median(data)
    data_first_quartile = np.percentile(data, 25)
    data_third_quartile = np.percentile(data, 75)
    data_five_number_summary = [data_min, data_first_quartile, data_median,
                                data_third_quartile, data_max]
    return data_five_number_summary


# Create a function to plot boxplot
def plot_five_number_summary(data, title):
    plt.boxplot(data)
    plt.title(title)
    for name, val in zip(["min", "q1", "med", "q3", "max"],
                         five_number_summary(data)):
        plt.text(1, val, f"{name}= {val:.2f}",
                 ha='center', va='bottom', fontsize=8, color='blue', fontweight='bold')


# Create variable for summary statistics of price of gas and diesel cars
gas_car_price = X['price'][X['fuel-type'] == 'gas']
diesel_car_price = X['price'][X['fuel-type'] == 'diesel']

# Drop missing values
gas_car_price.dropna(inplace=True)
diesel_car_price.dropna(inplace=True)

# Plot boxplot about price of cars in the dataset
plt.subplot(1, 2, 1)
plot_five_number_summary(gas_car_price, 'Price of gas cars')
plt.subplot(1, 2, 2)
plot_five_number_summary(diesel_car_price, 'Price of diesel cars')

# Display the plot
plt.show()
