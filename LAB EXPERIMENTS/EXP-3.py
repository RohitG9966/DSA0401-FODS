import numpy as np

# Columns: Bedrooms, Square Feet, Sale Price
house_data = np.array([
    [3, 1200, 200000],
    [5, 1800, 350000],
    [4, 1500, 280000],
    [6, 2200, 450000],
    [5, 2000, 400000]
])

selected = house_data[house_data[:, 0] > 4]

avg_price = np.mean(selected[:, 2])

print("Average Sale Price:", avg_price)
