import numpy as np
import pandas as pd

laptops_data = pd.read_csv('laptops_data.csv')

data_array = laptops_data['Device Name'].to_numpy()

sorted_array = np.sort(data_array)
print("Sorted Data: \n", sorted_array)

indexed_data = data_array[:5]
print("First 5 elements: \n", indexed_data)


split_data = np.array_split(data_array, 3)
print("--------------Split Data: \n", split_data)
